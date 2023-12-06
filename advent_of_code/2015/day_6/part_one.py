file = open("input")
data = file.readlines()
file.close()

grid = {}

for instruction in data:
    action = ""
    through = instruction.find("through")
    left = []
    right = instruction[through + 8:].split(",")
    if instruction.find("on") != -1:
        action = "on"
        left = instruction[8:through - 1].split(",")
    elif instruction.find("off") != -1:
        action = "off"
        left = instruction[9:through - 1].split(",")
    elif instruction.find("toggle") != -1:
        action = "toggle"
        left = instruction[7:through - 1].split(",")

    for i in range(int(left[0]), int(right[0]) + 1):
        for j in range(int(left[1]), int(right[1]) + 1):
            coordinates = str(i) + "_" + str(j)
            if coordinates not in grid:
                grid[coordinates] = False
            if action == "on":
                if not grid[coordinates]:
                    grid[coordinates] = True
            if action == "off":
                if grid[coordinates]:
                    grid[coordinates] = False
            if action == "toggle":
                grid[coordinates] = not grid[coordinates]

lights_lit = 0
for on in grid.values():
    if on:
        lights_lit += 1

print("Lights lit:", lights_lit)  # Lights lit: 569999
