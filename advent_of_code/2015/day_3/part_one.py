file = open("input")
file_in = file.read()
file.close()

houses = ["0_0"]
x = 0
y = 0
for i in file_in:
    if i == ">":
        x += 1
    elif i == "<":
        x -= 1
    elif i == "^":
        y += 1
    elif i == "v":
        y -= 1
    if str(x) + "_" + str(y) not in houses:
        houses.append(str(x) + "_" + str(y))

print("Houses that received at least one present: " + str(len(houses)))
