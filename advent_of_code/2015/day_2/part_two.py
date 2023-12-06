file = open("input")
file_in = file.readlines()
file.close()

total = 0
for i in file_in:
    l, w, h = i[:-1].split("x")
    l, w, h = int(l), int(w), int(h)
    wrap = 2 * min(l + w, w + h, h + l)
    bow = l * w * h
    total += wrap + bow
print("Ribbon: " + str(total) + " feet")
