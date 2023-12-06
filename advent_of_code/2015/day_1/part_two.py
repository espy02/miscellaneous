file = open("input")
file_in = file.read()
file.close()

floor = 0
for i in range(len(file_in)):
    if file_in[i] == "(":
        floor += 1
    elif file_in[i] == ")":
        floor -= 1
    if floor == -1:
        print("Position:", (i + 1))
        break
