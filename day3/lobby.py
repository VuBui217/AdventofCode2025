def max_joltage(battery):
    res = 0
    for i in range(len(battery) - 1):
        for j in range(i + 1, len(battery)):
            res = max(res, int(battery[i] + battery[j]))
    return res
def find_joltage(file):
    file_object = open(file, "r")
    total = 0
    for line in file_object:
        battery = line.strip()
        total += max_joltage(battery)
        print(battery)
    file_object.close()
    return total

file = "input.txt"
print(find_joltage(file))