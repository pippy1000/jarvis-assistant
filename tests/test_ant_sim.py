import unittest

from jarvis_assistant.ant_sim import ColonyGame


class AntSimTests(unittest.TestCase):
    def test_game_starts_with_basic_colony(self):
        game = ColonyGame()
        self.assertEqual(game.food, 10)
        self.assertEqual(game.workers, 2)
        self.assertEqual(game.soldiers, 1)
        self.assertEqual(game.nest_level, 1)

    def test_tick_increases_food(self):
        game = ColonyGame(food=10, workers=2)
        game.tick()
        self.assertGreater(game.food, 10)

    def test_hire_worker_costs_food(self):
        game = ColonyGame(food=40, workers=2)
        before = game.food
        game.hire_worker()
        self.assertLess(game.food, before)
        self.assertEqual(game.workers, 3)

    def test_upgrade_nest_increases_level(self):
        game = ColonyGame(food=100)
        game.upgrade_nest()
        self.assertGreater(game.nest_level, 1)


if __name__ == "__main__":
    unittest.main()
