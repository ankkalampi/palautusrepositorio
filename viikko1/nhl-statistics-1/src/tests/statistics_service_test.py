import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12), #16
            Player("Lemieux", "PIT", 45, 54), #99
            Player("Kurri",   "EDM", 37, 53), #90
            Player("Yzerman", "DET", 42, 56),#98
            Player("Gretzky", "EDM", 35, 89) #124
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):

        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_has_players(self):
        def has_players(self):
            if self.stats._players == None:
                return False
            return True
        
        self.assertEqual(has_players(self), True)

        

    def test_player_returned_if_exists(self):
        player = Player("Kurri",   "EDM", 37, 53)
        searched_player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, searched_player.name)
        self.assertAlmostEqual(player.team, searched_player.team)
        self.assertAlmostEqual(player.goals, searched_player.goals)
        self.assertAlmostEqual(player.assists, searched_player.assists)

    def test_none_returned_if_not_player_exists(self):      
        player = "player"
        

        searched_player = self.stats.search("player")

        self.assertAlmostEqual(None, searched_player)

    def test_correct_players_in_team(self):
        players_of_team = self.stats.team("EDM")

        

        sem = self.stats.search("Semenko")
        kur = self.stats.search("Kurri")
        gre = self.stats.search("Gretzky")

        team = list((sem, kur, gre))

        
        self.assertEqual(players_of_team, team)

    def test_sort_by_points_returns_player_points(self):
        player = self.stats.search("Kurri")
        self.assertEqual(player.points, 90)


    def test_result_is_correct(self):
        tested_result = list(self.stats.top(4))
        result = []
        result.append(Player("Semenko", "EDM", 4, 12))
        result.append(Player("Kurri",   "EDM", 37, 53))
        result.append(Player("Yzerman", "DET", 42, 56))
        result.append(Player("Lemieux", "PIT", 45, 54))
        result.append(Player("Gretzky", "EDM", 35, 89))

        result2 = list(result)

        

        self.assertEqual(result2[2].name, tested_result[2].name)

    