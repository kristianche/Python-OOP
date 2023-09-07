from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Kris", 20, 16.0)

    def test_init(self):
        self.assertEqual("Kris", self.tennis_player.name)
        self.assertEqual(20, self.tennis_player.age)
        self.assertEqual(16.0, self.tennis_player.points)
        self.assertEqual([], self.tennis_player.wins)

    def test_name_valid(self):
        self.tennis_player.name = "Georgi"
        self.assertEqual("Georgi", self.tennis_player.name)

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = "bb"
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))
        self.assertEqual("Kris", self.tennis_player.name)

    def test_age_invalid(self):
        self.tennis_player.age = 21
        self.assertEqual(21, self.tennis_player.age)

    def test_age_valid(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))
        self.assertEqual(20, self.tennis_player.age)

    def test_add_win_successfully(self):
        self.tennis_player.wins = ["USA Open"]
        self.tennis_player.add_new_win("Australia Open")
        self.assertEqual(["USA Open", "Australia Open"], self.tennis_player.wins)

    def test_add_win_unsuccessfully(self):
        self.tennis_player.wins = ["USA Open"]
        result = self.tennis_player.add_new_win("USA Open")
        self.assertEqual(["USA Open"], self.tennis_player.wins)
        self.assertEqual(result, "USA Open has been already added to the list of wins!")

    def test_lt_correct(self):
        other_tennis_player = TennisPlayer("Grisho", 34, 15)
        result = self.tennis_player < other_tennis_player
        self.assertEqual(result, 'Kris is a better player than Grisho')

    def test_lt_incorrect(self):
        other_tennis_player = TennisPlayer("Grisho", 34, 40)
        result = self.tennis_player < other_tennis_player
        self.assertEqual(result, 'Grisho is a top seeded player and he/she is better than Kris')

    def test_str(self):
        self.tennis_player.add_new_win("USA")
        self.tennis_player.add_new_win("Australia")

        result = f"Tennis Player: Kris\n" \
                 f"Age: 20\n" \
                 f"Points: 16.0\n" \
                 f"Tournaments won: USA, Australia"
        self.assertEqual(str(self.tennis_player), result)


if __name__ == "__main__":
    main()