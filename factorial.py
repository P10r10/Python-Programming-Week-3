def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


while True:
    nb = int(input("Please type in a number: "))
    if nb <= 0:
        break
    print(f"The factorial of the number {nb} is {factorial(nb)}")
print("Thanks and bye!")
