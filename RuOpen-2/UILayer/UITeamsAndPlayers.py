from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
import time

class UITeamsAndPlayers:

    def __init__(self) -> None:
        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()


    def get_team_ID(self, ID):
        """gets team ID from LLWrapper and returns it"""

        team_list = self.LLWrapper.getTeamFromID(ID)
        return team_list


    def get_players_ID(self, ID):
        """gets players ID from LLWrapper and returns it"""

        players_list = self.LLWrapper.getPlayersFromID(ID)
        return players_list

    
    def display_option_for_team(self):
        """Displays options for user to choose from, to see information about the teams and the players"""

        print("\n\tWhat information do you want to see?")
        print("\n\t1. Quality Points of all players\n\t2. Scores of all players\
              \n\t3. Ranking of the teams")


    def display_quality_points(self, ID):
        """Displays the quality points of all players in a tournament"""

        self.Terminal.clear()
        print(f"Quality points of all players for league: '{self.LLWrapper.getTournmanetByID(ID)[0].name}'\n")
        players_list = self.LLWrapper.getPlayersFromID(ID,qpsort=True)
        player_count = 1

        for player in players_list:
            
            if player_count > 9:
                print(f"\t{player_count}. {player.name:<20} QP: {player.qp}")
            else:
                print(f"\t {player_count}. {player.name:<20} QP: {player.qp}")
            player_count += 1
        
        user_input = input("\nPlease enter '[B/b]' to go back: ")
        while user_input.lower() != "b":

            print("Please enter 'B' or 'b' to go back")
            time.sleep(1.2)
            user_input = self.display_quality_points(ID)
            break
            
        return user_input

    def display_scores_for_players(self, ID):
        """Displays the scores of all players in a tournament"""

        self.Terminal.clear()
        print(f"Scores of all players for tournament: '{self.LLWrapper.getTournmanetByID(ID)[0].name}'\n")
        players_list = self.LLWrapper.getPlayersFromID(ID, qpsort=True)
        player_count = 1

        for player in players_list:
            
            if player_count > 9:
                print(f"\t{player_count}. {player.name:<20} Scores: {player.score}")
            else:
                print(f"\t {player_count}. {player.name:<20} Scores: {player.score}")
            player_count += 1
        
        user_input = input("\nPlease enter '[B/b]' to go back: ")
        while user_input.lower() != "b":

            print("Please enter 'B' or 'b' to go back")
            time.sleep(1.2)
            user_input = self.display_quality_points(ID)
            break
            
        return user_input


    def display_ranking_teams(self, ID):
        """Displays the ranking of all teams in a tournament"""
        self.Terminal.clear()
        self.Terminal.printHeader("Ranking of league", ['League: ' + self.LLWrapper.getTournmanetByID(ID)[0].name]) 
        ranked_team_list = self.LLWrapper.getRankedTeams(ID)
        print(f"\n\t{'   Team name' : <18}\tWins\tLoss")

        counter = 1
        for team in ranked_team_list:
            print(f"\t{counter}. {team.team_name : <18} Wins:{str(team.wins) : >2} Loss:{str(team.loss) : >2} ")
            counter += 1

        input("\n\tPress 'Enter' to go back: ")
        
    def display_teams_and_players(self, ID):
        """Displays information of all teams in a tournament and the players in the teams
            then asks the user to choose an option to see more information about the teams or players
            or both"""
            
        self.Terminal.clear()

        team_list = self.get_team_ID(ID)
        tournament_name = self.LLWrapper.getTournmanetByID(ID)[0].name
        self.Terminal.printHeader("Overview of teams for league", ['League: ' + tournament_name])  

        for team in team_list:
            
            for i in range(len(team.players)):
                team.players[i] += '\n\t\t'
            
            print(f"\nTeam: {team.team_name}\n\tPlayers: {' '.join(team.players)}")
        
        self.display_option_for_team()
        user_input = input("\nPlease enter a number for option or [B/b] to go back: ")
        while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) > 4:

            if user_input == "b" or user_input == "B":
                break
            
            print("Please enter valid number for tournament")
            time.sleep(1.2)

            (user_input, ID) = self.display_teams_and_players(ID)
            if user_input == "b" or user_input == "B":
                return (user_input, ID)

        return (user_input, ID)


    def input_for_teams_and_players(self, ID):
        """Function that checks the user input and if it matches one of the given options
        the function will call another function that displays the information the user wants to see"""
        
        proccessing_inputs = [self.display_teams_and_players]
        progress = 0

        while progress < len(proccessing_inputs):
            
            if progress == 0:
                
                data, ID = proccessing_inputs[progress](ID)

                if data == "b" or data == "B":
                    break
                
                elif data == "1":
                    self.display_quality_points(ID)
                
                elif data == "2":
                    self.display_scores_for_players(ID)                

                elif data == "3":
                    self.display_ranking_teams(ID)
               
                
                

            

            

                
            

        

        