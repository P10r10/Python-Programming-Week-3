word = input("Please type in a word: ")
char = input("Please type in a character: ")
idx = word.find(char)
if (idx + 3) <= len(word):
    print(word[idx: idx + 3])
