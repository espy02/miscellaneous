file = open("input")
file_in = file.readlines()
file.close()

grid = {}

for instruction in file_in:
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
                grid[coordinates] += 1
            if action == "off":
                if grid[coordinates] - 1 >= 0:
                    grid[coordinates] -= 1
                else:
                    grid[coordinates] = 0
            if action == "toggle":
                grid[coordinates] += 2

total_brightness = 0
for brightness in grid.values():
    total_brightness += brightness

print("Total brightness:", total_brightness)
