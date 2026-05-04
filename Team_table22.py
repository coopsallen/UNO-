import random

class UnoPlayer:
    def __init__(self):
        self.name = 'Team_table22'  # add your name here and change the filename to match!
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
        '''Your team must implement this!
         top_card is the current card
         at the top of the discard pile. 
         draw_amount is an integer to tell
         you if you are expected to draw from the current top_card
         Ensure that the card you play is legal for our rules.'''
        # Select a random card, if it's a valid play, then play it
                # # Select a random card, if it's a valid play, then play it
        # # otherwise we play nothing! (A BAD strategy)
        if playable_cards:
            chosen_card = random.choice(playable_cards)
            
            if "wild" in chosen_card:
                colour = random.choice(["red", "green", "blue", "yellow"])
                return f"{colour} {chosen_card}"

            if self.valid_play(top_card, card, draw_amount):
                return chosen_card

        # APPROACH 1
        # ------------------------------------

        # top card split
    #     top_parts = top_card.split()
    #     top_colour = top_parts[0]
    #     top_type = " ".join(top_parts[1:]) 

    #     # legal moves
    #     legal_moves = []
    #     for card in self.hand:
    #         # draw situation
    #         if draw_amount > 0:
    #             if "draw" in card:
    #                 legal_moves.append(card)
    #             continue
            
    #         # Standard rules
    #         if "wild" in card:
    #             legal_moves.append(card)
    #         elif top_colour in card:
    #             legal_moves.append(card)
    #         elif top_type in card:
    #             legal_moves.append(card)

    #     # no moves and take the L
    #     if not legal_moves:
    #         return None

    #     # highest point value
    #     best_card = self._get_highest_value_card(legal_moves)

    #     # Format return
    #     if "wild" in best_card:
    #         chosen_colour = self._get_best_colour()
    #         return f"{chosen_colour} {best_card}"

    #     return best_card

    # def _get_highest_value_card(self, moves):
    #     """Helper to safely calculate points and find the most expensive card[cite: 1]"""
    #     def score(card):
    #         card_type = card.split()[-1] 
            
    #         if "wild" in card: 
    #             return 50 # Wilds
    #         if card_type in ["draw", "skip", "reverse"]: 
    #             return 20 # Actions
            
    #         try:
    #             return int(card_type)
    #         except (ValueError, IndexError):
    #             return 0
        
    #     return max(moves, key=score)

    # def _get_best_colour(self):
    #     """Picks the colour you hold the most of to maximize future moves"""
    #     counts = {"red": 0, "blue": 0, "green": 0, "yellow": 0}
    #     for card in self.hand:
    #         for colour in counts:
    #             if colour in card:
    #                 counts[colour] += 1
    #     return max(counts, key=counts.get)


    # APPROACH 2
    # -------------------------------------------------

#prob delect:
        if(draw_amount == 0):
            playable = []
            for c in self.hand:
                if self.valid_play(top_card, c, draw_amount):
                    playable.append(c)
            if not playable:
                return None
            normals = []
            wilds = []
            for c in playable:
                if "wild" not in c:
                    normals.append(c)
                else:
                    wilds.append(c)
            if normals:
                card = random.choice(normals) #add something here
            elif "wild_draw" in wilds:
                card = "wild_draw"
            else:
                card = "wild"
            if "wild" in card:
                # Need to add a colour to "Wild" cards. Random is probably a BAD strategy!
                r_count = 0
                g_count = 0
                b_count = 0
                y_count = 0
                for c in self.hand:
                    if(c[0] == "r"):
                        r_count += 1
                    if(c[0] == "g"):
                        g_count += 1
                    if(c[0] == "b"):
                        b_count += 1
                    if(c[0] == "y"):
                        y_count += 1
                highest = max(r_count, g_count, b_count, y_count)
                if(highest == r_count):
                    return f"red {card}"
                if(highest == g_count):
                    return f"green {card}"
                if(highest == b_count):
                    return f"blue {card}"
                if(highest == y_count):
                    return f"yellow {card}"
            # play the chosen card if valid, otherwise play nothing  
            if self.valid_play(top_card, card, draw_amount):
                return card
            return None
        else:
            if "wild_draw" in self.hand:
                colour = random.choice(["red","green","blue","yellow"])
                return f"{colour} wild_draw"
            for c in self.hand:
                if "wild" not in c and c.split()[1] == "draw":
                    return c
            return None

    def valid_play(self, top_card, play_card, draw_amount):
        '''You don't have to implement this, but it is recommended to
        help make play_card easier to write and read!'''
        if(draw_amount == 0): 
            top_list = top_card.split(" ")
            top_val = top_list[1]   
            play_card_list = play_card.split(" ")
            play_card_val = play_card_list[0]
            
            if "wild" in play_card_val:
                    return True
            else:
                if(top_card[0] == play_card[0] or top_val == play_card_val):
                    return True
                else:
                    return False
        return False

