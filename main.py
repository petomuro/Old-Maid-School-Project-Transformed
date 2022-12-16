from game import Game


def start_game():
    print("Rules for Old Maid:")
    print(
        "\tTake turns going around in a circle picking a card from the next player's hand.\n\tIf you get a pair, you reducing the number of cards in your hand.\n\tThe last player left with one card in deck loses the game.")
    print("\n", end="")

    number_of_players = int(input("Please insert how many players are going to play Old Maid (2 - 5): "))

    if 1 < number_of_players < 5:
        game = Game(number_of_players)
        game.welcome_players()
        game.prepare_decks()
        game.start()

    if number_of_players < 2 or number_of_players > 5:
        print("You must choose between 2 - 5 players!")

        start_game()


if __name__ == "__main__":
    start_game()
