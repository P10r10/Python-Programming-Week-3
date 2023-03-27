def _row(is_one, size):
    for _ in range(size):
        print("1" if is_one else "0", end="")
        is_one ^= True


def chessboard(n):
    is_one = True
    for _ in range(n):
        _row(is_one, n)
        is_one ^= True
        print()


if __name__ == "__main__":
    chessboard(8)