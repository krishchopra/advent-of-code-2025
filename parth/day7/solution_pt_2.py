from typing import List
from collections import deque

with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    diagram = [[ch for ch in line] for line in lines]

# bfs, times out
def calculate_total_timelines_bfs(diagram: List[List[str]]) -> int:
    rows, cols = len(diagram), len(diagram[0])
    initial_idx = [i for i in range(cols) if diagram[0][i] == 'S']
    total_timelines = 0
    queue = deque([(0, initial_idx[0])]) # tuple of (timestamp, idx)

    while queue:
        t, idx = queue.popleft()
        # reached the end
        if t == rows - 1:
            total_timelines += 1
            continue

        if diagram[t + 1][idx] == "^":
            if idx - 1 >= 0:
                queue.append((t + 1, idx - 1)) # left timeline
            if idx + 1 < cols:
                queue.append((t + 1, idx + 1)) # right timeline
        else:
            queue.append((t + 1, idx))
    
    return total_timelines

# dp approach
def calculate_total_timelines_dp(diagram: List[List[str]]) -> int:
    rows, cols = len(diagram), len(diagram[0])
    initial_idx = [i for i in range(cols) if diagram[0][i] == 'S']
    counts = [0 for _ in range(cols)] # similar to fibonacci approach
    counts[initial_idx[0]] = 1

    for r in range(rows - 1):
        next_counts = [0 for _ in range(cols)]
        next_row = diagram[r + 1]

        for idx, num_ways in enumerate(counts):
            if num_ways == 0:
                continue
            elif next_row[idx] == "^":
                if idx > 0:
                    next_counts[idx - 1] += num_ways
                if idx + 1 < cols:
                    next_counts[idx + 1] += num_ways
            else:
                next_counts[idx] += num_ways
        
        counts = next_counts
    
    return sum(counts)

print(calculate_total_timelines_dp(diagram))