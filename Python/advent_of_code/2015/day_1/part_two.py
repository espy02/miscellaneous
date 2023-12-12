file = open("input")
data = file.read()
file.close()

floor = 0
for i in range(len(data)):
    if data[i] == "(":
        floor += 1
    elif data[i] == ")":
        floor -= 1
    if floor == -1:
        print("Position:", i + 1)  # Position: 1783
        break
