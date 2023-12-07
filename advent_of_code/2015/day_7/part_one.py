def findSignalInCircuit(d, w):
    signals = {}
    instructions_index = []
    index = -1

    while len(instructions_index) != len(d):
        index = (index + 1) % len(d)
        add_to_dictionary = False
        if index not in instructions_index:
            wire = d[index].split(" ")
            right = wire[-3]
            wire_id = wire[-1]
            if index != len(d) - 1:
                wire_id = wire_id[:-1]
            wire_signal = 0

            if len(wire) == 3:
                if right.isdecimal():
                    wire_signal = int(right)
                    add_to_dictionary = True
                elif right.isalpha() and right in signals:
                    wire_signal = int(signals[right])
                    add_to_dictionary = True
            elif len(wire) == 4:
                if right.isdecimal():
                    wire_signal = ~ int(right)
                    add_to_dictionary = True
                elif right.isalpha() and right in signals:
                    wire_signal = ~ int(signals[right])
                    add_to_dictionary = True
            elif len(wire) == 5:
                left = wire[0]
                if "AND" in wire:
                    if left.isdecimal() and right in signals:
                        wire_signal = int(left) & int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:
                        wire_signal = int(signals[left]) & int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:
                        wire_signal = int(signals[left]) & int(signals[right])
                        add_to_dictionary = True
                elif "OR" in wire:
                    if left.isdecimal() and right in signals:
                        wire_signal = int(left) | int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:
                        wire_signal = int(signals[left]) | int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:
                        wire_signal = int(signals[left]) | int(signals[right])
                        add_to_dictionary = True
                elif "LSHIFT" in wire:
                    if left.isdecimal() and right in signals:
                        wire_signal = int(left) << int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:
                        wire_signal = int(signals[left]) << int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:
                        wire_signal = int(signals[left]) << int(signals[right])
                        add_to_dictionary = True
                elif "RSHIFT" in wire:
                    if left.isdecimal() and right in signals:
                        wire_signal = int(left) >> int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:
                        wire_signal = int(signals[left]) >> int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:
                        wire_signal = int(signals[left]) >> int(signals[right])
                        add_to_dictionary = True

            if add_to_dictionary:
                signals[wire_id] = wire_signal
                instructions_index.append(index)

    return signals[w]


if __name__ == "__main__":
    file = open("input")
    data = file.readlines()
    file.close()

    signal_of_wire_a = findSignalInCircuit(data, "a")
    print("Signal of wire 'a':", signal_of_wire_a)  # Signal of wire 'a': 3176
