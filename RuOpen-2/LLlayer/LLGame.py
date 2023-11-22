from IOLayer.IOWrapper import IOWrapper
from ModelClasses.ModelGame import ModelGame
from datetime import datetime, timedelta

class LLGame:

    def __init__(self):
        """Constructor for LLGame, that initializes the IOWrapper"""

        self.IOWrapper = IOWrapper()

    
    def gameScheduler(self, team_list, rounds):
        '''Generates a schedule for a league with the given team list and number of rounds'''
        schedule_list = []

        if len(team_list) % 2 == 1:

            team_list += ["has no opponent"]

        for i in range((len(team_list) - 1)*int(rounds)):

            middle = int(len(team_list) / 2)
            list_1 = team_list[: middle]
            list_2 = team_list[middle :]
            list_2.reverse()
        
            if (i % 2 == 1):

                schedule_list += [zip(list_1, list_2)]
            else:
                schedule_list += [zip(list_2, list_1)]
        
            team_list.insert(1, team_list.pop())
        
        return schedule_list
    
    
    def generateGames(self, ID, team_list, start_n_days, rounds):
        """Generates games for a tournament"""
        
        scheduler_list = self.gameScheduler(team_list, int(rounds))
        start_n_end_date = [(start_n_days[0] + timedelta(days = i)).strftime('%d-%m-%Y') for i in range(0, start_n_days[1])]
        start_n_end_date_index = -1
        round_count = 0      
        game_types = ["501", "301", "C"]

        # if days are longer than round count for tournament
        if len(start_n_end_date) > len(scheduler_list):
                    
                    range_finder = len(start_n_end_date) - len(scheduler_list)
                    temp = [start_n_end_date[0]]
                    temp += start_n_end_date[range_finder + 1:]
                    start_n_end_date = temp

        
        for round in scheduler_list:
            try:
                start_n_end_date_index += 1
                date = start_n_end_date[start_n_end_date_index]
                round_count += 1
            
            except IndexError:
                round_count += 1

            for match in round:
                try:
                 
                    
                    for _ in range(4):

                        team_dict = {"id": ID, "date": date, "round_nr": round_count, "game_type": game_types[0], "home_team": match[0].team_name,\
                                    "away_team": match[1].team_name, "home_player": [], "away_player": [], "home_leg": [], "away_leg": []}
                        
                        self.addNewGame(team_dict)

                    for _ in range(1):

                        team_dict = {"id": ID, "date": date, "round_nr": round_count, "game_type": game_types[1], "home_team": match[0].team_name,\
                                    "away_team": match[1].team_name, "home_player": [], "away_player": [], "home_leg": [], "away_leg": []}
                        
                        self.addNewGame(team_dict)
                    
                    for _ in range(1):

                        team_dict = {"id": ID, "date": date, "round_nr": round_count, "game_type": game_types[2], "home_team": match[0].team_name,\
                                    "away_team": match[1].team_name, "home_player": [], "away_player": [], "home_leg": [], "away_leg": []}
                        
                        self.addNewGame(team_dict)

                    for _ in range(1):
                        
                        team_dict = {"id": ID, "date": date, "round_nr": round_count, "game_type": game_types[0], "home_team": match[0].team_name,\
                                    "away_team": match[1].team_name, "home_player": [], "away_player": [], "home_leg": [], "away_leg": []}
                        
                        self.addNewGame(team_dict)

                except AttributeError:
                    pass

    def getUpcomingRounds(self, ID):
        """Returns a list of upcoming rounds for a tournament"""
        round_list = []
        game_list = self.getGamesFromID(ID)

        for i in range(0,len(game_list)-1, 7): # Þarf confirmation hversu margar umferðir mótið á að vera.          
                round_list.append([game_list[i].round_nr, game_list[i].date, game_list[i].home_team, game_list[i].away_team])
        
        return round_list
       
            
    def addNewGame(self, new_game):
        """Takes in a dict of a game, maps it to a Game object and appends to the file"""

        games_list = self.getAllGames()
        game = ModelGame(new_game["id"], new_game["date"], new_game["round_nr"], new_game["game_type"], new_game["home_team"], new_game["away_team"], new_game["home_player"], new_game["away_player"], new_game["home_leg"], new_game["away_leg"])
        games_list.append(game)
        self.IOWrapper.StoreGamesToFile(games_list)


    def storeGamesToFile(self, new_games_list):
        """
        Stores a list of games to file

        Args:
            games_list (ModelGame list): list of all games to add to file
        """        
        
        self.IOWrapper.StoreGamesToFile(new_games_list)
        

    def removeGame(self, id):
        """Removes all with matching id"""
        
        games_list = self.getAllGames()
        new_games_list = [i for i in games_list if i.id != id]
        self.IOWrapper.StoreGamesToFile(new_games_list)
        
        if len(new_games_list) != games_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."
     
    
    def getAllGames(self):
        """Gets all games from file, and returns a list of games, uses loadGamesFromFile from IOWrapper"""

        data = self.IOWrapper.LoadGamesFromFile()
        return data
    

    def getGamesFromID(self, ID):
        '''Gets all games with a given id, sorted by date and match. Returns a list of games'''
        game_list_with_same_ID = []
        games = self.getAllGames()
        for game in games:

            if game.id == ID:
                game_list_with_same_ID.append(game)
            else:
                pass

        game_list_with_same_ID.sort(key=lambda x: datetime.strptime(x.date, '%d-%m-%Y')) 
        # sorts by date by converting to datetime object 

        game_list_with_same_ID.sort(key=lambda x: (999 if x.round_nr == "Postponed match" else x.round_nr)) 

        return game_list_with_same_ID
        
        
    
    
    
    