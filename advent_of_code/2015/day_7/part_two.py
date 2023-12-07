from part_one import findSignalInCircuit

file = open("input")
data = file.readlines()
file.close()

signal_of_wire_b = findSignalInCircuit(data, "a")
data[3] = str(signal_of_wire_b) + " -> b\n"
signal_of_wire_a = findSignalInCircuit(data, "a")
print("Signal of wire 'a':", signal_of_wire_a)  # Signal of wire 'a': 14710
