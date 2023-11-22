import time
from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UITeamsAndPlayers import UITeamsAndPlayers
from UILayer.UISchedule import UISchedule
from UILayer.UIScoreboardNavigator import UIScoreboardNavigator

class UIOngoingTournaments:

    def __init__(self):

        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()
        self.UITeamsAndPlayers = UITeamsAndPlayers()
        self.UISchedule = UISchedule()
        self.UIScoreboardNavigator = UIScoreboardNavigator()

    def check_input(self, data):

        if data.lower() == "b":
            return "b"
        else:
            return data 

    def select_tournament(self):

        tournament_list = self.display_all_ongoingTournaments()
        print("\n\n\tWhat tournament would you like to view?")

        user_input = input(("\nPlease enter a number for option or [B/b] to go back: ")).lower()
        while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) > (len(tournament_list)):
            
            if user_input.lower() == "b":
                break

            print("\tPlease enter valid number for tournament")
            time.sleep(1.2)
            user_input = self.select_tournament()
            break
        
        if user_input == "b":
            return self.check_input(user_input)
        
        
        tournament_choosen = tournament_list[int(user_input) - 1]
        return tournament_choosen

    def display_all_ongoingTournaments(self):
        
        self.Terminal.clear()
        future_tournament = self.LLWrapper.getOngoingTournaments()
        tournament_list = []
        nr = 0

        self.Terminal.printHeader("Ongoing Leagues")
        
        for tournament in future_tournament:
            nr += 1
            print(f"\n  {nr}. Name: {tournament.name} \n     Duration: {tournament.start_date} - {tournament.end_date}")
            tournament_list.append(tournament)
        
        if len(tournament_list) == 0:
             print(f"\n     Currently there are no tournaments scheduled :/")
        
        return tournament_list
    

    def display_tournament_options(self, tournament):
        self.Terminal.clear()
        self.Terminal.printHeader("League is currently ongoing", ['League: ' + tournament.name]) 
        print("\n What would you like to do?\n")
        print("\t1. Register scoreboard\n\t2. View teams and players\n\t3. View and change Schedule")
        
        user_input = input("\n\tPlease enter a number for option or [B/b] to go back: ")
        while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) > 4:
            
            if user_input.lower() == "b":
                break

            print("\t\tPlease enter valid number for tournament")
            time.sleep(1.2)
            user_input = self.display_tournament_options(tournament)
            break

        if user_input == "b":
            return self.check_input(user_input)

        return int(user_input)

    def input_for_ongoingTournaments(self):
        pass

    def input_for_ongoingTournaments(self):

        proccessing_inputs = [self.select_tournament, self.display_tournament_options]
        progress = 0

        while progress < len(proccessing_inputs):

            if progress == 1:
                data  = proccessing_inputs[progress](self.tournament)
                
                if data == 1:
                    self.UIScoreboardNavigator.input_for_scoreboard(self.tournament.id)
                    
                
                elif data == 2:
                    self.UITeamsAndPlayers.input_for_teams_and_players(self.tournament.id)
                    
                    
                elif data == 3:
                    self.UISchedule.input_for_schedule(self.tournament.id)
    
                
            else:
                data = proccessing_inputs[progress]()

            if data == "b" and progress == 0:
                break
            
            elif data == "b":
                progress -= 1
            
            elif progress == 0:
                self.tournament = data
                progress += 1