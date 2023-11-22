from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UISchedule import UISchedule
from UILayer.UIScoreboard import UIScoreboard
import time

class UIScoreboardNavigator:

    def __init__(self) -> None:
        
        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()
        self.UISchedule = UISchedule()


    def select_match_to_register(self, ID):

        self.UISchedule.display_upcoming_rounds(ID)
        print("\n\n\tWhat match would you like to register score to?")
        
        user_input = input("\nSelect number of round which you want to register score of a game or enter [B/b] to go back: ")
        while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) > (self.UISchedule.round_count):
            
            if user_input.lower() == "b":
                return "b"

            print("\tPlease enter valid number for tournament")
            time.sleep(1.2)

            user_input = self.select_match_to_register(ID)
            if user_input == "b":
                return "b"
            else:
                break
        
        user_input_two = input("Select nr. of game to register scores to or enter [B/b] to go back: ")
        while user_input_two.isdigit() == False or int(user_input_two) < 1 or int(user_input_two) > (self.UISchedule.game_count):
            
            if user_input_two.lower() == "b":
                return self.select_match_to_register(ID)
            
            print("\t\tPlease enter valid number of round or [B/b]")
            time.sleep(1.2)

            user_input_two = self.select_match_to_register(ID)
            if user_input_two == "b":
                return self.select_match_to_register(ID)
            else:
                break
        
        self.games_list = self.LLWrapper.getAllGames()
        self.right_index = ((int(self.UISchedule.game_count)*7)*(int(user_input) - 1) + ((int(user_input_two) - 1)*7))
        teams_list = self.LLWrapper.getTeamFromID(ID)
        self.game = self.games_list[self.right_index]
         
        
        for team in teams_list:
            if team.team_name == self.game.home_team.replace(" [W]", "").replace(" [L]", ""): # removing win/loss status for comparison
               self.home_players = [member for member in team.players]
            elif team.team_name == self.game.away_team.replace(" [W]", "").replace(" [L]", ""):
                self.away_players = [member for member in team.players]        

    
    def input_for_scoreboard(self, ID):

        processing_inputs = [self.select_match_to_register]
        progress = 0

        while progress < len(processing_inputs):

            if progress == 0:
                data = processing_inputs[progress](ID)

            if progress == 0 and data != 'b':
                
                
                score_board = UIScoreboard(self.game.home_team, self.home_players, self.game.away_team, self.away_players, self.game.date)
                score_board.fillScoreboard()

                score_board.fillScore()
                print(score_board)
                
                score_board.askQualityPoints()
                score_board.printQualityPoints()
                results_dict = score_board.getData()
                
                
                self.home_players = [name.lower() for name in self.home_players]
                self.away_players = [name.lower() for name in self.away_players]
                
                
                qp_from_dict = results_dict["QualityPoints"]
                self.LLWrapper.logPlayerPoints(ID, qp_from_dict, self.home_players, self.away_players)
                

                # "Team_Score" = [home_score, away_score]
                scores_from_dict = results_dict["Team_Score"]

            
                self.LLWrapper.registerWinsnLoss(ID, scores_from_dict, self.game.home_team, self.game.away_team)

                # Taka quilaty points attributes síðast ásamt team score
                counter = 0
                player_count = 0
                for i in range(7):
                    
                    if i == 0:
                        hometeam = self.games_list[self.right_index + counter].home_team.replace(" [W]", "").replace(" [L]", "")
                        awayteam = self.games_list[self.right_index + counter].away_team.replace(" [W]", "").replace(" [L]", "")
                        if scores_from_dict[0] > scores_from_dict[1]:# .replace(" [W]", "").replace(" [L]", "")
                            self.games_list[self.right_index + counter].home_team = hometeam + ' [W]'
                            self.games_list[self.right_index + counter].away_team = awayteam + ' [L]'
                        else:
                            self.games_list[self.right_index + counter].away_team = awayteam + ' [W]'
                            self.games_list[self.right_index + counter].home_team = hometeam + ' [L]'

                    if i < 4:

                        # Home team
                        self.games_list[self.right_index + counter].home_leg = results_dict["ScoreData"][i + 1][0]
                        self.games_list[self.right_index + counter].home_player = results_dict["PlayerList"][0][player_count]
                        # Away team
                        self.games_list[self.right_index + counter].away_leg = results_dict["ScoreData"][i + 1][1]
                        self.games_list[self.right_index + counter].away_player = results_dict["PlayerList"][1][player_count]
                        player_count += 1

                    elif i == 4 or i == 5:
                        
                        # Home team
                        self.games_list[self.right_index + counter].home_leg = results_dict["ScoreData"][i + 1][0]
                        # Away team
                        self.games_list[self.right_index + counter].away_leg = results_dict["ScoreData"][i + 1][1]
                        for _ in range(2):
                            # Home team
                            self.games_list[self.right_index + counter].home_player.append(results_dict["PlayerList"][0][player_count])
                            # Away team
                            self.games_list[self.right_index + counter].away_player.append(results_dict["PlayerList"][1][player_count])
                            player_count += 1

                    elif i == 6:
                        
                        # Home team
                        self.games_list[self.right_index + counter].home_leg = results_dict["ScoreData"][i + 1][0]
                        # Away team
                        self.games_list[self.right_index + counter].away_leg = results_dict["ScoreData"][i + 1][1]
                        for _ in range(4):
                            # Home team
                            self.games_list[self.right_index + counter].home_player.append(results_dict["PlayerList"][0][player_count])
                            # Away team
                            self.games_list[self.right_index + counter].away_player.append(results_dict["PlayerList"][1][player_count])
                            player_count += 1
                    
                    counter += 1 

                # Skra games list aftur i json
                self.LLWrapper.storeGamesToFile(self.games_list)
                print("\033[0;0m")
                break

            else:
                break

