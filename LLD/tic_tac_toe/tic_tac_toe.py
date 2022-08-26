from collections import deque


class Player:
    def __init__(self, id, sym):
        self.id = id
        # self.player_name = player_name
        self.sym = sym


class Board:
    def __init__(self, players, row, col):
        self.board = [[" "] * ((2 * col) - 1) for _ in range((2 * row) - 1)]
        self.row = row
        self.col = col
        self.posmap = {}
        self.players = players
        self.q = deque()
        self.initialise_board(row, col)
        self.initialise_players()

    def initialise_board(self, row, col):
        m, n = (2 * row) - 1, (2 * col) - 1

        self.posmap[0] = 0
        self.posmap[1] = 2
        self.posmap[2] = 4

        for i in range(m):
            for j in range(n):
                if j % 2 != 0 and i % 2 == 0:
                    self.board[i][j] = "|"
                if j % 2 == 0 and i % 2 != 0:
                    self.board[i][j] = "-"
                if j % 2 != 0 and i % 2 != 0:
                    self.board[i][j] = "+"

    def display_board(self):
        m, n = (2 * self.row) - 1, (2 * self.col) - 1

        for i in range(m):
            print("")
            for j in range(n):
                print(self.board[i][j], end="")

        print("")

    def initialise_players(self):
        for player in self.players:
            self.q.append((player.id, player.sym))

    def start_game(self):

        print("Game Started")

        while True:
            player, sym = self.q.popleft()
            row, col = input(f"Player {player} please enter position: ")
            row, col = int(row), int(col)
            r, c = self.posmap[row], self.posmap[col]
            while not self.is_valid(r, c):
                row, col = input(
                    f"Position not valid. Player {player} please re-enter position:"
                )
                row, col = int(row), int(col)
                print(f"Position entered is: ({row},{col})")
                r, c = self.posmap[row], self.posmap[col]
                print(
                    f"Actual position in grid: ({self.posmap[row]},{self.posmap[col]})"
                )

            self.board[r][c] = sym
            self.display_board()
            if self.validate_symbol(r, c, sym):
                print(f"Player {player} has won the game")
                break
            else:
                self.q.append((player, sym))

    def is_valid(self, r, c):
        m, n = (2 * self.row) - 1, (2 * self.col) - 1
        return r >= 0 and r < m and c >= 0 and c < n and self.board[r][c] == " "

    def validate_symbol(self, r, c, sym):
        m, n = (2 * self.row) - 1, (2 * self.col) - 1

        cnt = 0
        for i in range(m):
            if self.board[i][c] == sym:
                cnt += 1
            if cnt == self.row:
                return True
        cnt = 0
        for j in range(n):
            if self.board[r][j] == sym:
                cnt += 1
            if cnt == self.col:
                return True

        cnt = 0
        for i in range(m):
            for j in range(n):
                if i == j and self.board[r][j] == sym:
                    cnt += 1
                if cnt == self.col:
                    return True

        cnt = 0
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i == j and self.board[r][j] == sym:
                    cnt += 1
                if cnt == self.col:
                    return True


if __name__ == "__main__":
    playersList = []
    playersList.append(Player(1, "X"))
    playersList.append(Player(2, "O"))
    b = Board(playersList, 3, 3)
    b.start_game()

    # b.display_board()
