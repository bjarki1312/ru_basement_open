from os import system, name
from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UICreateTeam import UICreateTeam

class UICreatClub:

    def __init__(self):
        
        self.Terminal = UIClearTerminal()
        self.UICreateTeam = UICreateTeam()
    

    def check_input(self, data):
        """Checks if input is 'b' or not, if 'b' returns 'b' else returns data"""
        if data.lower() == "b":
            return "b"
        else:
            return data


    def name_of_club(self):
        """Asks the user for the name of the club, if 'B/b' is entered it returns 'b'
            else it returns the name of the club"""
        
        print("\nName of your club?")
        club_name = input('\n\tEnter name of your club?: ')
        return self.check_input(club_name)


    def address_of_club(self):
        """Asks the user for the address of the club, if 'B/b' is entered it returns 'b'
            else it returns the address of the club"""
            
        print("\nAddress of your club?")
        club_address = input("\n\tEnter address of your club: ")
        return self.check_input(club_address)


    def club_phone_number(self):
        """Ask the user for the clubs phone number, if 'B/b' is entered it returns 'b'
        else it returns the phone number of the club"""
        
        print("\nThe clubs phone number? (example: 5540573)")
        club_phone = input("\n\tEnter phone number of your club: ")
        
        while len(club_phone) != 7 or not club_phone.isdigit():
            
            if club_phone.lower() == "b":
                break

            print("Enter 7 digits for number, please try again")
            club_phone = input("\n\tEnter phone number: ")

        return self.check_input(club_phone)


    def inputs_for_club(self, LLWrapper):
        """Works through the inputs for the club, if 'B/b' is entered the user is returned to the previous input
            and the value is removed from the club_values list. If the user has entered all the inputs the function
            he is prompted to create another club, if he chooses to do so the function is called again. If he input is 
            'n' and number of teams is less than two the user needs to add more teams or clubs"""
            
        self.LLWrapper = LLWrapper
        processing_inputs = [self.name_of_club, self.address_of_club, self.club_phone_number]
        club_values = []
        progress = 0
        team_count = 0

        while progress < len(processing_inputs):
            
            if progress == 0:
                 self.Terminal.printHeader("Create a Club", ["Please register a club for your tournament"])
            
            data = processing_inputs[progress]()
            
            if data == "b" and progress == 0:
                pass
            
            elif data == "b":
                progress -= 1
                club_values.pop()
            else:
                progress += 1
                club_values.append(data)

            if progress == (len(processing_inputs)):
               
                self.LLWrapper.generateNewClub(club_values)
                team_count += self.UICreateTeam.inputs_for_team(self.LLWrapper, club_values[0])
                
                while True:                    
                    
                    ask_again = input("Would you like to add another Club [Y/y]/[N/n]?: ").lower()
        
                    if ask_again == 'y':
                        club_values = []
                        progress = 0
                        break

                    elif ask_again == 'n':
                        if team_count < 2:
                            print("\nAt least two teams are needed to create a tournament.\nPlease create a new team from clubs to continue.")
                            club_values = []
                            progress = 0
                        break
                    else:
                        print("\nPlease Enter either [Y/y] for yes or [N/n] for no")
