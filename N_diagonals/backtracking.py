def diagonals(n, k):
    def pretty_print(board):
        mapping = {0: "O", 1: "\\", 2: "/"}
        for i in range(0, len(board), n):
            print(*[mapping[el] for el in board[i:i+n]])
        print("\n\n")

    def permute(board, rem):
        if len(board) == n**2:
            if rem <= 0:
                print(k+abs(rem))
                pretty_print(board)
            return

        for el in (2, 1, 0):
            board.append(el)
            if is_valid(board):
                permute(board, rem - (el != 0))
            board.pop()

    def is_valid(board):
        last_idx = len(board)-1
        row, col = last_idx//n, last_idx % n
        if board[last_idx] == 0:
            return True

        for drow, dcol in ((-1, 0), (0, -1)):  # cardinal
            nrow, ncol = row + drow, col + dcol
            if nrow < 0 or nrow >= n or ncol < 0 or ncol >= n:
                continue
            nidx = nrow * n + ncol
            if board[nidx] == 0:
                continue
            if board[nidx] != board[last_idx]:
                return False

        for drow, dcol in ((-1, -1), (-1, 1)):  # diagonal
            nrow, ncol = row + drow, col + dcol
            if nrow < 0 or nrow >= n or ncol < 0 or ncol >= n:
                continue
            nidx = nrow * n + ncol
            if board[nidx] == 0:
                continue
            if board[last_idx] == 1:
                if (drow, dcol) == (-1, -1) and board[nidx] == 1:
                    return False
            if board[last_idx] == 2:
                if (drow, dcol) == (-1, 1) and board[nidx] == 2:
                    return False

        return True

    permute([], k)


if __name__ == "__main__":
    diagonals(5, 16)