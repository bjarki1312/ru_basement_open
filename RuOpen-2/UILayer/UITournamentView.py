from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UIOngoingTournaments import UIOngoingTournaments
from UILayer.UIFutureTournaments import UIFutureTournaments
from UILayer.UIFinishedTournaments import UIFinishedTournaments
from UILayer.UIClearTerminal import UIClearTerminal
import time


class UITournamentView:

    def __init__(self):

        self.UIClearTerminal = UIClearTerminal()
        self.UIOngoingTournaments = UIOngoingTournaments()
        self.UIFutureTournaments = UIFutureTournaments()
        self.UIFinishedTournaments = UIFinishedTournaments()
        self.Terminal = UIClearTerminal()


    def display_tournaments(self):
        '''
        print("1. View ongoing tournaments")
        print("2. View finished tournaments")
        print("3. View future tournaments")'''
        
        self.UIClearTerminal.printHeader("Tournament view", ["1. View ongoing tournaments", "2. View finished tournaments", "3. View future tournaments\n"], bottom="")


    def input_for_tournaments(self):
        """Displays a list of options for the user to choose from, checks the input and calls the
            function connected to the given input."""
        self.Terminal.clear()

        valid_input_list = ["1", "2", "3"]
        self.display_tournaments()
        print("\nWhat would you like to view?")
        user_input = input("\n\tPlease enter a number for option: ").lower()
        
        while user_input not in valid_input_list and user_input != 'b':
            
            print("Please enter a valid number for option")
            time.sleep(1.5)
            self.Terminal.clear()
            
            self.display_tournaments()
            print("\nWhat would you like to view?")
            user_input = input("\n\tPlease enter a number for option: ").lower()
        

        if user_input == "1":
            self.UIOngoingTournaments.input_for_ongoingTournaments()
            self.input_for_tournaments()

        elif user_input == "2":
            self.UIFinishedTournaments.input_for_finishedTournaments()
            self.input_for_tournaments()

        elif user_input == "3":
            self.UIFutureTournaments.input_for_futureTournaments()
            self.input_for_tournaments()

