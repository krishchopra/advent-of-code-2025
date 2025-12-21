with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]

fresh_id_ranges, ids = [], []

for line in lines:
    if "-" in line:
        # add ingredient range
        fresh_id_ranges.append([int(line.strip().split("-")[0]), int(line.strip().split("-")[1])])
    elif len(line) > 0:
        ids.append(int(line.strip()))

def falls_within_range(sorted_combined_ranges, id):
    for start, end in sorted_combined_ranges:
        if (start <= id <= end):
            return True
    return False
        

def find_all_fresh_ids(id_ranges, ids):
    sorted_ranges = sorted(id_ranges, key=lambda r: r[0])
    curr_ptr, next_ptr = 0, 1
    final_ranges = []
    total_fresh_ids = 0

    while curr_ptr < len(sorted_ranges):
        curr_range = sorted_ranges[curr_ptr]
        while True:
            if (next_ptr >= len(sorted_ranges)):
                final_ranges.append(curr_range)
                break
            next_range = sorted_ranges[next_ptr]
            if (next_range[0] <= curr_range[1]):
                curr_range[1] = max(curr_range[1], next_range[1]) # combine intervals
                next_ptr += 1
            else:
                final_ranges.append(curr_range)
                break
        curr_ptr, next_ptr = next_ptr, next_ptr + 1
    
    for id in ids:
        if falls_within_range(final_ranges, id):
           total_fresh_ids += 1 

    print(total_fresh_ids)
    return total_fresh_ids

find_all_fresh_ids(fresh_id_ranges, ids)
# print(f"The total number of fresh ids is {find_all_fresh_ids(fresh_id_ranges, ids)}")
    