ranges = []
with open("input-5.txt", "r") as f:
    line = f.readline().strip()
    while line:
        rgee = line.split("-")
        rge = [int(rgee[0]), int(rgee[1])]
        ranges.append(rge)
        line = f.readline().strip()

ranges.sort(key=lambda x: x[0])
intervals = [ranges[0]]
for start, end in ranges[1:]:
    if int(start) <= int(intervals[-1][1]):
        intervals[-1][1] = max(int(end), intervals[-1][1])
    else:
        intervals.append([int(start), int(end)])

fresh_ids_count = 0
for start, end in intervals:
    fresh_ids_count += end - start + 1

print(fresh_ids_count)
