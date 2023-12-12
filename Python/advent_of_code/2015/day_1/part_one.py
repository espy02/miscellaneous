file = open("input")
data = file.read()
file.close()

floor = 0
for p in data:
    if p == "(":
        floor += 1
    elif p == ")":
        floor -= 1

print("Floor:", floor)  # Floor: 232
