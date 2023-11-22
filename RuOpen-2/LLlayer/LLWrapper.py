from LLlayer.LLClub import LLClub
from LLlayer.LLTournaments import LLTournament
from LLlayer.LLTournamentManager import LLTournamentManager
from LLlayer.LLTeam import LLTeam
from LLlayer.LLHost import LLHost
from LLlayer.LLGame import LLGame
from LLlayer.LLPlayer import LLPlayer

class LLWrapper:

    def __init__(self):

        self.LLTournamentManager = LLTournamentManager()
        self.LLManager = LLHost()
        self.LLTournament = LLTournament()
        self.LLClub = LLClub()
        self.LLTeam = LLTeam()
        self.LLGame = LLGame()
        self.LLPlayer = LLPlayer()

    def generateNewTournament(self, tournament_info):
        """Generates a new tournament from the information given in the tournament_info"""
        self.LLTournamentManager.generateTournamentFromInfo(tournament_info)
    

    def addNewTournamentChangedDate(self, model_object):
        """Adds a new tournament to the list of tournaments that have changed dates"""
        self.LLTournamentManager.addNewTournamentChangedDate(model_object)


    def generateNewHost(self, host_info):
        """Generates a new host from the information given in the host_info"""
        self.LLTournamentManager.generateHostFromInfo(host_info)


    def generateNewClub(self, club_info):
        """Generates a new club from the information given in the club_info"""
        self.LLTournamentManager.generateClubFromInfo(club_info)
     
     
    def generateNewTeam(self, team_info):
        """Generates a new team from the information given in the team_info"""
        self.LLTournamentManager.generateTeamFromInfo(team_info)
    

    def generateNewPlayer(self, player_info):
        """Generates a new player from the information given in the player_info"""
        self.LLTournamentManager.generatePlayerFromInfo(player_info)
    

    def createScheduleForTournament(self, ID, start_n_days, rounds):
        """Creates a schedule for the tournament with the given ID, date and number of rounds"""
        self.LLTournamentManager.createScheduleForTournament(ID, start_n_days, rounds)
    
    def gameScheduler(self, team_list, rounds):
        """Generates a schedule for the tournament with the given ID, date and number of rounds"""
        return self.LLGame.gameScheduler(team_list, rounds)


    def getAllClubs(self):
        """Returns a list of all clubs"""
        club_list = self.LLClub.getAllClubs()
        return club_list


    def removeClub(self, id):
        """Removes the club with the given ID"""
        self.LLClub.removeClub(id)


    def getAllTournaments(self):
        """Returns a list of all tournaments"""
        tournaments_list = self.LLTournament.getAllTournaments()
        return tournaments_list
    
    def getTournmanetByID(self, ID):
        """Returns a list of all tournaments with the given ID"""
        tournament_list = self.LLTournament.getTournamentByID(ID)
        return tournament_list
    

    def startTournament(self, id):
        """Starts the tournament with the given ID"""
        return self.LLTournament.startTournament(id)


    def finishTournament(self, id):
        """Finishes the tournament with the given ID"""
        return self.LLTournament.finishTournament(id)
    

    def removeTournament(self, id):
        """Removes the tournament with the given ID"""
        self.LLTournament.removeTournament(id)


    def getOngoingTournaments(self):
        """Returns a list of all ongoing tournaments"""
        return self.LLTournament.getOngoingTournaments()

    
    def getFinishedTournaments(self):
        """Returns the finished tournaments"""
        return self.LLTournament.getFinishedTournaments()


    def getFutureTournaments(self):
        """Returns the future tournaments"""
        return self.LLTournament.getFutureTournaments()
    

    def getAllTeamsFromFile(self):
        """Returns all teams from file"""
        return self.LLTeam.getAllTeams()
    

    def getTeamFromID(self, ID):
        """Returns a list of all teams with the given ID"""
        team_id_list = self.LLTeam.getTeamFromID(ID)
        return team_id_list


    def getAllPlayers(self):
        """Returns a list of all players"""
        players_list = self.LLPlayer.getAllPlayers()
        return players_list


    def getPlayersFromID(self, ID, qpsort=False):
        """Returns a list of all players with the given ID"""
        players_id_list = self.LLPlayer.getPlayersFromID(ID, qpsort)
        return players_id_list


    def storePlayersToFile(self, players_list):
        """Stores the players in the players_list to file"""
        self.LLPlayer.storePlayersToFile(players_list)

    def getAllGames(self):
        """Returns all games"""
        return self.LLGame.getAllGames()


    def getGamesFromID(self, ID):
        """Returns all games with the given ID"""
        return self.LLGame.getGamesFromID(ID)


    def getUpcomingRounds(self, ID):
        """Returns a list of all upcoming rounds for the tournament with the given ID"""
        rounds_list = self.LLTournamentManager.getUpcomingRounds(ID)
        return rounds_list


    def addNewGame(self, game_info):
        """Adds a new game to the list of games"""
        self.LLGame.addNewGame(game_info)


    def storeGamesToFile(self, games_list):
        """Stores the games in the games_list to file"""
        self.LLGame.storeGamesToFile(games_list)


    def storeTeamsToFile(self, teams_list):
        """Stores the teams in the teams_list to file"""
        self.LLTeam.storeTeamsToFile(teams_list)
    

    def startTournament(self, id):
        """Starts the tournament with the given ID"""
        return self.LLTournament.startTournament(id)


    def finishTournament(self, id):
        """Finishes the tournament with the given ID"""
        return self.LLTournament.finishTournament(id)


    def getRankedTeams(self, ID):
        """Returns a list of all ranked teams for the tournament with the given ID"""
        return self.LLTeam.getRankedTeams(ID)


    def logPlayerPoints(self, ID, qp_from_dict, home_players, away_players):
        """Logs the points for the players in the game with the given ID"""
        self.LLPlayer.logPlayerPoints(ID, qp_from_dict, home_players, away_players)


    def registerWinsnLoss(self, id, scores, home_team, away_team):
        """Registers the wins and losses for the teams in the game with the given ID"""
        self.LLTeam.registerWinsnLoss(id, scores, home_team, away_team)
        self.startTournament(id)
    