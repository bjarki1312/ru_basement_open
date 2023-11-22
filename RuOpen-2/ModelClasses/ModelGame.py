class ModelGame:
    
    def __init__(self, id=None, date=None, round_nr=None, game_type=None, home_team=None, away_team=None, home_player=None, away_player=None, home_leg=None, away_leg=None) -> None:
        
        self.id = id
        self.date = date
        self.round_nr = round_nr
        self.game_type = game_type
        self.home_team = home_team
        self.away_team = away_team
        self.home_player = home_player
        self.away_player = away_player
        self.home_leg = home_leg
        self.away_leg = away_leg

    def __str__(self) -> str:
        """Returns all attributes seperated by a comma"""
        
        return f"{self.id}, {self.date}, {self.game_type}, {self.home_team}, {self.away_team}, {self.home_player}, {self.away_player}, {self.home_leg}, {self.away_leg}"