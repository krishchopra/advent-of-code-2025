# # part 1
# def has_less_than_four(r, c, grid):
#     how_many_adjacent = 0
#     dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#     for dr, dc in dirs:
#         nr, nc = r + dr, c + dc
#         if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "@":
#             how_many_adjacent += 1
#     if how_many_adjacent < 4:
#         return True
#     return False


# grid = []
# with open("input-4.txt", "r") as f:
#     line = f.readline().strip()
#     while line:
#         grid.append(line)
#         line = f.readline().strip()

# total_rolls = 0
# for row in range(len(grid)):
#     for col in range(len(grid[0])):
#         if grid[row][col] == "@" and has_less_than_four(row, col, grid):
#             total_rolls += 1

# print(total_rolls)

# part 2
def has_less_than_four(r, c, grid):
    how_many_adjacent = 0
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "@":
            how_many_adjacent += 1
    if how_many_adjacent < 4:
        return True
    return False


grid = []
with open("input-4.txt", "r") as f:
    line = f.readline().strip()
    while line:
        grid.append(line)
        line = f.readline().strip()

total_rolls = 0

while True:
    marked = []
    new_grid = []
    curr_rolls = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "@" and has_less_than_four(row, col, grid):
                marked.append((row, col))
                curr_rolls += 1
        
    for row in range(len(grid)):
        new_line = ""
        for col in range(len(grid[0])):
            if (row, col) in marked:
                new_line += '.'
            else:
                new_line += grid[row][col]
        new_grid.append(new_line)

    if curr_rolls == 0:
        break

    total_rolls += curr_rolls
    grid = new_grid


print(total_rolls)
