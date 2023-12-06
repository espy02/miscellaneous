file = open("input")
data = file.readlines()
file.close()

feet = 0
for dimension in data:
    l, w, h = dimension[:-1].split("x")
    l, w, h = int(l), int(w), int(h)
    wrap = 2 * min(l + w, w + h, h + l)
    bow = l * w * h
    feet += wrap + bow

print("Ribbon:", feet, "feet")  # Ribbon: 3737498 feet
