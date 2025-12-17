def find_grand_total(file):
    grand_total = 0
    
    
    with open(file, "r") as f:
        lines = f.readlines()
    # Part 1
    # nums =[]
    # for line in lines[:len(lines) - 1]:
    #     nums.append(list(map(int,line.strip().split())))
    # operations = lines[-1].strip().split()
    # rows = len(nums)
    # cols = len(nums[0])
    # import math
    # for c in range(cols):
    #     if operations[c] == "+":
    #         grand_total += sum([nums[r][c] for r in range(rows)])
    #     else:
    #         grand_total += math.prod([nums[r][c] for r in range(rows)])
    
    # Part 2
    import math
    nums2 = []
    for line in lines:
        nums2.append(line.rstrip("\n"))
    # Transpose nums2
    cols = list(zip(*nums2))
    i = 0
    while i < len(cols):
        if all(ch == " " for ch in cols[i]):
            i += 1
            continue
        curr = []
        while i < len(cols) and not all(ch == " " for ch in cols[i]):
            curr.append(cols[i])
            i += 1
        operator = curr[0][-1]
        numbers = []
        for col in curr:
            digits = "".join(c for c in col[:-1] if c != " ")
            if digits:
                numbers.append(int(digits))
        if operator == "+":
            grand_total += sum(numbers)
        else:
            grand_total += math.prod(numbers)
    # print(operations)
    # print(nums2)
    # print(cols)
    return grand_total

file = "input.txt"
print(find_grand_total(file))