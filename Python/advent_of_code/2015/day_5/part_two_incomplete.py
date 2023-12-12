ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
tests = ["xyxy", "aabcdefgaa", "aaa", "xyx", "abcdefeghi", "qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg",
         "ieodomkazucvgmuy"]

file = open("input")
file_in = file.readlines()
file.close()

print(file_in)

good_strings = 0

for string in tests:
    #string = string[:-1]
    properties_count = 0
    print(string)

    for i in range(len(ALPHABET)):
        for j in range(len(ALPHABET)):
            if properties_count == 0:
                pair = ALPHABET[i] + ALPHABET[j]
                occurrences = string.count(pair)
                if occurrences >= 2:
                    properties_count += 1

    for a in ALPHABET:
        if properties_count > 0:
            occurrences = string.count(a)
            if occurrences >= 2:
                second = 0
                for p in range(occurrences - 1):
                    first = string.find(a, second)
                    second = string.find(a, first + 1)
                    if second - first > 1:
                        properties_count += 1
                        break
    print(properties_count)

    if properties_count == 2:
        good_strings += 1

print("Good strings: " + str(good_strings))
