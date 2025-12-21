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

def remove_accessible_rows_and_return_count(grid):
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "@" and is_accessible(r, c, grid):
                grid[r][c] = "."
                count += 1
    return (grid, count)

def remove_all_accessible_rolls(grid):
    total_count = 0
    num_rolls_recently_removed = float('inf')
    while num_rolls_recently_removed > 0:
        grid, count = remove_accessible_rows_and_return_count(grid)
        total_count += count
        num_rolls_recently_removed = count
    return total_count

total_removable_rolls = remove_all_accessible_rolls(grid)

print(f"Number of removable rolls: {total_removable_rolls}")