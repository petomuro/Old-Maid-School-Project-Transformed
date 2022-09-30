import random


class Player:
    def __init__(self, number):
        self.player = number

    def print_player(self):
        print("*************************Welcome in Game - Old Maid!*************************")
        print("Players: (", self.player, ")")


class Game:
    def __init__(self, number):
        self.number = number
        self.ptr = []
        self.deck0 = []
        self.deck1 = []

    def decks(self):
        if self.number == 2:
            for index in range(self.number):
                self.ptr.append(index + 16)

            for i in range(self.ptr[0]):
                self.deck0.append(i + 1)

            random.shuffle(self.deck0)

            for i in range(self.ptr[1]):
                self.deck1.append(i + 1)

            random.shuffle(self.deck1)

    def print_cards(self):
        if self.number == 2:
            print("Player's 1 deck: ")

            for i in range(self.ptr[0]):
                # print(self.deck0[i], end=" ")
                print("#, ", end=" ")

            print("\n")
            print("Player' 2 deck: ")

            for i in range(self.ptr[1]):
                # print(self.deck1[i], end=" ")
                print("#, ", end=" ")

    def game_start(self):
        if self.number == 2:
            while True:
                self.print_cards()

                print("\n")
                print("It's Player 1 turn")
                print("Which index do you want to turn?")
                print("You can turn card within the range with index 0 - ", self.ptr[1] - 1)

                first_player_turn = int(input())

                print("You turned card: ", self.deck1[first_player_turn], " from index: ", first_player_turn)

                for i in range(self.ptr[0]):
                    if self.deck1[first_player_turn] == self.deck0[i]:
                        self.deck0[i] = 0

                        swap(self.deck0, i, self.ptr[0] - 1)

                        self.ptr[0] -= 1
                        self.deck1[first_player_turn] = 0

                        swap(self.deck1, first_player_turn, self.ptr[1] - 1)

                        self.ptr[1] -= 1

                        print("Cards missing: ", self.ptr[0])

                        break

                    elif self.deck1[first_player_turn] == 17:
                        self.ptr[0] += 1
                        self.deck1[first_player_turn] = 0
                        self.deck0[self.ptr[0] - 1] = 17

                        swap(self.deck1, first_player_turn, self.ptr[1] - 1)

                        self.ptr[1] -= 1

                        print("Cards missing: ", self.ptr[0])

                        break

                print("\n")

                if (self.ptr[0] == 1):
                    print("Winner is P1 and P2 is old maid!")

                    break
                elif (self.ptr[1] == 1):
                    print("Winner is P2 and P1 is old maid!")

                    break

                print("It's Player 2 turn")
                print("Which index do you want to turn?")
                print("You can turn card within the range with index 0 - ", self.ptr[0] - 1)

                second_player_turn = int(input())

                print("You turned card: ", self.deck0[second_player_turn], " from index: ", second_player_turn)

                for i in range(self.ptr[1]):
                    if self.deck0[second_player_turn] == self.deck1[i]:
                        self.deck1[i] = 0

                        swap(self.deck1, i, self.ptr[1] - 1)

                        self.ptr[1] -= 1
                        self.deck0[second_player_turn] = 0

                        swap(self.deck0, second_player_turn, self.ptr[0] - 1)

                        self.ptr[0] -= 1

                        print("Cards missing: ", self.ptr[1])

                        break

                    elif self.deck0[second_player_turn] == 17:
                        self.ptr[1] += 1
                        self.deck0[second_player_turn] = 0
                        self.deck1[self.ptr[1] - 1] = 17

                        swap(self.deck0, second_player_turn, self.ptr[0] - 1)

                        self.ptr[0] -= 1

                        print("Cards missing: ", self.ptr[1])

                        break

                print("\n")

                if (self.ptr[0] == 1):
                    print("Winner is P1 and P2 is old maid!")

                    break
                elif (self.ptr[1] == 1):
                    print("Winner is P2 and P1 is old maid!")

                    break


def swap(array, pos1, pos2):
    array[pos1], array[pos2] = array[pos2], array[pos1]

    return array


def rule():
    print("Rules for Old Maid:")
    print("Take turns going around in a circle picking a card from the next player's hand.\nIf you get a pair, you"
          "reducing the number of cards in your hand.\nThe last player left with the number of 17 loses the game.")


def main_program(how_many_of_players):
    while True:
        if how_many_of_players > 2 or how_many_of_players < 5:
            players = Player(how_many_of_players)
            players.print_player()

            game = Game(how_many_of_players)
            game.decks()
            game.game_start()

        if how_many_of_players < 2 or how_many_of_players > 5:
            print("You must choose between 2 - 5 players!")

            break


if __name__ == "__main__":
    rule()
    how_many_of_players = int(
        input(
            "Please insert how many players are going to play Old Maid(2 - 5): "))

    main_program(how_many_of_players)
