str = input("Please type in a string: ")
sub = input("Please type in a substring: ")
idx = str.find(sub, str.find(sub) + len(sub))

if idx != -1:
    print(f"The second occurrence of the substring is at index {idx}.")
else:
    print("The substring does not occur twice in the string.")
