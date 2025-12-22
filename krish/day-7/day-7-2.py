# from collections import deque
from functools import lru_cache

lines = []
with open("input-7.txt", "r") as f:
    for line in f:
        lines.append(line.strip())
start_col = lines[0].index('S')

# bfs approach
# queue = deque() # track (row, col) for each particle/timeline
# queue.append((1, start_col))
# timeline_count = 0

# while queue:
#     r, c = queue.popleft()
#     # out of bounds (left/right)
#     if c < 0 or c >= len(lines[0]):
#         timeline_count += 1
#         continue
    
#     # reached bottom
#     if r >= len(lines):
#         timeline_count += 1
#         continue
    
#     cell = lines[r][c]
#     if cell == '^':
#         queue.append((r + 1, c - 1))
#         queue.append((r + 1, c + 1))
#     else:
#         queue.append((r + 1, c))

# print(timeline_count)


# recursion w/ memoization approach
@lru_cache(maxsize=None)
def count_timelines(r, c):
    # out of bounds (left/right)
    if c < 0 or c >= len(lines[0]):
        return 1

    # reached bottom
    if r >= len(lines):
        return 1

    cell = lines[r][c]
    if cell == '^':
        return count_timelines(r + 1, c - 1) + count_timelines(r + 1, c + 1)
    else:
        return count_timelines(r + 1, c)

print(count_timelines(1, start_col))
