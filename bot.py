import random
from player import Player

class AIPlayer(Player):
    def decide_action(self, opponent):
        """AI decides to either tap or split based on the current game state."""
        # If the AI can knock out an opponent's hand, it should tap
        for my_hand in range(2):
            if self.hands[my_hand] > 0:
                for their_hand in range(2):
                    if opponent.hands[their_hand] > 0:
                        if self.hands[my_hand] + opponent.hands[their_hand] >= 5:
                            return 'tap'  # Tap to knock out opponent's hand

        # Otherwise, if the AI has a dangerous hand (e.g., 4 points), it should split
        for hand in range(2):
            if self.hands[hand] == 4:
                return 'split'

        # As a fallback, the AI will tap if it can make progress
        return 'tap'

    def choose_hand_to_tap(self, opponent):
        """AI chooses which hand to use for tapping and which opponent hand to tap."""
        # Prioritize knocking out opponent's hand if possible
        for my_hand in range(2):
            if self.hands[my_hand] > 0:
                for their_hand in range(2):
                    if opponent.hands[their_hand] > 0:
                        if self.hands[my_hand] + opponent.hands[their_hand] >= 5:
                            return my_hand, their_hand

        # Otherwise, choose a random active hand for the AI and opponent
        my_active_hands = [i for i in range(2) if self.hands[i] > 0]
        their_active_hands = [i for i in range(2) if opponent.hands[i] > 0]
        return random.choice(my_active_hands), random.choice(their_active_hands)

    def choose_hands_to_split(self):
        """AI chooses which hand to split points from and to."""
        # If one hand has 4 points, split it to avoid being knocked out
        if self.hands[0] == 4:
            return 0, 1, 2  # Split 2 points to balance the hands
        elif self.hands[1] == 4:
            return 1, 0, 2  # Split 2 points to balance the hands

        # If the AI has only one active hand, split to revive the other
        if self.hands[0] == 0:
            return 1, 0, self.hands[1] // 2  # Split half the points to revive hand 0
        if self.hands[1] == 0:
            return 0, 1, self.hands[0] // 2  # Split half the points to revive hand 1

        # Otherwise, choose a random hand to split from, and move half the points
        active_hands = [i for i in range(2) if self.hands[i] > 0]
        hand_from = random.choice(active_hands)
        hand_to = 1 - hand_from
        points = self.hands[hand_from] // 2  # Split half the points
        return hand_from, hand_to, points
