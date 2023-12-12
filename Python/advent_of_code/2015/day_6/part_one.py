file = open("input")
data = file.readlines()
file.close()

grid = {}

for instruction in data:
    instruction = instruction.split(" ")
    left = instruction[2 - (5 % len(instruction))].split(",")
    right = instruction[4 - (5 % len(instruction))].split(",")

    for i in range(int(left[0]), int(right[0]) + 1):
        for j in range(int(left[1]), int(right[1]) + 1):
            coordinates = str(i) + "_" + str(j)
            if coordinates not in grid:
                grid[coordinates] = False
            if "on" in instruction:
                if not grid[coordinates]:
                    grid[coordinates] = True
            if "off" in instruction:
                if grid[coordinates]:
                    grid[coordinates] = False
            if "toggle" in instruction:
                grid[coordinates] = not grid[coordinates]

lights_lit = sum(grid.values())

print("Lights lit:", lights_lit)  # Lights lit: 569999
