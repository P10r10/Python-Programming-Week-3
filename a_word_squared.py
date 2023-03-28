def squared(s, side):
    idx = 0
    for _ in range(side):
        for _ in range(side):
            print(s[idx % len(s)], end="")
            idx += 1
        print()


if __name__ == "__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)
