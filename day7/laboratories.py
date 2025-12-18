def count_splits(file):
    splits = 0
    with open(file, "r") as f:
        lines = f.readlines()
    
    grid = []
    for line in lines:
        grid.append(list(line.strip()))
    rows = len(grid)
    cols = len(grid[0])
    # Part 1
    for r in range(rows - 1):
        for c in range(cols):
            if grid[r][c] == "S":
                grid[r + 1][c] = "|"
                continue
            elif grid[r][c] == "|":
                if grid[r + 1][c] != "^":
                    grid[r+1][c] = "|"
                else:
                    splits += 1
                    grid[r + 1][c - 1] = "|"
                    grid[r + 1][c + 1] = "|"
    # Part 2
    count = 0
    start_r = 0
    start_c = grid[start_r].index("S")
    path = {}
    def dfs(r, c, path):
        if r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if r == rows - 1:
            return 1
        if (r, c) in path:
            return path[(r ,c)]
        if grid[r][c] == "^":
            curr = dfs(r + 1, c + 1, path) + dfs(r + 1, c - 1, path)
        else:
            curr = dfs(r+ 1, c, path)
        path[(r, c)] = curr
        return curr
    for r in range(rows):
        print("".join(grid[r]))
    # Part 1
    # return splits
    # Part 2
    return dfs(start_r, start_c, path)

file = "input.txt"
print(count_splits(file))