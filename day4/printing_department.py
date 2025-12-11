
def find_rolls_of_paper(file):
    res = 0
    file_object = open(file, "r")
    grid = []
    for line in file_object:
        line = line.strip()
        grid.append(line)
    rows = len(grid)
    cols = len(grid[0])
    # Part 1
    def can_access(r, c):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        count = 0
        for dr, dc in directions:
            new_r = r + dr
            new_c = c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == "@":
                count += 1
                if count > 3:
                    return False
        return True
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@" and can_access(r, c):
                res += 1
            
    file_object.close()
    # print(grid)
    return res

file = "input.txt"
print(find_rolls_of_paper(file))