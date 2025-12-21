with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]

grid = [[c for c in line] for line in lines]

def is_accessible(r, c, grid):
    num_adjacent_rolls = 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            if grid[nr][nc] == "@":
                num_adjacent_rolls += 1
    return num_adjacent_rolls < 4

num_accessible_rolls = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == "@" and is_accessible(r, c, grid):
            num_accessible_rolls += 1

print(f"Number of accessible rolls: {num_accessible_rolls}")