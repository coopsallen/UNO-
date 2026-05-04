class UnoPlayer:
    def __init__(self):
        self.name = 'Best Team'
        self.hand = []

    def add_cards(self, cards: list):
        self.hand.extend(cards)

    def remove_cards(self, cards: list):
        for card in cards:
            if 'wild' in card:
                card = card.split()[1]
            if card not in self.hand:
                return False
            self.hand.remove(card)
        return True

    def play_card(self, top_card, draw_amount):
        top_colour, top_type = top_card.split()

        def card_colour(card):
            if card in ('wild', 'wild_draw'):
                return None
            return card.split()[0]

        def card_type(card):
            if card in ('wild', 'wild_draw'):
                return card
            return card.split()[1]

        def card_value(card):
            c_type = card_type(card)
            if c_type in ('wild', 'wild_draw'):
                return 50
            if c_type in ('draw', 'skip', 'reverse'):
                return 20
            return int(c_type)

        def best_colour():
            counts = {'red': 0, 'blue': 0, 'green': 0, 'yellow': 0}
            for card in self.hand:
                colour = card_colour(card)
                if colour in counts:
                    counts[colour] += 1
            return max(counts, key=counts.get)

        def legal_card(card):
            c_colour = card_colour(card)
            c_type = card_type(card)

            if draw_amount > 0:
                return c_type in ('draw', 'wild_draw')

            if c_type in ('wild', 'wild_draw'):
                return True

            return c_colour == top_colour or c_type == top_type

        playable_cards = [card for card in self.hand if legal_card(card)]

        if not playable_cards:
            return None

        if draw_amount > 0:
            playable_cards.sort(key=card_value, reverse=True)
            chosen = playable_cards[0]
            if chosen == 'wild_draw':
                return best_colour() + ' wild_draw'
            return chosen

        non_wild_cards = [card for card in playable_cards if card not in ('wild', 'wild_draw')]

        if non_wild_cards:
            non_wild_cards.sort(key=card_value, reverse=True)
            return non_wild_cards[0]

        playable_cards.sort(key=card_value, reverse=True)
        chosen = playable_cards[0]
        colour = best_colour()

        if chosen == 'wild_draw':
            return colour + ' wild_draw'

        if chosen == 'wild':
            return colour + ' wild'

        return None

    def valid_play(self, top_card, play_card, draw_amount):
        top_colour, top_type = top_card.split()
        parts = play_card.split()

        if len(parts) != 2:
            return False

        play_colour, play_type = parts

        if play_type in ('wild', 'wild_draw'):
            return play_colour in ('red', 'blue', 'green', 'yellow')

        if draw_amount > 0:
            return play_type == 'draw'

        return play_colour == top_colour or play_type == top_type
