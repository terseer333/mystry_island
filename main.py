
# ==========================================
# MYSTERY ISLAND - MAIN PROGRAM
# ==========================================

from game import (
    new_game,
    move_player,
    collect_item,
    available_actions,
    light_beacon,
    is_win
)


# ==========================================
# LOCATION DESCRIPTIONS
# ==========================================

SCENES = {
    "beach": "You are on a quiet beach. Waves roll in. A path leads inland.",

    "jungle": "You are in a thick jungle. A strong rope lies beside an old tree.",

    "cave": "You are inside a dark cave. An old lantern sits on a rock.",

    "old bridge": "You stand before an old bridge connecting the island to the lighthouse.",

    "lighthouse": "You have reached the lighthouse. Its beacon is dark."
}


# ==========================================
# DISPLAY PLAYER STATUS
# ==========================================

def show_status(player):

    print("\n==============================")

    print("Current location:", player["location"].title())

    print(
        "Energy:",
        "⚡" * player["energy"],
        f"({player['energy']}/5)"
    )

    print("==============================")


# ==========================================
# DISPLAY AVAILABLE ACTIONS
# ==========================================

def show_menu(player):

    actions = available_actions(player)

    print("\nAvailable actions:")

    for action in actions:

        if action == "pick":
            print("- pick (collect an item)")

        elif action == "inventory":
            print("- inventory")

        elif action == "quit":
            print("- quit")

        elif action == "light":
            print("- light (restore the beacon)")

        else:
            print("- Travel to", action.title())

    # Show bridge restriction
    if (player["location"] == "old bridge"
            and "rope" not in player["inventory"]):

        print("- Lighthouse (LOCKED: requires rope)")

    # Show lighthouse restriction
    if (player["location"] == "lighthouse"
            and "lantern" not in player["inventory"]):

        print("- light (LOCKED: requires lantern)")


# ==========================================
# DISPLAY INVENTORY
# ==========================================

def show_inventory(player):

    if len(player["inventory"]) == 0:

        print("Your inventory is empty.")

    else:

        print("You are carrying:", player["inventory"])


# ==========================================
# HANDLE PLAYER ACTIONS
# ==========================================

def handle_action(player, choice):

    choice = choice.strip().lower()

    # QUIT
    if choice == "quit":

        player["game_over"] = True

        print("Goodbye,", player["name"], "!")

    # INVENTORY
    elif choice == "inventory":

        show_inventory(player)

    # PICK UP ITEMS
    elif choice == "pick":

        result = collect_item(player)

        if result == "collected_rope":

            print("You collected the rope!")

        elif result == "collected_lantern":

            print("You collected the lantern!")

        elif result == "already_collected":

            print("You already collected that item.")

        elif result == "nothing_here":

            print("There is nothing to collect here.")

        elif result == "game_over":

            print("The game has ended.")

    # LIGHTHOUSE
    elif choice == "light":

        result = light_beacon(player)

        if result == "beacon_lit":

            print("\nYou use the lantern to restore the lighthouse beacon!")
            print("A rescue boat spots the light in the distance.")

            print(
                "Congratulations,",
                player["name"],
                "! YOU WIN!"
            )

        elif result == "needs_lantern":

            print("You need a lantern to restore the beacon.")

        elif result == "not_at_lighthouse":

            print("You must reach the lighthouse first.")

        else:

            print("The game has already ended.")

    # MOVEMENT
    else:

        result = move_player(player, choice)

        if result == "moved":

            print("You travelled to", player["location"].title())

            print("Energy remaining:", player["energy"])

        elif result == "needs_rope":

            print("The bridge is locked!")
            print("You need a rope before you can cross.")

        elif result == "lost":

            print("You travelled to", player["location"].title())

            print("Energy:", "⚡" * player["energy"], f"({player['energy']}/5)")

            print("\nYou have run out of energy!")
            print("You could not complete your mission.")
            print("GAME OVER!")

        elif result == "invalid":

            print("Invalid action or destination.")
            print("Please try again.")

        elif result == "game_over":

            print("The game has already ended.")


# ==========================================
# RUN ONE ADVENTURE
# ==========================================

def run_adventure(player):

    while not player["game_over"]:

        show_status(player)

        print(SCENES[player["location"]])

        show_menu(player)

        choice = input("\nYour choice: ")

        handle_action(player, choice)


# ==========================================
# MAIN GAME AND REPLAY
# ==========================================

def main():

    print("==============================")
    print("     MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("==============================")

    print("You wake up on Mystery Island after a powerful storm.")
    print("Your only chance of rescue is to restore the lighthouse beacon.")
    print("Explore the island, collect useful objects and find a way to escape.")

    while True:

        # Ask for player name
        name = input("\nWhat is your name? ").strip()

        # Create a fresh game
        player = new_game(name)

        # Start the adventure
        run_adventure(player)

        # Display final outcome
        if is_win(player):

            print("\nMISSION COMPLETED!")

        elif player["energy"] == 0:

            print("\nYour adventure has ended in failure.")

        else:

            print("\nYou left the island without completing the mission.")

        # Replay
        replay = input(
            "\nWould you like to play again? (yes/no): "
        )

        replay = replay.strip().lower()

        # Validate replay response
        while replay not in ["yes", "no"]:

            print("Please enter yes or no.")

            replay = input(
                "Would you like to play again? (yes/no): "
            ).strip().lower()

        if replay == "no":

            break

        print("\nStarting a new adventure...")

    print("\nThank you for playing MYSTERY ISLAND!")


# ==========================================
# PROGRAM ENTRY POINT
# ==========================================

if __name__ == "__main__":

    main()
