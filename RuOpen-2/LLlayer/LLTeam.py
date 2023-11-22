from IOLayer.IOWrapper import IOWrapper
from ModelClasses.ModelTeam import ModelTeam

class LLTeam:

    def __init__(self):
        """Constructor for LLTeam"""

        self.IOWrapper = IOWrapper()


    def addNewTeam(self, new_team):
        """Takes in a dict of a team, maps it to a Team object and appends to the file"""
        
        teams_list = self.getAllTeams()
        teams = ModelTeam(new_team["id"], new_team["club_name"], new_team["team_name"], new_team["home_or_away"], new_team["Captain"], new_team["Players"], new_team["Count"]) # leaving wins and loss empty to initialize as 0
        teams_list.append(teams)
        self.IOWrapper.StoreTeamToFile(teams_list)

    def removeTeam(self, id):
        """Removes all teams with matching id"""
        
        teams_list = self.getAllTeams()
        new_teams_list = [i for i in teams_list if i.id != id]
        self.IOWrapper.StoreTeamToFile(new_teams_list)
        
        if len(new_teams_list) != teams_list:
            return "Succesfully removed!"
        else:
            return "No ID matching..."
    
    def getAllTeams(self):
        """Returns list of all teams"""
        
        teams_list = self.IOWrapper.LoadTeamsFromFile()
        return teams_list

    def getTeamFromID(self, ID):
        """Returns a list of all teams with matching ID"""
        team_id_list = []        
        teams_list = self.getAllTeams()

        for team in teams_list:

            if team.id == ID:
                team_id_list.append(team)
        
        return team_id_list

    def storeTeamsToFile(self, teams_list):
        """Stores a list of teams to file"""

        self.IOWrapper.StoreTeamToFile(teams_list)

    def getRankedTeams(self, id):
        """Returns a list of teams sorted by wins"""
        teams_list = self.getAllTeams()
        teams_list = sorted(teams_list, key=lambda x: x.wins-x.loss, reverse=True)
        return teams_list
 
 
    def registerWinsnLoss(self, id, scores, home_team, away_team):
        '''
        scores is a list
        '''  
        all_teams_list = self.getAllTeams()
        for team in all_teams_list:
            if team.id == id:
                if home_team == team.team_name: # currently home team
                    if scores[0] > scores[1]: # home team won
                        team.wins += 1
                    else:
                        team.loss += 1
                elif away_team == team.team_name: # currently away team
                    if scores[1] > scores[0]: # away team won
                        team.wins += 1
                    else:
                        team.loss += 1
        self.storeTeamsToFile(all_teams_list)
        