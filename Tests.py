'''
Run this test using "pytest Tests.py"
You should see any errors that run in your code.
If you get an AssertionError, it means your code
has executed but you have failed the test case.
Look at the compared output to the expected.

Remember: You SHOULD NOT add or remove any cards
to/from your hand when writing your play_card method.
The simulation will handle that for you.
Just pick a card to play from your hand, based on the input.
'''

'''Change TeamName to the name of your .py file'''
from UnoPlayers.Best_Team import UnoPlayer

colours = ("red", "blue", "green", "yellow")

def test_play_card():
    new_player = UnoPlayer()
    new_player.hand = [
      "blue 9", "green 0", "yellow reverse",
      "red skip", "blue draw", "red 9",
      "yellow 0", "blue skip", "red skip"
    ]
    played = new_player.play_card("blue 9", 0)
    assert played in [None, "blue 9", "red 9",
                      "blue skip", "blue draw"]

def test_play_wild():
    new_player = UnoPlayer()
    new_player.hand = ["wild"]
    played = new_player.play_card("red 0", 0)
    assert played in [None] + [f"{colour} wild" for colour in colours]

def test_play_number_match():
    new_player = UnoPlayer()
    new_player.hand = [
      "blue 9"
    ]
    played = new_player.play_card("red 9", 0)
    assert played in [None, "blue 9"]

def test_cant_play():
    new_player = UnoPlayer()
    new_player.hand = [
      "blue 9", "yellow reverse",
      "red skip", "blue draw", "red 9",
      "yellow 0", "blue skip", "red skip"
    ]
    played = new_player.play_card("green 7", 0)
    assert played is None

def test_play_draw():
    new_player = UnoPlayer()
    new_player.hand = [
      "blue 9", "yellow reverse",
      "red skip", "red 9",
      "yellow 0", "blue skip", "red skip"
    ]
    played = new_player.play_card("blue draw", 2)
    assert played is None, "You must return None if you cannot play draw cards when required to draw"

