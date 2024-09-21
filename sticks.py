from player import Player
from bot import AIPlayer

class SticksGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_turn = 0  # Player 1 starts

    def play_turn(self):
        current_player = self.players[self.current_turn]
        opponent = self.players[1 - self.current_turn]

        # Display the current state
        print(f"\n{current_player.name}'s turn:")
        print(current_player)
        print(opponent)

        if isinstance(current_player, AIPlayer):
            # AI's turn
            action = current_player.decide_action(opponent)

            if action == "tap":
                my_hand, their_hand = current_player.choose_hand_to_tap(opponent)
                print(f"{current_player.name} taps with hand {my_hand + 1} on opponent's hand {their_hand + 1}.")
                current_player.tap(opponent, my_hand, their_hand)

            elif action == "split":
                hand_from, hand_to, points = current_player.choose_hands_to_split()
                print(f"{current_player.name} splits {points} points from hand {hand_from + 1} to hand {hand_to + 1}.")
                current_player.split(hand_from, hand_to, points)

        else:
            # Human player's turn with loop for valid move
            valid_move = False
            while not valid_move:
                try:
                    action = input("Do you want to 'tap' or 'split'? ").strip().lower()

                    if action not in ["tap", "split"]:
                        raise ValueError("Invalid action. Please enter 'tap' or 'split'.")

                    if action == "tap":
                        my_active_hands = [i for i in range(2) if current_player.hands[i] > 0]

                        if len(my_active_hands) == 1:
                            my_hand = my_active_hands[0]
                            print(f"You only have one active hand. Using hand {my_hand + 1} automatically.")
                        else:
                            my_hand = int(input(f"Which of your hands (1 or 2)? ")) - 1  # Subtract 1 for 0-based index

                        active_hands = [i for i in range(2) if opponent.hands[i] > 0]

                        if len(active_hands) == 1:
                            their_hand = active_hands[0]
                            print(f"Opponent only has one hand active. Tapping hand {their_hand + 1}.")
                        else:
                            their_hand = int(input(f"Which opponent hand to tap (1 or 2)? ")) - 1  # Subtract 1 for 0-based index

                        # Attempt to tap
                        current_player.tap(opponent, my_hand, their_hand)
                        valid_move = True  # Move was successful

                    elif action == "split":
                        hand_from = int(input(f"Which hand to take points from (1 or 2)? ")) - 1  # Subtract 1 for 0-based index

                        if current_player.hands[0] == 0 or current_player.hands[1] == 0:
                            hand_to = 1 - hand_from
                            print(f"Splitting points to your other hand {hand_to + 1}.")
                        else:
                            hand_to = 1 - hand_from

                        if current_player.hands[hand_from] == 1:
                            print(f"Hand {hand_from + 1} only has 1 point. Automatically moving it to hand {hand_to + 1}.")
                            points = 1
                        else:
                            points = int(input(f"How many points to move? "))

                        # Attempt the split
                        current_player.split(hand_from, hand_to, points)

                        # Move was successful
                        valid_move = True

                except (ValueError, IndexError) as e:
                    print("ERROR! Please enter a valid input.")  # Error message
                    # Optionally, you can print the error message as well
                    # print(f"Invalid input: {e}")

        # Check for win condition
        if opponent.is_knocked_out():
            print(f"{current_player.name} wins!")
            return False  # Game ends

        # Switch turn to the other player
        self.current_turn = 1 - self.current_turn
        return True  # Continue the game loop


# Main loop to run the game
if __name__ == "__main__":
    player1 = Player("Player 1")
    player2 = Player("Player 2")
    game = SticksGame(player1, player2)

    while game.play_turn():
        pass
