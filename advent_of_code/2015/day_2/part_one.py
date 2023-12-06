file = open("input")
file_in = file.readlines()
file.close()

total = 0
for i in file_in:
    calc = i[:-1].split("x")
    areas = []
    for j in range(3):
        areas.append(int(calc[j % 3]) * int(calc[(j + 1) % 3]))
    slack = min(areas)
    for k in range(3):
        total += areas[k]*2
    total += slack
print("Wrapping paper: " + str(total) + " feet")
