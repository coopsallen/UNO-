import random

class UnoPlayer:
    def __init__(self):
        self.name = "HelensburghHobbits"
        self.hand = []

    def play_card(self, top_card, draw_amount):
        colours = ["red", "blue", "green", "yellow"]

        def split_card(card):
            if card in ["wild", "wild_draw"]:
                return None, card
            parts = card.split()
            return parts[0], parts[1]

        def card_value(card):
            if "wild" in card:
                return 50
            if any(x in card for x in ["draw", "skip", "reverse"]):
                return 20
            return int(card.split()[1])

        def best_colour():
            counts = {colour: 0 for colour in colours}
            for card in self.hand:
                if card not in ["wild", "wild_draw"]:
                    colour = card.split()[0]
                    counts[colour] += 1
            return max(counts, key=counts.get)

        def valid_play(card):
            top_colour, top_type = split_card(top_card)

            if card in ["wild", "wild_draw"]:
                return True

            colour, card_type = split_card(card)

            # If draw stack exists, only continue with draw/wild_draw type cards
            if draw_amount > 0:
                return card_type == "draw"

            return colour == top_colour or card_type == top_type

        playable = [card for card in self.hand if valid_play(card)]

        if not playable:
            return None

        # During draw stack, avoid picking up by playing draw cards first
        if draw_amount > 0:
            draw_cards = [card for card in playable if "draw" in card or card == "wild_draw"]
            if draw_cards:
                chosen = max(draw_cards, key=card_value)
            else:
                return None
        else:
            # General strategy: dump highest-point playable card first
            chosen = max(playable, key=card_value)

        # Add colour when playing wild cards
        if chosen in ["wild", "wild_draw"]:
            return f"{best_colour()} {chosen}"

        return chosen

    def valid_play(self, top_card, play_card, draw_amount):
        if play_card is None:
            return True

        colours = ["red", "blue", "green", "yellow"]

        if play_card in ["wild", "wild_draw"]:
            return False

        play_parts = play_card.split()
        top_parts = top_card.split()

        play_colour = play_parts[0]
        play_type = play_parts[1]
        top_colour = top_parts[0]
        top_type = top_parts[1]

        if play_colour not in colours:
            return False

        if play_type in ["wild", "wild_draw"]:
            return True

        if draw_amount > 0:
            return play_type == "draw"

        return play_colour == top_colour or play_type == top_type



