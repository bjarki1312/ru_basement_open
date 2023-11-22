from os import system, name
from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
from UILayer.UICreatePlayer import UICreatePlayer
import time


class UICreateTeam:

    def __init__(self):

        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()
        self.UICreatePlayer = UICreatePlayer()
        

    def check_input(self, data):
        """Checks if input is 'b' or not, if 'b' returns 'b' else returns data"""
        
        if data.lower() == "b":
            return "b"
        else:
            return data
    

    def name_of_team(self):
        """Asks user for name of team and returns it, if 'b' is entered returns 'b'"""
        
        print("\nName of your team?")
        team_name = input("\n\tEnter name of your team: ")
        return self.check_input(team_name)
    

    def write_members(self):
        """Asks user for amount of players in the team, minimum of 4 players,
            then asks for name of each player and returns a list of players"""
        
        member_count = input("\nHow many members are in your team? (minimum 4): ")
        members_list = []
        
        while member_count.isdigit() == False or int(member_count) < 4:

            if member_count.lower() == "b":
                return self.check_input(member_count)

            print("Enter a valid number for member count in your team")
            member_count = input("\nHow many members are in your team? (minimum 4): ")
            
        print("\nPlayer nr: \n")
        for i in range(int(member_count)):

            if i < 9:
                member = input(f" {i+1}. Enter name: ")
            else:
                member = input(f"{i+1}. Enter name: ")
            
            members_list.append(member)
        
        return members_list


    def choose_captain(self, team_members):
        """User chooses a player to be team captain, the function has two checks,
        first checks if input is valid, then checks if the player number is valid,
        then returns the player number, if 'b' is entered the function returns 'b'"""
        
        print("\nWho should be the team captain of your team?")
        team_captain = input("\n\tSelect number of player for team captain: ")
        valid_input_range = len(team_members)

        # Check First If input is valid
        while team_captain.isdigit() == False and team_captain.lower() != "b":

            print("Please select a valid number of player to be team captain")
            team_captain = input("\n\tSelect number of player for team captain: ")

        # Next check if valid nr. of player was choosen for captain        
        while int(team_captain) > valid_input_range or int(team_captain) < 1:

            print(f"No player has nr.{int(team_captain)}, please select valid nr.")
            team_captain = input("\n\tSelect number of player for team captain: ")

        return self.check_input(team_captain)


    def inputs_for_team(self, LLWrapper, club_name):
        """Works through the inputs for team, first asks for name of team, then for amount of players,
            then asks for name of each player, then asks for team captain, then returns a list of all inputs,
            if 'b' at any given point in the function, it removes the last value in the list and returns to the previous input.
            In the end it asks the user if they want to create another team, if yes it starts over, if no it returns to
            the previous menu and returns a list to the LLWrapper"""
        
        self.LLWrapper = LLWrapper
        processing_inputs = [self.name_of_team, self.write_members, self.choose_captain]
        team_values = [club_name]
        progress = 0
        team_count = 0


        while progress < len(processing_inputs):
            
            if progress == 0:
                print(f"\n\nTeam count for {club_name}: {team_count}")
                self.Terminal.printHeader("Form a team", ["Please register team/s for your club"])

            if progress == 2:
                data = processing_inputs[progress](team_values[2:])

            else:
                data = processing_inputs[progress]()

            if data == "b" and progress == 0:
                pass

            elif data == "b":
                progress -= 1
                team_values.pop()
                
            elif progress == 1:
                progress += 1
                team_values.extend(data)
            
            else:
                progress += 1
                team_values.append(data)

            if progress == (len(processing_inputs)):
                
                team_count += 1
                print(f"\nTeam Captain choosen: {team_values[int(team_values[-1]) + 1]}")
                time.sleep(1.2)
                self.LLWrapper.generateNewTeam(team_values)
                print("\nPlease register personal information for each member")
                self.UICreatePlayer.inputs_for_players(self.LLWrapper, team_values)

                while True:                    
                    
                    ask_again = input(f"\nWould you like to add another Team to Club: {club_name} [Y/y]/[N/n]?: ").lower()
                    
                    if ask_again == 'y':
                        progress = 0
                        team_values = [club_name]
                        break
                    
                    elif ask_again == 'n':
                        return team_count
                    
                    else:
                        print("\nPlease Enter either [Y/y] for yes or [N/n] for no")


