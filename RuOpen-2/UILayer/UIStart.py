from UILayer.UICreateTournament import UICreateTournament
from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UITournamentView import UITournamentView
#from UILayer.UIScoreboard import UIScoreboard
import os
import time


class UIStart:
    def __init__(self) :
        
        path = f"UITextFiles{os.sep}MainMenu.txt"
        dir = os.path.dirname(__file__)
        self.file_name = os.path.join(dir, os.pardir, path)

        self.UICreateTournament = UICreateTournament()
        self.UITournamentView = UITournamentView()
        self.Terminal = UIClearTerminal()    

    def display_header(self):
        """Displays the header of the program"""
        ru_open_display = open(self.file_name, 'r')
        counter = 0
        for line in ru_open_display:
            line = line.strip()

            if counter < 6:
                 print(f"\t\033[1;31;49m{line}\033[0;0m")
            else:
                print(f"\t\033[1;33;49m{line}\033[0;0m")
            counter += 1               
    
            
    def display_start(self):
        """Displays the start menu options"""
        print("\t\t\t\t\t\t\t\t\t    ___")
        print("\t\t\t\tWelcome to RU Basement Open\t\t  /\ _ /\\\n\t____\t\t\t\t\t\t\t\t / /\ /\ \\")
        print("\t\___\_.:::::::.___\t1. Make a new tournament\t\t|---(*)---|")
        print("\t/___/ ':::::::'\t\t2. See ongoing tournaments\t\t \ \/_\/ /\n\t\t\t\t\t\t\t\t\t  \/___\/") 

    
    def input_menu(self):
        """Takes input from the user and calls the appropriate function"""
        self.Terminal.clear()
        self.display_header()
        self.display_start()
        option_input = input("\t\t\t\tWhat would you like to do?: ")

        while True:
            
            if option_input == "1":
                
                print("Option 1 was selected")
                self.Terminal.clear()
                self.UICreateTournament.inputs_for_tournament()
                
            elif option_input == "2":

                print("Option 2 was selected")
                self.Terminal.clear()
                #scoreboard = UIScoreboard()
                #scoreboard.fill_scoreboard()
                #scoreboard.fill_score()
                self.UITournamentView.input_for_tournaments()
                
            else:
                print("\t\t\tInvalid input, try again")
                time.sleep(1.2)
                self.Terminal.clear()
            
            self.Terminal.clear()
            self.display_header()
            self.display_start()
            option_input = input("\t\t\t\tWhat would you like to do?: ")
