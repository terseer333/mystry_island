
import unittest

from game import (
    new_game,
    move_player,
    collect_item,
    available_actions,
    light_beacon,
    is_win
)


class MysteryIslandTests(unittest.TestCase):

    # ======================================
    # TEST 1: NEW GAME
    # ======================================

    def test_new_game_starts_correctly(self):

        player = new_game("Jimmy")

        self.assertEqual(player["name"], "Jimmy")
        self.assertEqual(player["location"], "beach")
        self.assertEqual(player["energy"], 5)
        self.assertEqual(player["inventory"], [])
        self.assertFalse(player["game_over"])
        self.assertFalse(player["won"])

    # ======================================
    # TEST 2: INVALID COMMAND
    # ======================================

    def test_invalid_destination_changes_nothing(self):

        player = new_game("Jimmy")

        result = move_player(player, "airplane")

        self.assertEqual(result, "invalid")
        self.assertEqual(player["location"], "beach")
        self.assertEqual(player["energy"], 5)

    # ======================================
    # TEST 3: SUCCESSFUL MOVEMENT
    # ======================================

    def test_legal_movement_reduces_energy_once(self):

        player = new_game("Jimmy")

        result = move_player(player, "jungle")

        self.assertEqual(result, "moved")
        self.assertEqual(player["location"], "jungle")
        self.assertEqual(player["energy"], 4)

    # ======================================
    # TEST 4: WRONG DIRECTION
    # ======================================

    def test_wrong_direction_is_rejected(self):

        player = new_game("Jimmy")

        result = move_player(player, "cave")

        self.assertEqual(result, "invalid")
        self.assertEqual(player["location"], "beach")
        self.assertEqual(player["energy"], 5)

    # ======================================
    # TEST 5: COLLECT ROPE ONCE
    # ======================================

    def test_rope_can_only_be_collected_once(self):

        player = new_game("Jimmy")

        player["location"] = "jungle"

        first_result = collect_item(player)
        second_result = collect_item(player)

        self.assertEqual(first_result, "collected_rope")
        self.assertEqual(second_result, "already_collected")

        self.assertEqual(player["inventory"], ["rope"])

    # ======================================
    # TEST 6: BRIDGE REQUIRES ROPE
    # ======================================

    def test_bridge_cannot_be_crossed_without_rope(self):

        player = new_game("Jimmy")

        player["location"] = "old bridge"

        result = move_player(player, "lighthouse")

        self.assertEqual(result, "needs_rope")
        self.assertEqual(player["location"], "old bridge")
        self.assertEqual(player["energy"], 5)

    # ======================================
    # TEST 7: BRIDGE WITH ROPE
    # ======================================

    def test_bridge_can_be_crossed_with_rope(self):

        player = new_game("Jimmy")

        player["location"] = "old bridge"
        player["inventory"].append("rope")

        result = move_player(player, "lighthouse")

        self.assertEqual(result, "moved")
        self.assertEqual(player["location"], "lighthouse")
        self.assertEqual(player["energy"], 4)

    # ======================================
    # TEST 8: LANTERN REQUIRED
    # ======================================

    def test_lighthouse_requires_lantern(self):

        player = new_game("Jimmy")

        player["location"] = "lighthouse"

        result = light_beacon(player)

        self.assertEqual(result, "needs_lantern")
        self.assertFalse(is_win(player))
        self.assertFalse(player["game_over"])

    # ======================================
    # TEST 9: SUCCESSFUL VICTORY
    # ======================================

    def test_correct_items_and_location_can_win(self):

        player = new_game("Jimmy")

        player["location"] = "lighthouse"
        player["inventory"] = ["rope", "lantern"]

        result = light_beacon(player)

        self.assertEqual(result, "beacon_lit")
        self.assertTrue(is_win(player))
        self.assertTrue(player["game_over"])

    # ======================================
    # TEST 10: ENERGY EXHAUSTION
    # ======================================

    def test_energy_exhaustion_causes_loss(self):

        player = new_game("Jimmy")

        player["energy"] = 1

        result = move_player(player, "jungle")

        self.assertEqual(result, "lost")
        self.assertEqual(player["energy"], 0)
        self.assertTrue(player["game_over"])
        self.assertFalse(player["won"])

        # Energy must never become negative
        self.assertGreaterEqual(player["energy"], 0)

    # ======================================
    # TEST 11: LANTERN COLLECTION
    # ======================================

    def test_lantern_can_be_collected_in_cave(self):

        player = new_game("Jimmy")

        player["location"] = "cave"

        result = collect_item(player)

        self.assertEqual(result, "collected_lantern")
        self.assertEqual(player["inventory"], ["lantern"])

    # ======================================
    # TEST 12: REPLAY RESET
    # ======================================

    def test_new_game_resets_player_state(self):

        old_player = new_game("Jimmy")

        old_player["location"] = "jungle"
        old_player["energy"] = 2
        old_player["inventory"].append("rope")

        new_player = new_game("Jimmy")

        self.assertEqual(new_player["location"], "beach")
        self.assertEqual(new_player["energy"], 5)
        self.assertEqual(new_player["inventory"], [])
        self.assertFalse(new_player["game_over"])
        self.assertFalse(new_player["won"])

        # The inventories must be independent lists
        self.assertIsNot(
            old_player["inventory"],
            new_player["inventory"]
        )

    # ======================================
    # TEST 13: NO MOVEMENT AFTER GAME OVER
    # ======================================

    def test_player_cannot_move_after_game_over(self):

        player = new_game("Jimmy")

        player["game_over"] = True

        result = move_player(player, "jungle")

        self.assertEqual(result, "game_over")
        self.assertEqual(player["location"], "beach")
        self.assertEqual(player["energy"], 5)

    # ======================================
    # TEST 14: AVAILABLE ACTIONS
    # ======================================

    def test_available_actions_at_beach(self):

        player = new_game("Jimmy")

        actions = available_actions(player)

        self.assertEqual(
            actions,
            ["jungle", "inventory", "quit"]
        )

    # ======================================
    # TEST 15: NO ACTIONS AFTER GAME OVER
    # ======================================

    def test_no_actions_after_game_over(self):

        player = new_game("Jimmy")

        player["game_over"] = True

        actions = available_actions(player)

        self.assertEqual(actions, [])


if __name__ == "__main__":

    unittest.main()
