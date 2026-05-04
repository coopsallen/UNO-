import random

class UnoPlayer:
    def __init__(self):
        self.name = 'Param'  # add your name here and change the filename to match!
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

    def play_card(self, top_card, draw_amount):
        '''Your team must implement this! top_card is the current card
         at the top of the discard pile. draw_amount is an integer to tell
         you if you are expected to draw from the current top_card
         Ensure that the card you play is legal for our rules.'''
        # Select a random card, if it's a valid play, then play it
        # otherwise we play nothing! (A BAD strategy)
        # card = random.choice(self.hand)

        # if "wild" in card:
        #     # Need to add a colour to "Wild" cards. Random is probably a BAD strategy!
        #     card = f"{random.choice(("red", "green", "blue", "yellow"))} {card}"
        # # play the chosen card if valid, otherwise play nothing
        # if self.valid_play(top_card, card, draw_amount):
        #     return card
        # return None

        # Checking if I need to draw cards
        if draw_amount:
            if "wild_draw" in self.hand:
                return "red wild_draw"

            for card_in_hand in self.hand:
                if len(card_in_hand.split()) > 1 and card_in_hand.split()[1] == "draw":
                    return card_in_hand

            return None
        
        for card_in_hand in self.hand:
            if card_in_hand == "wild":
                card = "red " + card_in_hand
                return card
        
        color_of_top_card = top_card.split()[0]

        if top_card.split()[1] != "wild":
            number_of_top_card = top_card.split()[1]
        number_of_top_card = None

        has_reverse = False
        has_draw = False
        has_color = False
        has_number = False
        has_wild = False

        for card_in_hand in self.hand:
            if color_of_top_card in card_in_hand:
                if card_in_hand.split()[1] == "draw":
                    has_draw = True
                    draw_card = card_in_hand
                elif card_in_hand.split()[1] == "reverse":
                    has_reverse = True
                    reverse_card = card_in_hand
                else:
                    has_color = True
                    color_card = card_in_hand
            elif number_of_top_card != None and number_of_top_card in card_in_hand:
                has_number = True
                number_card = card_in_hand
        
        if has_draw:
            card = draw_card
        elif has_reverse:
            card = reverse_card
        elif has_color:
            card = color_card
        elif has_number:
            card = number_card
        else:
            card = None
        
        # if self.valid_play(top_card, card, draw_amount):
        #     return card
        return card

                        

    def valid_play(self, top_card, play_card, draw_amount):
        '''You don't have to implement this, but it is recommended to
        help make play_card easier to write and read!'''
        return False
