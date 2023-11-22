from IOLayer.IOClubs import IOClubs
from IOLayer.IOTournaments import IOTournaments
from IOLayer.IOHosts import IOHosts
from IOLayer.IOTeams import IOTeams
from IOLayer.IOPlayers import IOPlayers
from IOLayer.IOGames import IOGames


class IOWrapper:

    
    def __init__(self):
        """Wrapper class for all IO classes, to be used in the Controller layer."""
        
        self.Tournaments = IOTournaments()
        self.Clubs = IOClubs()
        self.Teams = IOTeams()
        self.Hosts = IOHosts()
        self.Players = IOPlayers()
        self.Games = IOGames()


    def LoadTournamentsFromFile(self):
        """Loads all tournaments from file, and returns a list of ModelTournament objects"""

        data = self.Tournaments.LoadTournamentsFromFile()
        return data


    def StoreTournamentToFile(self, tournaments_info):
        """Stores the Tournaments to a file, tournaments_info is a list of ModelTournament objects"""

        self.Tournaments.StoreTournamentToFile(tournaments_info)


    def LoadClubsFromFile(self):
        """Loads all clubs from file, and returns a list of ModelClub objects"""

        data = self.Clubs.LoadClubsFromFile()
        return data


    def StoreClubToFile(self, club_info):
        """Stores the clubs to a file, club_info is a list of ModelClub objects"""

        self.Clubs.StoreClubToFile(club_info)


    def LoadTeamsFromFile(self):
        """Loads all teams from file, and returns a list of ModelTeam objects"""

        data = self.Teams.LoadTeamsFromFile()
        return data
            

    def StoreTeamToFile(self, team_info):
        """Stores the teams to a file, team_info is a list of ModelTeam objects"""

        self.Teams.StoreTeamToFile(team_info)


    def LoadPlayersFromFile(self):
        """Loads all players from file, and returns a list of ModelPlayer objects"""

        data = self.Players.LoadPlayersFromFile()
        return data


    def StorePlayersToFile(self, player_info):
        """Stores the players to a file, player_info is a list of ModelPlayer objects"""

        self.Players.StorePlayersToFile(player_info)


    def LoadHostsFromFile(self):
        """Loads all hosts from file, and returns a list of ModelHost objects and returns a list of ModelHost objects"""

        data = self.Hosts.LoadHostsFromFile()
        return data

    def StoreHostsToFile(self, host_info):
        """Stores the hosts to a file, host_info is a list of ModelHost objects"""

        self.Hosts.StoreHostsToFile(host_info)
    

    def LoadGamesFromFile(self):
        """Loads all games from file, and returns a list of ModelGame objects"""

        data = self.Games.LoadGamesFromFile()
        return data


    def StoreGamesToFile(self, game_info):
        """Stores the games to a file, game_info is a list of ModelGame objects"""

        self.Games.StoreGamesToFile(game_info)

       



    
