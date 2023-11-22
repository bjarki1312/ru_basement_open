from LLlayer.LLWrapper import LLWrapper
from UILayer.UIClearTerminal import UIClearTerminal
from ModelClasses.ModelGame import ModelGame
import time
from datetime import datetime


class UISchedule:

    def __init__(self):

        self.LLWrapper = LLWrapper()
        self.Terminal = UIClearTerminal()


    def display_upcoming_rounds(self, ID):
        
        self.Terminal.clear()
        tournament_name = self.LLWrapper.getAllTournaments()[0].name
        schedule_list = self.LLWrapper.getUpcomingRounds(ID) # scheduler_list = [round, date, home_team, away_team]
        self.Terminal.printHeader("Upcoming rounds for league", ['League: ' +tournament_name])
        n_round = 0
        n_game = 1

        while n_round < len(schedule_list):


            if schedule_list[n_round][0] != schedule_list[n_round - 1][0]:
                self.game_count = n_game - 1
                n_game = 1
            
            if schedule_list[n_round][0] == schedule_list[n_round - 1][0]:
                print(f"\t{n_game}. {schedule_list[n_round][2]} vs {schedule_list[n_round][3]}")
                n_game += 1
            else:
                print(f"\n\tRound: {schedule_list[n_round][0]} - {schedule_list[n_round][1]}\n\t{n_game}. {schedule_list[n_round][2]} vs {schedule_list[n_round][3]}")
                n_game += 1
                
                if schedule_list[n_round][0] == "Postponed match":
                    pass
                else:
                    self.round_count = schedule_list[n_round][0]
            
            n_round += 1


    def first_option(self, ID):
        
        self.display_upcoming_rounds(ID)
        
        user_input = input(("\nPlease enter [Y/y] for yes to change date of a match or [B/b] to go back: ")).lower()
        while user_input != "y":
            
            if user_input.lower() == "b":
                return "b"

            print("\t\tPlease enter either [Y/y] or [B/b]")
            time.sleep(1.2)

            user_input = self.first_option(ID)
            break

        if user_input == "b":
            return "b"

        return user_input
    

    def change_schedule(self, ID):
        '''User can change date of a match'''
        self.Terminal.clear()
        self.display_upcoming_rounds(ID)
        
        user_input = input("\nSelect number of round which you want to change date of a match or enter [B/b] to go back: ")
        while user_input.isdigit() == False or int(user_input) < 1 or int(user_input) > self.round_count:
            
            if user_input.lower() == "b":
                return "b"
            
            print("\tPlease enter valid number of round or [B/b]")
            time.sleep(1.2)
            
            user_input = self.change_schedule(ID)
            if user_input == "b":
                return "b"
            else:
                break

        user_input_two = input("Select nr. of game to postpone schedule or enter [B/b] to go back: ")
        while user_input_two.isdigit() == False or int(user_input_two) < 1 or int(user_input_two) > self.game_count:
            
            if user_input_two.lower() == "b":
                return self.change_schedule(ID)
            
            print("\t\tPlease enter valid number of round or [B/b]")
            time.sleep(1.2)

            user_input_two = self.change_schedule(ID)
            if user_input_two == "b":
                return self.change_schedule(ID)
            else:
                break
        

        games_list = self.LLWrapper.getAllGames()
        right_index = ((int(self.game_count)*7)*(int(user_input) - 1) + ((int(user_input_two) - 1)*7))

        date_changed = input("Enter date to postpone match (ex. dd-mm-yyyy): ")
        checked_date = self.Terminal.check_date(date_changed.replace("-", " "))
        while checked_date == datetime.min or datetime.strptime(games_list[right_index].date, "%d-%m-%Y") >= checked_date:

            print("Incorrect date")
            date_changed = input("\nEnter date to postpone match (ex. dd-mm-yyyy): ")
            checked_date = self.Terminal.check_date(date_changed)
        
        counter = 0
        for _ in range(7):
            
            games_list[right_index + counter].date = datetime.strftime(checked_date,"%d-%m-%Y")
            temp_model = games_list[right_index + counter]
            games_list[right_index + counter] = ModelGame(ID, datetime.strftime(checked_date,"%d-%m-%Y"), round_nr = temp_model.round_nr)
            temp_model.round_nr = "Postponed match"
            games_list.append(temp_model)
            
            counter += 1
        
      
        
        # Checking weather the date_changed goes surpasses end_date
        model_tournament = self.LLWrapper.getTournmanetByID(ID)
        end_date = datetime.strptime(model_tournament[0].end_date.replace("/","-"), "%d-%m-%Y")
        
        if checked_date > end_date:
            
            end_date = checked_date
            model_tournament[0].end_date = end_date.strftime("%d-%m-%Y") # fer eftir hvaða formatið er í modelinu
            self.LLWrapper.addNewTournamentChangedDate(model_tournament[0])
              
        self.LLWrapper.storeGamesToFile(games_list)
        
    
    def input_for_schedule(self, ID):
        '''Main function for changing schedule'''
        progress_inputs = [self.first_option, self.change_schedule]
        progress = 0

        while progress < len(progress_inputs):

            data = progress_inputs[progress](ID)

            if progress == 1:
                progress -= 1

            elif progress == 0 and data != "b":
                progress += 1

            elif progress == 0 and data == "b":
                break

            elif data == "b":
                progress -= 1 
                
            

        