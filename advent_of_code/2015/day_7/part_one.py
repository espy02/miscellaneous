file = open("input")  # What a mess, need to optimize this
data = file.readlines()
file.close()

signals = {}
instructions_index = []
index = -1

while len(instructions_index) != len(data):
    index = (index + 1) % len(data)

    if index not in instructions_index:
        wire = data[index].split(" ")
        if index != len(data) - 1:
            wire[-1] = wire[-1][:-1]
        if "AND" in wire:
            left = wire[0]
            right = wire[2]
            wire_id = wire[4]
            wire_signal = 0
            if left.isdecimal() and right in signals:
                wire_signal = int(left) & signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isdecimal() and left in signals:
                wire_signal = signals[left] & int(right)
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isalpha() and left in signals and right in signals:
                wire_signal = signals[left] & signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
        elif "OR" in wire:
            left = wire[0]
            right = wire[2]
            wire_id = wire[4]
            wire_signal = 0
            if left.isdecimal() and right in signals:
                wire_signal = int(left) | signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isdecimal() and left in signals:
                wire_signal = signals[left] | int(right)
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isalpha() and left in signals and right in signals:
                wire_signal = signals[left] | signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
        elif "NOT" in wire:
            left = wire[1]
            wire_id = wire[3]
            if left in signals:
                wire_signal = ~ signals[left]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
        elif "LSHIFT" in wire:
            left = wire[0]
            right = wire[2]
            wire_id = wire[4]
            wire_signal = 0
            if left.isdecimal() and right in signals:
                wire_signal = int(left) << signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            if right.isdecimal() and left in signals:
                wire_signal = signals[left] << int(right)
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isalpha() and left in signals and right in signals:
                wire_signal = signals[left] << signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
        elif "RSHIFT" in wire:
            left = wire[0]
            right = wire[2]
            wire_id = wire[4]
            wire_signal = 0
            if left.isdecimal() and right in signals:
                wire_signal = int(left) >> signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            if right.isdecimal() and left in signals:
                wire_signal = signals[left] >> int(right)
                signals[wire_id] = wire_signal
                instructions_index.append(index)
            elif right.isalpha() and left in signals and right in signals:
                wire_signal = signals[left] >> signals[right]
                signals[wire_id] = wire_signal
                instructions_index.append(index)
        elif wire[0].isalpha() and wire[0] in signals:
            wire_id = wire[2]
            wire_signal = signals[wire[0]]
            signals[wire_id] = int(wire_signal)
            instructions_index.append(index)
        elif wire[0].isdecimal():
            wire_id = wire[2]
            wire_signal = int(wire[0])
            signals[wire_id] = wire_signal
            instructions_index.append(index)

wire_a_signal = signals["a"]
print("Signal of wire 'a':", wire_a_signal)  # Signal of wire 'a': 3176
