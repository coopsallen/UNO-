import random

class UnoPlayer:
    def __init__(self):
        self.name = 'Table24'  # add your name here and change the filename to match!
        self.hand = []  # don't change this

    def add_cards(self, cards: list):
        '''Don't change this method'''
        self.hand.extend(cards)

    def remove_cards(self, cards: list):
        '''Don't change this method'''
        for card in cards:
            if "wild" in card:
                card = card.split()[1]
            if card not in self.hand:
                return False
            self.hand.remove(card)
        return True
    
    def choose_colour(self):
        """
        Check which colour you have the most of in your hand.
        """
        red_count = 0
        blue_count = 0
        green_count = 0
        yellow_count = 0

        for card in self.hand:
            if card.split()[0] == "red":
                red_count += 1
            elif card.split()[0] == "blue":
                blue_count += 1
            elif card.split()[0] == "green":
                green_count += 1
            elif card.split()[0] == "yellow":
                yellow_count += 1
        # Match colour to the count
        colours = {
            'red' : red_count,
            'blue' : blue_count,
            'green' : green_count,
            'yellow' : yellow_count,
        }
        max_colour, max_cards = max(colours.items(), key=lambda item: item[1])
        return max_colour

    def play_card(self, top_card, draw_amount):
        '''Your team must implement this! top_card is the current card
         at the top of the discard pile. draw_amount is an integer to tell
         you if you are expected to draw from the current top_card
         Ensure that the card you play is legal for our rules.'''
        # Select a random card, if it's a valid play, then play it
        # otherwise we play nothing! (A BAD strategy)
        # card = random.choice(self.hand)

        play_card = random.choice(self.hand)

        # Try play a wild draw on top of a wild draw
        if "wild_draw" in top_card:
            for card in self.hand:
                if "wild_draw" in card:
                    colour = choose_colour()
                    play_card = f"{colour} wild_draw"
                    continue
            else:
                pass
        # Deal with colour card and regular wild card
        else:
            colour = top_card.split()[0]
            if "draw" in top_card:
                for card in self.hand:
                    if "wild_draw" in card:
                        colour = choose_colour()
                        play_card = f"{colour} wild_draw"
                        continue
                    elif "draw" in card:
                        play_card = card
                        continue
            else:
                colour = top_card.split()[0]
                number = top_card.split()[1]
                for card in self.hand:
                    if colour in card:
                        play_card = card
                        continue
                    elif number in card:
                        play_card = card
                        continue

        # play the chosen card if valid, otherwise play nothing
        if self.valid_play(top_card, play_card, draw_amount):
            return play_card
        return None

    def valid_play(self, top_card, play_card, draw_amount):
        '''You don't have to implement this, but it is recommended to
        help make play_card easier to write and read!'''
        
        return False

