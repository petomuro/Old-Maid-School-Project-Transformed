import random


class Game:
    def __init__(self, number_of_players):
        self.current_player_index = 0
        self.decks = []
        self.number_of_cards = []
        self.number_of_players = number_of_players
        self.total_cards = 33

    def welcome_players(self):
        print("\n", end="")
        print("*************************Welcome in Game - Old Maid!*************************")
        print(f"Number of players: {self.number_of_players}")

    def prepare_decks(self):
        old_maid = random.randint(0, self.number_of_players - 1)

        for index in range(self.number_of_players):
            self.number_of_cards.append(round(self.total_cards / self.number_of_players))

        self.number_of_cards[old_maid] += 1

        for i in range(len(self.number_of_cards)):
            self.decks.append([])

            for j in range(self.number_of_cards[i]):
                self.decks[i].append(j)

            random.shuffle(self.decks[i])

    def show_decks(self):
        print("\n", end="")

        for i in range(self.number_of_players):
            print(f"Player's {i} deck:")

            for j in range(len(self.decks[i])):
                print("#, ", end="")
                # print(f"{self.decks[i][j]}, ", end="")

            print("\n\n", end="")

    def bad_index(self, player_turn):
        print("\n", end="")
        print(
            f"Card at index {player_turn} doesn't exist! You need to turn card within the range with index 0 - {len(self.decks[0]) - 1}!")
        print("\n", end="")

    def draw_a_card(self, new_round):
        next_player_index = 0 if new_round else self.current_player_index + 1

        print(f"You can turn card within the range with index 0 - {len(self.decks[next_player_index]) - 1}")

        player_turn = int(input())

        try:
            print(f"You turned card: {self.decks[next_player_index][player_turn]} from index: {player_turn}")

            if self.decks[next_player_index][player_turn] not in self.decks[self.current_player_index]:
                self.decks[self.current_player_index].append(self.decks[next_player_index][player_turn])
                self.decks[next_player_index].pop(player_turn)
            else:
                self.decks[self.current_player_index].pop(
                    self.decks[self.current_player_index].index(self.decks[next_player_index][player_turn]))
                self.decks[next_player_index].pop(player_turn)

            random.shuffle(self.decks[self.current_player_index])
            random.shuffle(self.decks[next_player_index])

            print("\n", end="")

            self.show_decks()

            if new_round:
                self.current_player_index = 0
            else:
                self.current_player_index += 1
        except IndexError:
            self.bad_index(player_turn)

    def check_for_winner(self):
        for i in range(self.number_of_players):
            if len(self.decks[i]) < 1:
                print(f"Winner is Player {i}")

                return True

    def start(self):
        self.show_decks()

        while True:
            print(f"It's Player {self.current_player_index} turn")
            print("Which index do you want to turn?")

            if self.current_player_index >= self.number_of_players - 1:
                self.draw_a_card(True)
            else:
                self.draw_a_card(False)

            if self.check_for_winner():
                break
