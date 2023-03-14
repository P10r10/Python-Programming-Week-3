limit = int(input("Limit: "))
total = 0
increment = 1
res = ""
while total < limit:
    total += increment
    res += str(increment) + " + "
    increment += 1
res = res[:-3]
print(f"The consecutive sum: {res} = {total}")
