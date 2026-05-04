"""
You can use this file to simulate your Uno games!
Place your .py file containing the UnoPlayer class in the UnoPlayers folder.
There are two existing bots for you to challenge, the NaivePlayer and RandomPlayer.
The default is 1000 simulations, you can provide a command line arugment to specify.
e.g. "python3 Simulation.py 50" would run 50 simulations.
"""


import os
import sys
from collections import defaultdict
import importlib.util
from Uno import UnoGame

def main():
    sim_count = int(sys.argv[1]) if len(sys.argv) > 1 else 1000  # Default 1000 sims

    uno_players = load_uno_players("UnoPlayers")
    # Keys of interior dicts will be player names
    results = {
        "wins": defaultdict(int),
        "points": defaultdict(int)
    }

    # Simulate Uno games and store wins/points for players
    for i in range(sim_count):
        new_game = UnoGame(uno_players)
        new_game.play()
        results["wins"][new_game.current_player.name] += 1
        for player in uno_players:
            results["points"][player.name] += calculate_points(player.hand)
        print(f"Games simulated: {i + 1}/{sim_count}", end='\r', flush=True)

    print("\nStatistics Summary:")
    for category, data in results.items():
        print(f"\n{category.capitalize()}:")
        for strategy, value in data.items():
            print(f"  {strategy}: {value}")


def calculate_points(hand: list):
    '''Calcuates total points in Uno hand based off card worth'''

    # Card values determined by Uno ruleset
    point_list = {
        "wild": 50,
        "wild_draw": 50,
        "reverse": 20,
        "skip": 20,
        "draw": 20
    }
    points = 0
    # Calculates total points of cards in hand
    for card in hand:
        if "wild" not in card:
            card = card.split()[1]
        if card in point_list:
            points += point_list[card]
        else:
            points += int(card)
    return points


def load_uno_players(folder_path):
    '''Generates an UnoPlayer instance for every class in folder
    and returns as a list. '''
    
    uno_players = []

    for filename in os.listdir(folder_path):
        i = 3 if filename.endswith(".py") else 4 # char count to remove .py or .pyc
        if filename.endswith(".py") or filename.endswith(".pyc"):
            module_name = filename[:-i]  # remove .py or pyc
            file_path = os.path.join(folder_path, filename)

            # Load the module from the file path
            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)

            # Get the UnoPlayer class and instantiate it
            if hasattr(module, "UnoPlayer"):
                uno_player_class = getattr(module, "UnoPlayer")
                uno_players.append(uno_player_class())


    return uno_players

if __name__ == "__main__":
    main()
