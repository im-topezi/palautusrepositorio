import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_found(self):
        self.assertEqual((self.stats.search("Semenko")).name,"Semenko")

    def test_search_not_found(self):
        self.assertEqual(self.stats.search("Jaska Jokunen"),None)

    def test_players_of_team(self):
        self.assertEqual(((self.stats.team("DET"))[0]).name,"Yzerman")

    def test_top_players_no_parameter(self):
        self.assertEqual(((self.stats.top(1))[0]).name,"Gretzky")

    def test_top_players_points(self):
        self.assertEqual(((self.stats.top(1,SortBy.POINTS))[0]).name,"Gretzky")

    def test_top_players_goals(self):
        self.assertEqual(((self.stats.top(1,SortBy.GOALS))[0]).name,"Lemieux")

    def test_top_players_assists(self):
        self.assertEqual(((self.stats.top(1,SortBy.ASSISTS))[0]).name,"Gretzky")
