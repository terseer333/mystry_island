
# Mystery Island — The Lost Lighthouse

A beginner-friendly Python text-adventure game.

## About the Game

You wake up on Mystery Island after a powerful storm.
Your only chance of rescue is to restore the lighthouse beacon.

Explore the island, collect useful objects, manage your energy
and solve the challenges preventing your escape.

## Requirements

- Python 3
- No external Python packages required.
- A terminal or command-line interface.

## Project Structure

```text
mystry_island/
├── main.py
├── game.py
├── README.md
├── .gitignore
└── tests/
    └── test_game.py
```

## Installation and Setup

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Enter the project directory:

```bash
cd mystry_island
```

Check your Python version:

```bash
python3 --version
```

## How to Run

Start the game:

```bash
python3 main.py
```

Enter your name and follow the instructions displayed
in the terminal.

## Game Locations

The island contains five locations:

1. Beach — starting location.
2. Jungle — contains the rope.
3. Cave — contains the lantern.
4. Old Bridge — requires the rope.
5. Lighthouse — requires the lantern to restore the beacon.

## Game Rules

- The player starts with 5 energy points.
- Every successful movement costs 1 energy point.
- Returning to a previous location also costs 1 energy point.
- Collecting items does not consume energy.
- Viewing inventory does not consume energy.
- Invalid actions do not consume energy.
- The rope must be collected before crossing the Old Bridge.
- The lantern is required to restore the lighthouse beacon.
- Each useful item can only be collected once.
- Energy reaching zero results in a loss.
- Restoring the beacon with the required item results in victory.

## Available Commands

- `jungle`, `beach`, `cave`, `old bridge`, `lighthouse` — travel between connected locations.
- `pick` — collect an available item.
- `inventory` — inspect collected items.
- `light` — restore the lighthouse beacon.
- `quit` — leave the adventure.

Commands are case-insensitive.

## Example Winning Journey

Starting energy: 5

1. Beach → Jungle.
2. Collect the rope.
3. Jungle → Cave.
4. Collect the lantern.
5. Cave → Old Bridge.
6. Cross to Lighthouse.
7. Type `light` to restore the beacon.

The player wins with 1 energy point remaining.

## Running Automated Tests

Run the test suite:

```bash
python3 -m unittest discover -s tests -v
```

The project includes tests for:

- New game initialization.
- Valid and invalid movement.
- Energy consumption.
- Rope and lantern collection.
- Duplicate item prevention.
- Bridge restrictions.
- Lighthouse requirements.
- Victory and loss conditions.
- Replay reset.
- Actions after game over.

## Known Limitations

- The game uses a fixed island map.
- There is no graphical interface.
- Game progress is not saved between program sessions.
- The island has two collectible objects.
- There are no random events or multiple endings.
- The game runs entirely in the terminal.

## Technologies

- Python 3
- Python standard library
- unittest

## Author

Jimmy

## Project

EASY TRACK — MYSTERY ISLAND

The Lost Lighthouse
