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
                grid[coordinates] += 1
            if "off" in instruction:
                if grid[coordinates] - 1 >= 0:
                    grid[coordinates] -= 1
                else:
                    grid[coordinates] = 0
            if "toggle" in instruction:
                grid[coordinates] += 2

total_brightness = sum(grid.values())

print("Total brightness:", total_brightness)  # Total brightness: 17836115
