# Part 1
def max_joltage_part1(battery):

    # Helper function
    def find_largest(curr_battery):
        return max(curr_battery), curr_battery.index(max(curr_battery))

    
    largest, largest_idx = find_largest(battery)
    if largest_idx != len(battery) - 1:
        
        next_largest, next_largest_idx = find_largest(battery[largest_idx + 1:])
        return int(largest + next_largest)
    else:
        next_largest, next_largest_idx = find_largest(battery[:largest_idx])
        return int(next_largest + largest)

# Part 2
def max_joltage_part2(battery):
    answer = ""
    for i in range(12, 0, -1):
        largest, largest_idx = next_max_digit(battery, i)
        answer += largest
        battery = battery[largest_idx + 1:]
    return int(answer)

def next_max_digit(battery, remaining_digit_count):
    if len(battery) == remaining_digit_count:
        return battery[0], 0
    largest = max(battery)
    largest_index = battery.index(largest)
    if largest_index <= len(battery) - remaining_digit_count:
        return largest, largest_index
    return next_max_digit(battery[:largest_index], remaining_digit_count - (len(battery) - largest_index))
    

def find_joltage(file):
    file_object = open(file, "r")
    total = 0
    for line in file_object:
        battery = line.strip()
        # print(max_voltage(battery))
        total += max_joltage_part2(battery)
        
    file_object.close()
    return total

file = "input.txt"
print(find_joltage(file))