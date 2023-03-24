nb = int(input("Please type in a number: "))
lst = [i + 1 for i in range(nb)]
for i in range(0, len(lst), 2):
    if (i + 1) < len(lst):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
for n in lst:
    print(n)
