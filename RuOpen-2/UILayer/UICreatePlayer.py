from os import system, name
from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
from datetime import datetime


class UICreatePlayer:

    def __init__(self):
        
        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()


    def check_input(self, data):
        """Check if input is 'b' or not, if 'b' return 'b' else return data"""
        
        if data.lower() == "b":
            return "b"
        else:
            return data
    

    def get_email(self):
        """
        Gets a player's email from user input

        Returns:
            string: email or "b" if user wants to go back
        """   
             
        print("\nEmail for player?")
        email = input("\n\tEnter email for player: ")
        while "@" not in email or "." not in email:
            if email.lower() == "b":
                return "b"
            if email == "":
                print("You have to enter an email, please try again")
            else:
                print("Incorrect email format, please try again")
            email = input("\n\tEnter email for player: ")
        return self.check_input(email)


    def get_ssn(self):
        """
        Gets a player's social security number from user input

        Returns:
            string: ssn or "b" if user wants to go back
        """
        
        print("\nSocial security number (If None, press 'Enter')")
        # Removing spaces and dashes from input to get pure numbers
        ssn = input("\n\tEnter SSN: ").replace(" ", "").replace("-", "")
        while len(ssn) != 10 or ssn.isdigit() == False:
            if ssn == "":
                return ""
            if ssn.lower() == "b":
                return "b"

            print("Enter 10 digits for SSN, please try again")
            ssn = input("\n\tEnter SSN: ").replace(" ", "").replace("-", "")
        return self.check_input(ssn)


    def get_birthday(self):
        """Gets a player's birthday from user input and makes sure it is a valid date format"""     
        
        print("\nBirthday for player?")
        birthday = input("\n\tEnter birthday: ")

        checked_birthday = self.Terminal.check_date(birthday)

        while checked_birthday == datetime.min:
            
            if birthday.lower() == "b":
                return "b"

            print("Incorrect date")
            birthday = input("\n\tEnter birthday: ")
            checked_birthday = self.Terminal.check_date(birthday)

        return self.check_input(birthday)


    def get_address(self):
        """Asks user for address and returns it, if 'B/b' is entered returns 'b'"""
        
        print("\nAddress for player?")
        addr = input("\n\tEnter address: ")
        return self.check_input(addr)


    def home_phone_number(self):
        """Ask the user for the players home phone number, if phone number is not 7 digits of length
            the program prints an error and asks user for a new input, if 'B/b' is entered it returns 'b'"""
            
        print("\nThe player home phone number? (example: 5540573)")
        home_phone = input("\n\tEnter home phone number for player: ")
        
        while len(home_phone) != 7:
            
            if home_phone.lower() == "b":
                break

            print("Enter 7 digits for number, please try again")
            home_phone = input("\n\tEnter home phone number for player: ")

        return self.check_input(home_phone)


    def personal_phone_number(self):
        """Ask the user for the players personal phone number, if phone number is not 7 digits of length
            the program prints an error and asks user for a new input, if 'B/b' is entered it returns 'b'"""
        
        print("\nThe player GSM phone number? (example: 5540573)")
        home_phone = input("\n\tEnter GSM phone number for player: ")
        
        while len(home_phone) != 7:
            
            if home_phone.lower() == "b":
                break

            print("Enter 7 digits for number, please try again")
            home_phone = input("\n\tEnter GSM phone number for player: ")

        return self.check_input(home_phone)
    

    def is_captain(self, players, player_name, captain_index):
        """Checks if player is captain, if player is captain returns [player_name, 1] 1 being the boolean value 'True'
            else returns [player_name, 0] 0 being the boolean value 'False'"""
        
        if player_name == players[int(captain_index) - 1]:
            return [player_name, 1]
        else:
            return [player_name, 0]


    def inputs_for_players(self, LLWrapper, players_list):
        '''Function that asks user for inputs for players and calls neccesary functions to create players'''
        self.LLWrapper = LLWrapper

        processing_inputs = [self.get_email, self.get_ssn, self.get_birthday, self.get_address, self.home_phone_number, self.personal_phone_number]
        player_values = []
        progress = 0
        player_index = 2
        count = 0
        count_limit = len(players_list[3:]) 
       
        while count != count_limit:
            
            while progress < len(processing_inputs):

                if progress == 0:
                    self.Terminal.printHeader("Information for player", ["Please register informations for player"])
                    print(f"\n{players_list[player_index]} is playing for team: {players_list[1]}")

                data = processing_inputs[progress]()

                if data == "b" and progress == 0:
                    pass

                elif data == "b":
                    progress -= 1
                    player_values.pop()
                else:
                    progress += 1
                    player_values.append(data)

                if progress == (len(processing_inputs)):

                    # players_list = [clubname, teamname, p1, p2, p3, p4, captain_index(p1-p4)]
                    is_captain = self.is_captain(players_list[2:-1], players_list[player_index], players_list[-1]) 
                    player_dict_values = is_captain + player_values + players_list[0:2]
                    self.LLWrapper.generateNewPlayer(player_dict_values)
                    
                    player_values = [] # [email, ssn, addr, homephone, gsm]
                    count += 1
                    player_index += 1
                    progress = 0
                    break
        
        
        
        
    
