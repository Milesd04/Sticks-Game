from sticks import SticksGame
from player import Player
from bot import AIPlayer

def main():
    print("Welcome to Sticks!")

    # Create Player 1 (human)
    player1_name = input("Enter Player 1's name: ")
    player1 = Player(player1_name)

    # Ask if Player 2 should be human or AI
    opponent_choice = ''
    while opponent_choice not in ['human', 'ai']:
        opponent_choice = input("Do you want to play against a human or AI? (type 'human' or 'ai'): ").strip().lower()

        if opponent_choice not in ['human', 'ai']:
            print("Invalid choice. Please choose either 'human' or 'ai'.")

    if opponent_choice == 'ai':
        # Create an AI Player for Player 2
        player2 = AIPlayer("AI")
    elif opponent_choice == 'human':
        # Create a Human Player for Player 2
        player2_name = input("Enter Player 2's name: ")
        player2 = Player(player2_name)

    # Initialize and start the game
    game = SticksGame(player1, player2)

    # Play the game in a loop until one player wins
    game_in_progress = True
    while game_in_progress:
        game_in_progress = game.play_turn()

if __name__ == "__main__":
    main()
