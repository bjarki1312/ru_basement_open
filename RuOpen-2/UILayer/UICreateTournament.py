from os import system, name
from LLlayer.LLWrapper import LLWrapper
from UILayer.UICreateClub import UICreatClub
from UILayer.UIClearTerminal import UIClearTerminal
from datetime import datetime

class UICreateTournament:
    
    def __init__(self):
        
        self.LLWrapper = LLWrapper()
        self.UICreateClub = UICreatClub()
        self.Terminal = UIClearTerminal()


    def check_input(self, data):

        if data.lower() == "b":
            return "b"
        else:
            return data


    def tournament_header(self):
        """Prints out a header for the tournament menu"""
        
        print("-"*13 + "Start a New Tournament" + "-"*13)


    def tournament_footer(self):
        """Prints out a footer for the tournament menu"""
        
        print("-"*48)


    def printHeader(self, title, bottom=""):
        """Prints out a header with a title, back and home options and a bottom line"""
        
        print(f"{title :-^48}")
        print(f"{'B/b: Back' : ^48}")
        print(f"{'H/h: Home' : ^48}")
        print(f"{bottom :-^48}")
    

    def back_or_home(self):
        """Prints out back and home options"""
        
        print("B/b: Back\nH/h: Home")
    

    def tournament_info(self):
        """Asks for tournament name and checks if a tournament with the same name already exists
            if it does it asks for another name else it checks the input and returns it"""
            
        print("\nWhat would you like the tournament to be called?")
        tournament_name = input("\n\tEnter name: ")
        tournaments_list = self.LLWrapper.getAllTournaments()
        index = 0
        
        # Checking if Tournament name already exists
        while index < len(tournaments_list):
            
            if tournaments_list[index].name.lower() == tournament_name.lower():

                    print("Tournament with same name exists, please type in another name")
                    tournament_name = input("\n\tEnter name: ")
                    index = 0
            else:
                index += 1

        return self.check_input(tournament_name)


    def host_info(self):
        """Asks for host name, checks the input and returns it"""
        
        # Host Name
        print("\nWho's hosting the tournament?")
        data =  input("\n\tEnter name: ")
        return self.check_input(data)


    def host_phone_nr(self):
        """Asks for host phone number, checks if the length is 7 otherwise it prompts user to try again
        if the input is 'b' it is returned else the input is returned"""
        
        # Host Phone nr
        print("\nThe host's phone number? (example: 5540573)")
        host_phone_number = input("\n\tEnter phone number: ")
        
        while len(host_phone_number) != 7 or not host_phone_number.isdigit():
            
            if host_phone_number.lower() == "b":
                break

            print("Enter 7 digits for number, please try again")
            host_phone_number = input("\n\tEnter phone number: ")

        return self.check_input(host_phone_number)
    

    def tournament_start(self, b_not_allowed = None):
        """Asks for tournament start date, checks for the correct format,
        if the input is 'b' it is returned else the input is returned"""
        
        print("\nWhen will the tournament be held? (example dd-mm-yyyy)\n")
        start_date = input("\tEnter starting date: ")
        
        while self.Terminal.check_date(start_date) == datetime.min:
            
            if start_date == "b" and b_not_allowed != 1:
                return "b"
            print("Incorrect date format")
            print("\nWhen will the tournament be held? (example dd-mm-yyyy)\n")
            start_date = input("\tEnter starting date: ")
        
        self.start_date = self.Terminal.check_date(start_date)
        return self.check_input(datetime.strftime(self.start_date, "%d/%m/%Y")) 


    def tournament_end(self, b_not_allowed = None):
        """Asks for tournament end date, checks for the correct format and 
        if the end date is earlier than the start date, if the input is 'b' it is returned else 
        the input is returned"""
        
        end_date = input("\tEnter end date: ")
        checked_date = self.Terminal.check_date(end_date)
        while checked_date == datetime.min or (checked_date < self.start_date):
            
            if end_date == "b" and b_not_allowed:
                return "b"

            if checked_date < self.start_date:
                print("End date is earlier than start date\n")
            else:
                print("Incorrect date format")
            
            end_date = input("\tEnter end date: ")
            checked_date = self.Terminal.check_date(end_date)
        
        self.end_date = checked_date

        return self.check_input(datetime.strftime(checked_date, "%d/%m/%Y"))


    def tournament_type(self):
        """Asks for tournament type, checks if the input is 'b' or '1' otherwise it prompts user to try again"""
        
        print("\nWhat kind of tournament will this be?\nAvailable types:\n\n\t1. Darts")
        tourn_type = input("\tEnter a number: ")

        while tourn_type != "1":

            if tourn_type.lower() == "b":
                break

            print("Number is not connected to a tournament type")
            tourn_type = input("\n\tEnter a number: ")

        return self.check_input(tourn_type)
    
    
    def enter_rounds(self):
        """Asks for number of rounds, checks if the input is 'b' or a number
            otherwise it prompts user to try again"""
           
        print("\nHow many rounds will be played?")
        num_of_round = input("\n\tEnter number: ")

        while not num_of_round.isdigit():
            
            print("Please enter a number")
            num_of_round = input("\n\tEnter number: ")
        
        return self.check_input(num_of_round)
    

    def check_if_tournament_crammed(self, LLWrapper, tournament_values):
        """Checks if the amount of rounds that the user wants the tournament to be fits into the amount of days
        that the tournament is going to be held. If it doesn't it prints a warning message, and asks the user if
        they want to continue with the tournament or want to change the number of days."""
        
        days = (self.end_date - self.start_date).days + 1 # counting days included not between
        tournaments_list = self.LLWrapper.getAllTournaments()
        current_tournment_id = tournaments_list[-1].id
        
        team_list = self.LLWrapper.getTeamFromID(current_tournment_id)
        schedule_list = self.LLWrapper.gameScheduler(team_list, rounds = tournament_values[-1])
        
        round_length = len(schedule_list)
        
        if round_length > days:

            print("\nSince the number of days is too small compared to the")
            print("number of rounds, your tournament might be little crammed.\n")
            print(f"Extend the tournament length to at least {round_length-days} day/s")
            print("Would you like to change the dates of the tournament or keep schedule")
            
            user_input = input("Enter [Y/y] for yes, or [N/n] for no: ").lower()
            while user_input != "y" or user_input != "n":

                if user_input == 'y':
                    tournament_values[3] = self.tournament_start(1)
                    tournament_values[4] = self.tournament_end(1)
                    break
                elif user_input == 'n':
                    break
                else:
                    print("Please enter valid input [Y/y] or [N/n]")
                    user_input = input("Enter [Y/y] for yes, or [N/n] for no: ").lower()
        
        LLWrapper.generateNewTournament(tournament_values)
        self.LLWrapper.createScheduleForTournament(current_tournment_id, [self.start_date, (self.end_date - self.start_date).days + 1], rounds = tournament_values[-1])


    def inputs_for_tournament(self):
        """Works through the inputs for a new tournament and returns a list of the inputs that are returned
        to the datalayer, if 'b' is entered it brings the user 1 step back in the process"""
        
        self.Terminal.printHeader("Start a new tournament")
        processing_inputs = [self.tournament_info, self.host_info, self.host_phone_nr, self.tournament_start,\
                             self.tournament_end, self.tournament_type, self.enter_rounds]
        tournament_values = []
        progress = 0
      
        while progress < len(processing_inputs):
    
            data = processing_inputs[progress]()

            if data == "b" and progress == 0:
                break

            elif progress == (len(processing_inputs) - 2) and data == "b":
                progress -= 2
                for _ in range(2):
                    tournament_values.pop()

            elif data == "b":
                progress -= 1
                tournament_values.pop()
            
            else:
                progress += 1
                tournament_values.append(data)
           
            if progress == (len(processing_inputs)):
                
                self.LLWrapper = LLWrapper()
                self.LLWrapper.generateNewTournament(tournament_values)
                self.LLWrapper.generateNewHost(tournament_values[1:3])
                self.UICreateClub.inputs_for_club(self.LLWrapper)
                break
        
        if tournament_values:
            self.check_if_tournament_crammed(self.LLWrapper, tournament_values)
        else:
            pass
    
