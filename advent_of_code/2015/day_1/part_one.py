file = open("input")
file_in = file.read()
file.close()

floor = 0
for i in file_in:
    if i == "(":
        floor += 1
    elif i == ")":
        floor -= 1
print("Floor:", floor)
