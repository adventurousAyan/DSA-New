from collections import deque
import random
import abc
from typing import List


class Player:
    def __init__(self, id, player_name):
        self.id = id
        self.player_name = player_name
        self.pos = 0


class Dice:
    def __init__(self, faces):
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)


class Snake:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end


# Snakes:[46, 12],[25,6],[88,76],[74,52]
# Ladders: [73,91],[20,66],[32,53],[67,100]


class Board:
    def __init__(
        self,
        snakes: List[Snake],
        ladders: List[Ladder],
        players: List[Player],
        dice: Dice,
    ):
        self.board = [0] * 100
        self.snakes = snakes
        self.ladders = ladders
        self.players = players
        self.dice = dice
        self.q = deque()
        self.snake_dict = {}
        self.ladder_dict = {}
        self.initialise_board()
        self.initialise_players()

    def initialise_board(self):
        for i in range(0, 100):
            self.board[i] = i + 1

        for snake in self.snakes:
            self.snake_dict[snake.start] = snake.end

        for ladder in self.ladders:
            self.ladder_dict[ladder.start] = ladder.end

    def initialise_players(self):
        for player in self.players:
            self.q.append((player.id, player.pos))

    def show_board(self):
        print(self.board)

    def start_game(self):
        print("Game Started")
        while len(self.q) > 0:
            player, pos = self.q.popleft()
            val = self.dice.roll()
            print(f"Player {player} has rolled dice with value: {val}")
            new_pos = pos + val
            print(f"Player {player} new_position: {new_pos}")
            if new_pos in self.snake_dict:
                new_pos = self.snake_dict[new_pos]
                print(
                    f"Oops encountered a snake. Player {player} going back to {new_pos}"
                )
            elif new_pos in self.ladder_dict:
                new_pos = self.ladder_dict[new_pos]
                print(
                    f"Hurrah encountered a ladder. Player {player} going to {new_pos}"
                )
            if new_pos == 100:
                if len(self.q) > 0:
                    print(f"Player {player} has won the game")
                    break
                else:
                    print(f"Thanks player {player} for finishing the game")
            elif new_pos < 100:
                self.q.append((player, new_pos))
            elif new_pos > 100:
                self.q.append((player, pos))


if __name__ == "__main__":
    snakesList = []
    laddersList = []
    playersList = []

    snakesList.append(Snake(46, 12))
    snakesList.append(Snake(25, 6))
    snakesList.append(Snake(88, 76))
    snakesList.append(Snake(74, 52))

    laddersList.append(Ladder(73, 91))
    laddersList.append(Ladder(20, 66))
    laddersList.append(Ladder(32, 53))
    laddersList.append(Ladder(67, 100))

    playersList.append(Player(1, "Ayan"))
    playersList.append(Player(2, "Debamita"))

    dice = Dice(6)

    board = Board(snakesList, laddersList, playersList, dice)

    board.start_game()
