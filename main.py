
play_again = "yes"

while play_again == "yes":

    print("==============================")
    print("     MYSTERY ISLAND")
    print("    THE LOST LIGHTHOUSE")
    print("==============================")

    print("You wake up on Mystery Island after a powerful storm.")
    print("Your only chance of rescue is to restore the lighthouse beacon.")
    print("Explore the island, collect useful objects and find a way to escape.")
    print()
    print("Commands: destination, pick, inventory, light, quit")

    player = input("\nWhat is your name? ").strip()

    # PLAYER INFORMATION
    current_location = "beach"
    inventory = []
    energy = 5

    # ISLAND MAP
    locations = {
        "beach": ["jungle"],
        "jungle": ["beach", "cave"],
        "cave": ["jungle", "old bridge"],
        "old bridge": ["cave", "lighthouse"],
        "lighthouse": ["old bridge"]
    }

    # LOCATION DESCRIPTIONS
    scenes = {
        "beach": "You are on a quiet beach. Waves roll in. A path leads inland.",
        "jungle": "You are in a thick jungle. A strong rope lies beside an old tree.",
        "cave": "You are inside a dark cave. An old lantern sits on a rock.",
        "old bridge": "You stand before an old bridge connecting the island to the lighthouse.",
        "lighthouse": "You have reached the lighthouse. Its beacon is dark."
    }

    game_running = True

    while game_running:

        print("\n==============================")
        print("Current location:", current_location.title())
        print("Energy:", "⚡" * energy, f"({energy}/5)")
        print("==============================")

        print(scenes[current_location])

        print("\nConnected destinations:", locations[current_location])

        print("\nAvailable commands:")
        print("1. Type a destination to move")
        print("2. Type 'pick' to collect an item")
        print("3. Type 'inventory' to see your items")
        print("4. Type 'quit' to leave")

        if current_location == "lighthouse":
            print("5. Type 'light' to restore the beacon")

        choice = input("\nYour choice: ").strip().lower()

        # QUIT
        if choice == "quit":
            game_running = False
            print("Goodbye,", player, "!")

        # INVENTORY
        elif choice == "inventory":

            if len(inventory) == 0:
                print("Your inventory is empty.")
            else:
                print("You are carrying:", inventory)

        # COLLECT ITEMS
        elif choice == "pick":

            if current_location == "jungle":

                if "rope" in inventory:
                    print("You already collected the rope.")
                else:
                    inventory.append("rope")
                    print("You collected the rope!")

            elif current_location == "cave":

                if "lantern" in inventory:
                    print("You already collected the lantern.")
                else:
                    inventory.append("lantern")
                    print("You collected the lantern!")

            else:
                print("There are no useful items to collect here.")

        # LIGHT THE LIGHTHOUSE
        elif choice == "light":

            if current_location != "lighthouse":
                print("You must reach the lighthouse first.")

            elif "lantern" not in inventory:
                print("You need a lantern to restore the beacon.")

            else:
                print("\nYou use the lantern to restore the lighthouse beacon!")
                print("A rescue boat spots the light in the distance.")
                print("Congratulations,", player, "! YOU WIN!")
                game_running = False

        # PLAYER MOVEMENT
        elif choice in locations[current_location]:

            if (current_location == "old bridge"
                    and choice == "lighthouse"
                    and "rope" not in inventory):

                print("The bridge is locked!")
                print("You need a rope before you can cross.")

            else:
                current_location = choice
                energy = energy - 1

                print("You travelled to", current_location.title())
                print("Energy remaining:", energy)

                if energy == 0:
                    print("\nYou have run out of energy!")
                    print("You could not complete your mission.")
                    print("GAME OVER!")
                    game_running = False

        # INVALID INPUT
        else:
            print("Invalid action. Please try again.")

    # REPLAY OPTION
    print("\n==============================")
    play_again = input("Would you like to play again? (yes/no): ")
    play_again = play_again.strip().lower()

    while play_again not in ["yes", "no"]:
        print("Please enter yes or no.")
        play_again = input("Would you like to play again? ").strip().lower()

print("\nThank you for playing MYSTERY ISLAND!")
