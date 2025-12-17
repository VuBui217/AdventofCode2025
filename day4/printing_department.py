
def find_rolls_of_paper(file):
    res = 0
    file_object = open(file, "r")
    grid = []
    for line in file_object:
        line = line.strip()
        grid.append(list(line))
    rows = len(grid)
    cols = len(grid[0])
    # Part 1
    directions = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i != 0 or j != 0:
                directions.append((i, j))
    print(directions)
    def is_roll(current_position, direction):
        if 0 <= (current_position[0] + direction[0]) < rows and 0 <= (current_position[1] + direction[1]) < cols and grid[current_position[0] + direction[0]][current_position[1] + direction[1]] == "@":
            return True
        else:
            return False
    
    def roll_count(current_position):
        return sum([is_roll(current_position, direction) for direction in directions])
    # Part 1
    # for r in range(rows):
    #     for c in range(cols):

    #         if grid[r][c] == "@" and roll_count((r,c)) < 4:
    #             res += 1

    # Part 2
    while True:
        to_remove = []
        curr = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@" and roll_count((r, c)) < 4:
                    # to_remove.append((r, c)) 
                    curr += 1
                    grid[r][c] = "."

        if curr == 0:
            break
        else:
            res += curr
        # if not to_remove:
        #     break
        # for r, c in to_remove:
        #     grid[r][c] = "."
        # res += len(to_remove)
    file_object.close()
    # print(grid)
    return res

file = "input.txt"
print(find_rolls_of_paper(file))