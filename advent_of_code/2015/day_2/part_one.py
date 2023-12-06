file = open("input")
data = file.readlines()
file.close()

feet = 0
for dimension in data:
    calc = dimension.split("x")
    areas = []
    for j in range(3):
        areas.append(int(calc[j % 3]) * int(calc[(j + 1) % 3]))
    slack = min(areas)
    for k in range(3):
        feet += areas[k]*2
    feet += slack

print("Wrapping paper:", feet, "feet")  # Wrapping paper: 1586300 feet
