def find_fresh_ingredients(file):
    fresh_count = 0

    file_object = open(file, "r")
    
    lines =[line.strip() for line in file_object] # input
    blank_index = lines.index("")
    range_lines = lines[:blank_index]
    id_lines = lines[blank_index + 1:]

    ranges = []
    for r in range_lines:
        start, end = map(int, r.split("-"))
        ranges.append([start, end])
    ids = [int(id) for id in id_lines]
    ids.sort()
    ranges.sort(key = lambda pair: pair[0])
    merged_ranges = [ranges[0]]
    for start, end in ranges[1:]:
        if start > merged_ranges[-1][1]:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(end, merged_ranges[-1][1] )

    # Part 1
    # for id in ids:
    #     for start, end in merged_ranges:
    #         if start <= id <= end:
    #             fresh_count += 1
    #             break

    # Part 2:
    for start, end in merged_ranges:
        fresh_count += end - start + 1
    
    # print(ranges)
    # print(merged_ranges)
    # print(ids)
    file_object.close()
    return fresh_count
file = "input.txt"
print(find_fresh_ingredients(file))