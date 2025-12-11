# Part 1
def is_invalid(id):
    id_str = str(id)
    part1 = id_str[:len(id_str)//2]
    part2 = id_str[len(id_str)//2:]
    return part1 == part2
# Part 2
def is_invalid_v2(id):
    s = str(id)
    n = len(s)
    
    # pattern length must divide n
    for k in range(1, n // 2 + 1):
        if n % k == 0: 
            pattern = s[:k]
            if pattern * (n // k) == s:
                return True
    return False


def invalid_ids_sum(file):
    file_object = open(file, "r")
    total = 0
    input = file_object.read().strip()
    range_list = input.split(",")
    print(range_list)
    for part in range_list:
        start_strs, end_strs = part.strip().split("-")
        start = int(start_strs)
        end = int(end_strs)
        for id in range(start, end + 1):
            # part 1
            # if len(str(id)) % 2 == 1:
            #     continue
            if is_invalid_v2(id):
                print(id)
                total += id
       
        
    file_object.close()
    return total

file = "input.txt"
print(invalid_ids_sum(file))