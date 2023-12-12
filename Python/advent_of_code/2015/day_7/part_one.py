def findSignalInCircuit(f: list[str], w: str) -> int:
    """
    Finds the signal of a given wire
    :param f: file containing signal and bitwise operation instructions
    :param w: wire identifier
    :return: signal of the wire w
    """
    signals = {}  # key is the identifier of the wire, value is the signal of the wire
    instructions_index = []  # stores the index of the instructions that have already been processed
    index = -1  # index of the file

    while len(instructions_index) != len(f):  # loop until every instruction has been processed
        index = (index + 1) % len(f)  # cycles through every index
        add_to_dictionary = False
        if index not in instructions_index:  # won't process instruction if index already in instruction_index
            wire = f[index].split(" ")
            right = wire[-3]  # identifier of the wire, or signal, to the left of the arrow
            wire_id = wire[-1]  # identifier of the wire to the right of the arrow
            if index != len(f) - 1:  # used to remove newline (\n) character, except for the last line of the file
                wire_id = wire_id[:-1]
            wire_signal = 0

            if len(wire) == 3:  # instructions for no bitwise operations
                if right.isdecimal():  # instructions like 1 -> b
                    wire_signal = int(right)
                    add_to_dictionary = True
                elif right.isalpha() and right in signals:  # instructions like a -> b
                    wire_signal = int(signals[right])
                    add_to_dictionary = True
            elif len(wire) == 4:  # instructions for NOT gates
                if right.isdecimal():  # instructions like NOT 1 -> b
                    wire_signal = ~ int(right)
                    add_to_dictionary = True
                elif right.isalpha() and right in signals:  # instructions like NOT a -> b
                    wire_signal = ~ int(signals[right])
                    add_to_dictionary = True
            elif len(wire) == 5:  # instructions for AND, OR, LSHIFT and RSHIFT gates
                left = wire[0]  # identifier of the wire, or signal, of the leftmost element of the instruction
                if "AND" in wire:
                    if left.isdecimal() and right in signals:  # instructions like 1 AND b -> c
                        wire_signal = int(left) & int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:  # instructions like a AND 1 -> c
                        wire_signal = int(signals[left]) & int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:  # instructions like a AND b -> c
                        wire_signal = int(signals[left]) & int(signals[right])
                        add_to_dictionary = True
                elif "OR" in wire:
                    if left.isdecimal() and right in signals:  # instructions like 1 OR b -> c
                        wire_signal = int(left) | int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:  # instructions like a OR 1 -> c
                        wire_signal = int(signals[left]) | int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:  # instructions like a OR b -> c
                        wire_signal = int(signals[left]) | int(signals[right])
                        add_to_dictionary = True
                elif "LSHIFT" in wire:
                    if left.isdecimal() and right in signals:  # instructions like 1 LSHIFT b -> c
                        wire_signal = int(left) << int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:  # instructions like a LSHIFT 1 -> c
                        wire_signal = int(signals[left]) << int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:  # instructions like a LSHIFT b -> c
                        wire_signal = int(signals[left]) << int(signals[right])
                        add_to_dictionary = True
                elif "RSHIFT" in wire:
                    if left.isdecimal() and right in signals:  # instructions like 1 RSHIFT b -> c
                        wire_signal = int(left) >> int(signals[right])
                        add_to_dictionary = True
                    elif right.isdecimal() and left in signals:  # instructions like a RSHIFT 1 -> c
                        wire_signal = int(signals[left]) >> int(right)
                        add_to_dictionary = True
                    elif left in signals and right in signals:  # instructions like a RSHIFT b -> c
                        wire_signal = int(signals[left]) >> int(signals[right])
                        add_to_dictionary = True

            if add_to_dictionary:  # finalize instruction by storing the identifier and value
                signals[wire_id] = wire_signal
                instructions_index.append(index)

    return signals[w]


if __name__ == "__main__":
    file = open("input")
    data = file.readlines()
    file.close()

    signal_of_wire_a = findSignalInCircuit(data, "a")
    print("Signal of wire 'a':", signal_of_wire_a)  # Signal of wire 'a': 3176
