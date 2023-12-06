VOWELS = ["a", "e", "i", "o", "u"]
ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
BAD_STRINGS = ["ab", "cd", "pq", "xy"]

file = open("input")
file_in = file.readlines()
file.close()

good_strings = 0

for string in file_in:
    properties_count = 0
    vowel_count = 0

    for v in VOWELS:
        vowel_count += string.count(v)
        if vowel_count >= 3:
            properties_count += 1
            break

    for c in ALPHABET:
        if string.count(c * 2):
            properties_count += 1
            break

    for bs in BAD_STRINGS:
        if string.count(bs):
            properties_count -= 1
            break

    if properties_count == 2:
        good_strings += 1

print("Good strings: " + str(good_strings))
