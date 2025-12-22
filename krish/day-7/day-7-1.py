lines = []
with open("input-7.txt", "r") as f:
    line = f.readline().strip()
    while line:
        lines.append(line)
        line = f.readline().strip()

line2 = ""
for i in range(len(lines[0])):
    if lines[0][i] == 'S':
        line2 += '|'
    else:
        line2 += lines[1][i]
lines[1] = line2

def process_line(grid, line_idx):
    count_split = 0
    new_line = [c for c in grid[line_idx]]
    for i in range(len(grid[line_idx])):
        if grid[line_idx][i] == '^' and grid[line_idx - 1][i] == '|':
            if (i - 1) >= 0:
                new_line[i - 1] = '|'
            if (i + 1) < len(new_line):
                new_line[i + 1] = '|'
            count_split += 1
        elif grid[line_idx][i] == '.' and grid[line_idx - 1][i] == '|':
            new_line[i] = '|'
    return ("".join(new_line), count_split)

split_count = 0
for r in range(2, len(lines)):
    lines[r], split_count = process_line(lines, r)[0], split_count + process_line(lines, r)[1]

print(split_count)
