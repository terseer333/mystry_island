
# ==========================================
# MYSTERY ISLAND - GAME LOGIC
# ==========================================

MAX_ENERGY = 5


# THE ISLAND MAP
LOCATIONS = {
    "beach": ["jungle"],
    "jungle": ["beach", "cave"],
    "cave": ["jungle", "old bridge"],
    "old bridge": ["cave", "lighthouse"],
    "lighthouse": ["old bridge"]
}


# ITEMS AVAILABLE AT EACH LOCATION
ITEMS_BY_LOCATION = {
    "jungle": "rope",
    "cave": "lantern"
}


# ==========================================
# 1. CREATE A NEW GAME
# ==========================================

def new_game(name):

    player = {
        "name": name.strip() or "Player",
        "location": "beach",
        "energy": MAX_ENERGY,
        "inventory": [],
        "game_over": False,
        "won": False
    }

    return player


# ==========================================
# 2. MOVE PLAYER
# ==========================================

def move_player(player, destination):

    # Stop movement after the game ends
    if player["game_over"]:
        return "game_over"

    # Clean up the destination
    destination = destination.strip().lower()

    current_location = player["location"]

    # Check whether the destination exists
    # and is connected to the current location
    if current_location not in LOCATIONS:
        return "invalid"

    if destination not in LOCATIONS[current_location]:
        return "invalid"

    # Check whether rope is required
    if (current_location == "old bridge"
            and destination == "lighthouse"):

        if "rope" not in player["inventory"]:
            return "needs_rope"

    # Update the player's location
    player["location"] = destination

    # Reduce energy after successful movement
    player["energy"] = max(0, player["energy"] - 1)

    # Check whether energy has reached zero
    if player["energy"] == 0:

        player["game_over"] = True

        return "lost"

    return "moved"


# ==========================================
# 3. COLLECT ITEMS
# ==========================================

def collect_item(player):

    # Check whether the game has ended
    if player["game_over"]:
        return "game_over"

    # Find the item at the current location
    item = ITEMS_BY_LOCATION.get(player["location"])

    # Check whether an item exists here
    if item is None:
        return "nothing_here"

    # Prevent duplicate collection
    if item in player["inventory"]:
        return "already_collected"

    # Add the item to inventory
    player["inventory"].append(item)

    return "collected_" + item


# ==========================================
# 4. AVAILABLE ACTIONS
# ==========================================

def available_actions(player):

    # No actions after the game ends
    if player["game_over"]:
        return []

    current_location = player["location"]

    actions = []

    # Check for available items
    item = ITEMS_BY_LOCATION.get(current_location)

    if item is not None and item not in player["inventory"]:
        actions.append("pick")

    # Check connected destinations
    for destination in LOCATIONS[current_location]:

        # Lighthouse requires rope
        if (current_location == "old bridge"
                and destination == "lighthouse"
                and "rope" not in player["inventory"]):

            continue

        actions.append(destination)

    # General actions
    actions.append("inventory")
    actions.append("quit")

    # Lighthouse requires lantern
    if (current_location == "lighthouse"
            and "lantern" in player["inventory"]):

        actions.append("light")

    return actions


# ==========================================
# 5. LIGHT THE LIGHTHOUSE
# ==========================================

def light_beacon(player):

    # Check whether the game has ended
    if player["game_over"]:
        return "game_over"

    # Player must be at the lighthouse
    if player["location"] != "lighthouse":
        return "not_at_lighthouse"

    # Lantern is required
    if "lantern" not in player["inventory"]:
        return "needs_lantern"

    # Restore the beacon
    player["won"] = True
    player["game_over"] = True

    return "beacon_lit"


# ==========================================
# 6. CHECK WINNING CONDITION
# ==========================================

def is_win(player):

    return player["won"]
