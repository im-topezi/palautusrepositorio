class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality=dict["nationality"]
        self.assists=dict["assists"]
        self.goals=dict["goals"]
        self.team=dict["team"]
        self.games=dict["games"]
        
    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name: <20}{self.team:^10}{self.goals:^3}+{self.assists:^4}+{self.points:>3}"
