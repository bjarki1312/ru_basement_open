class ModelTeam:

    def __init__(self, team_id=None, club_name=None, team_name=None, home_or_away=None, captain=None, players=None, count=None, wins=0, loss=0):
        
        self.id = team_id
        self.club_name = club_name
        self.team_name = team_name
        self.home_or_away = home_or_away
        self.captain = captain
        self.players = players
        self.count  = count
        self.wins = wins
        self.loss = loss


    def __str__(self) -> str:
        """Returns all attributes seperated by a comma"""
        
        return f"{self.id} {self.club_name} {self.team_name} {self.home_or_away} {self.captain} {self.players} {self.count} {self.wins} {self.loss}"
