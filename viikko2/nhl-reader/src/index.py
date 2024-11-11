import requests
from rich.text import Text
from player import Player
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

class PlayerReader:
    def __init__(self,url):
        self.url=url
        self.players=[]

    def get_players(self):
        response = requests.get(self.url).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        self.players=players

class PlayerStats:
    def __init__(self,reader):
        self.reader=reader


    def list_players(self,nation):
        def points(player):
            return player.points
        nations_players=[]
        self.reader.players.sort(key=points,reverse=True)
        for player in self.reader.players:
            if player.nationality==nation:
                nations_players.append(player)
        return nations_players
    
    def list_nationalities(self):
        nationalities=set()
        for player in self.reader.players:
            nationalities.add(player.nationality)
        return nationalities
    



def main():
    console = Console()
    text = Text("NHL statistics by nationality")
    text.stylize("italic")
    console.print(text)
    when = Prompt.ask("Select season", choices=["2018-19", "2019-20", "2020-21","2021-22","2022-23","2023-24","2024-25"])
    url = f"https://studies.cs.helsinki.fi/nhlstats/{when}/players"
    reader = PlayerReader(url)
    reader.get_players()
    stats = PlayerStats(reader)
    nations=stats.list_nationalities()
    string_of_nations=[]
    for nation in nations:
        string_of_nations.append(nation)
    while True:
        user_nation=Prompt.ask("Select nationality",choices=string_of_nations)
        players = stats.list_players(user_nation)
        table=Table(title=f"Top scores of {user_nation}")
        table.add_column("Player name",style="cyan",no_wrap=True)
        table.add_column("team",style="magenta",no_wrap=True)
        table.add_column("goals",style="green",justify="right",no_wrap=True)
        table.add_column("assists",style="green",justify="right",no_wrap=True)
        table.add_column("points",style="green",justify="right",no_wrap=True)
        for player in players:
            table.add_row(player.name,player.team,str(player.goals),str(player.assists),str(player.points))
        console.print(table)


if __name__ == "__main__":
    main()
