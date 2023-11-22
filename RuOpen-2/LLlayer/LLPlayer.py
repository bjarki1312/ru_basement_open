from IOLayer.IOWrapper import IOWrapper
from ModelClasses.ModelPlayer import ModelPlayer

class LLPlayer:

    def __init__(self):
        """Constructor for LLPlayer"""
        self.IOWrapper = IOWrapper()
        
    def addNewPlayer(self, new_player):
        """Takes in a dict of a player, maps it to a Player object and appends to the file"""
        
        players_list = self.getAllPlayers()
        player = ModelPlayer(new_player["id"], new_player["player_name"], new_player["isCaptain"], new_player["email"], new_player["ssn"], new_player["birthday"], new_player["address"], new_player["home_num"], new_player["cell_num"], new_player["club_name"], new_player["team_name"], new_player["score"], new_player["qp"])
        players_list.append(player)
        self.IOWrapper.StorePlayersToFile(players_list)


    def storePlayersToFile(self, players_list):
        """Takes in a list of players and stores them to the file"""
        self.IOWrapper.StorePlayersToFile(players_list)


    def removePlayer(self, id):
        """Removes all  with matching id"""
        
        players_list = self.getAllPlayers()
        new_players_list = [i for i in players_list if i.id != id]
        self.IOWrapper.StorePlayersToFile(new_players_list)
        
        if len(new_players_list) != players_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."

    
    def getAllPlayers(self):
        """Returns list of all teams"""
        
        teams_list = self.IOWrapper.LoadPlayersFromFile()
        return teams_list
    
    
    def getPlayersFromID(self, ID, qpsort=False):
        """Returns list of all players with matching ID"""
        players_id_list = []
        players_list = self.getAllPlayers()

        for player in players_list:
            if player.id == ID:
                players_id_list.append(player)
        if qpsort == True:
            players_id_list.sort(key=lambda x: x.qp, reverse=True)
        
        return players_id_list

    def logPlayerPoints(self, id, qp_list, home_players, away_players):
        
        """Takes in a list of qp's and adds them to the player"""
        
        players_list = self.getAllPlayers()
        for playeritem in players_list:
            
            if playeritem.id == id:
                
                for player in qp_list:
                    
                    if player.lower() in home_players or player.lower() in away_players:
                        
                        if playeritem.name.lower() == player.lower():
                            playeritem.score = qp_list[player]
                            playeritem.qp = self.convertScoreToQp(qp_list[player])

        self.storePlayersToFile(players_list)

    def convertScoreToQp(self, score_list):
        """Takes in a list of scores, calculates the inputs to the right format and
        returns the quality points score"""
        qp_score = 0 
        # examples of qp points[112, 150N, 150U, 8H]
        for item in score_list:

            if "N" in item.upper() or "U" in item.upper():
                qp_score += 1
                item = item[:-1]
            
            if item.isdigit() == True:

                if int(item) > 93:
                    qp_score += 1

                if int(item) > 119:

                    qp_score += 1

                if int(item) > 169:
                    qp_score += 1

            if "H" in item.upper():

                if item[:-1].isdigit() == True:

                    if int(item[:-1]) > 4:
                        qp_score += 1
                    
                    if int(item[:-1]) > 6:
                        qp_score += 1

                    if int(item[:-1]) >= 9:
                        qp_score += 1
            
                if "HB" in item.upper(): #Bullseye
                    qp_score += 1
            
                if "HB1": #Bullseye og ein telur tvöfalt:
                    qp_score += 1
                
                if "HB3": # Bullseye allt telur tvöfalt:
                    qp_score += 1
        
        return qp_score
            

             