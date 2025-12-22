from typing import List

with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    diagram = [[ch for ch in line] for line in lines]

# iterative
def calculate_beams_split(diagram: List[List[str]]) -> int:
    rows, cols = len(diagram), len(diagram[0])
    t, total_beams_split = 0, 0
    # last time step, recursive base case
    while t < rows:
        if t == rows - 1:
            return total_beams_split
        beam_indexes = [i for i in range(cols) if diagram[t][i] == '|' or diagram[t][i] == 'S']
        # advance forward
        for idx in beam_indexes:
            if diagram[t + 1][idx] == "^": # splitter
                diagram[t + 1][max(0, idx - 1)] = "|"
                diagram[t + 1][min(cols - 1, idx + 1)] = "|"
                total_beams_split += 1
            else:
                diagram[t + 1][idx] = "|" # regular case
        t += 1
    
    return total_beams_split

# recursive
def advance_time_step(diagram: List[List[str]], t: int, total_beams_split: int = 0) -> int:
    rows, cols = len(diagram), len(diagram[0])
    # last time step, recursive base case
    if t == rows - 1:
        return total_beams_split
    beam_indexes = [i for i in range(cols) if diagram[t][i] == '|' or diagram[t][i] == 'S']
    # advance forward
    for idx in beam_indexes:
        if diagram[t + 1][idx] == "^": # splitter
            diagram[t + 1][max(0, idx - 1)] = "|"
            diagram[t + 1][min(cols - 1, idx + 1)] = "|"
            total_beams_split += 1
        else:
            diagram[t + 1][idx] = "|" # regular case
    return advance_time_step(diagram, t + 1, total_beams_split)

print(calculate_beams_split(diagram))
