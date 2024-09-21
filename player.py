class Player:
    def __init__(self, name):
        """
        Initialize player with two hands starting at 1 point each.
        """
        self.name = name
        self.hands = [1,1]

    def is_knocked_out(self):
        """
        Check if both hands are knocked out (set to 0)
        """
        return self.hands == [0, 0]

    def tap(self, opponent, my_hand, their_hand):
        """
        Add the number of points from one of your hands to the opponent's hand.
        """
        if self.hands[my_hand] > 0 and opponent.hands[their_hand] > 0:
            opponent.hands[their_hand] += self.hands[my_hand]
            if opponent.hands[their_hand] >= 5:
                opponent.hands[their_hand] = 0
        else:
            raise ValueError("Invalid move: Dead hand cannot tap or be tapped.")
        
    def split(self, hand_from, hand_to, points):
        # Check if the move is valid
        if hand_from == hand_to:
            print("You cannot split points to the same hand.")
            return

        # Validate points to move
        if points <= 0 or points > self.hands[hand_from]:
            print("Invalid number of points to split.")
            return

        # Perform the split
        self.hands[hand_from] -= points
        self.hands[hand_to] += points

        # Check if the new distribution is a swap
        if self.hands[hand_from] == points and self.hands[hand_to] == (self.hands[hand_from] + points):
            print("Invalid move: swapping hands is not allowed.")
            self.hands[hand_from] += points  # Undo the split
            self.hands[hand_to] -= points
            return

        print(f"Moved {points} points from hand {hand_from + 1} to hand {hand_to + 1}.")

    def __str__(self):
        return f"{self.name}'s hands: {self.hands}"
