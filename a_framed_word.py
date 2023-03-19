from math import ceil

s = input("Word: ")
pad = (28 - len(s)) / 2
print(f"{'*' * 30}\n*{' ' * int(pad)}{s}{' ' * ceil(pad)}*\n{'*' * 30}")
