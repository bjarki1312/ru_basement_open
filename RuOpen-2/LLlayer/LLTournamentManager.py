from IOLayer.IOWrapper import IOWrapper
from LLlayer.LLTournaments import LLTournament
from LLlayer.LLClub import LLClub
from LLlayer.LLPlayer import LLPlayer
from LLlayer.LLTeam import LLTeam
from LLlayer.LLHost import LLHost
from LLlayer.LLGame import LLGame
from random import randint

class LLTournamentManager:

    def __init__(self):
        """Constructor for LLTournamentManager"""
        
        self.IOWrapper = IOWrapper()
        self.LLTournament = LLTournament()
        self.LLClub = LLClub()
        self.LLPlayer = LLPlayer()
        self.LLTeam = LLTeam()
        self.LLHost = LLHost()
        self.LLGame = LLGame()
        self.current_id = randint(1000, 2000)
        self.counter = 0

    

    def generateTournamentFromInfo(self, tournament_info: list):
        """Generates a tournament from a list of info"""

        tournament_dict = {"id": 0, "name": tournament_info[0], "status": "not started", "start_date": tournament_info[3], \
                            "end_date": tournament_info[4], "host_name": tournament_info[1], "rounds": tournament_info[6]}
        
        # generate random id for all

        tournament_dict["id"] = self.current_id
        self.LLTournament.addNewTournament(tournament_dict)


    def addNewTournamentChangedDate(self, mode_object):
        self.LLTournament.addNewTournamentChangedDate(mode_object)


    def generateHostFromInfo(self, host_info: list):
        """Generates a host from a list of info"""

        host_dict = {"id": 0, "name": host_info[0], "phone_number": host_info[1]}
        host_dict["id"] = self.current_id
        self.LLHost.addNewHost(host_dict)
    

    def generateClubFromInfo(self, club_info: list):
        """Generates a club from a list of info and adds it to the file"""

        club_dict = {"id": 0, "name": club_info[0], "address": club_info[1], "phone_number": club_info[2]}
        club_dict["id"] = self.current_id
        self.LLClub.addNewClub(club_dict)


    def generateTeamFromInfo(self, team_info: list):
        
        team_dict = {"id": 0, "club_name": team_info[0], "team_name": team_info[1], "home_or_away": None,\
                    "Captain": team_info[int(team_info[-1]) + 1], "Players": team_info[2:-1],"Count": len(team_info[2:-1])}
        team_dict["id"] = self.current_id
        self.LLTeam.addNewTeam(team_dict)


    def generatePlayerFromInfo(self, player_info: list):

        player_dict = {"id": 0, "player_name": player_info[0], "isCaptain": player_info[1], "email":player_info[2], "ssn": player_info[3], "birthday": player_info[4],\
                       "address":player_info[5], "home_num": player_info[6], "cell_num": player_info[7], "club_name": player_info[8], "team_name":player_info[9], "score": [], "qp": 0} 
        player_dict["id"] = self.current_id
        self.LLPlayer.addNewPlayer(player_dict)

    def createScheduleForTournament(self, ID, start_n_days, rounds):
        
        team_list = self.LLTeam.getTeamFromID(ID)
        self.LLGame.generateGames(self.current_id, team_list, start_n_days, rounds)
    
    def getUpcomingRounds(self, ID):

        games_list = self.LLGame.getUpcomingRounds(ID)
        return games_list
        
    
   
    