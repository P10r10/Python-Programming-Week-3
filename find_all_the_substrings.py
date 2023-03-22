word = input("Please type in a word: ")
char = input("Please type in a character: ")
while True:
    idx = word.find(char)
    if idx == -1:
        break
    if (idx + 3) <= len(word):
        print(word[idx: idx + 3])
    word = word[idx + 1:]
