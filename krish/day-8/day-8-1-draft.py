import math

lines = []
with open("input-8.txt", "r") as f:
    for line in f:
        li = line.strip().split(",")
        for i in range(len(li)):
            li[i] = int(li[i])
        li = tuple(li)
        lines.append(li)


def calc_distance(arr1, arr2):
    x1, y1, z1 = arr1
    x2, y2, z2 = arr2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


# def merge_arrs(arrs):
#     new_arrs = []
#     for i in range(len(arrs)):
#         for j in range(len(arrs[i])):
#             temp = set()
#             if (i + 1) < len(arrs) and j in arrs[i + 1]:
#                 temp.add(arrs[i + 1][0])
#                 temp.add(arrs[i + 1][1])
#                 temp.add(arrs[i][0])
#                 temp.add(arrs[i][1])
#                 for x in temp:
#                     new_arrs.append(temp)
#     return new_arrs


def merge_arrs(arrs):
    result = []
    for s in arrs:
        s = set(s)
        for t in result:
            if t & s:
                t.update(s)
                break
        else:
            result.append(s)
    return result


# for i in range(len(lines)):
#     for j in range(len(lines[i])):
#         lines[i][j] = int(lines[i][j])

shortest_matches = []
for n in range(10):
    curr_shortest_match = []
    shortest_dist = float("inf")
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i != j:
                dist = calc_distance(lines[i], lines[j])
                if (
                    dist <= shortest_dist
                    and [lines[i], lines[j]] not in shortest_matches
                    and [lines[j], lines[i]] not in shortest_matches
                ):
                    shortest_dist = dist
                    curr_shortest_match = [lines[i], lines[j]]
    shortest_matches.append(curr_shortest_match)

merged_shortest_matches = merge_arrs(shortest_matches)
merged_shortest_matches.sort(key=len, reverse=True)
print(merged_shortest_matches)
result = (
    len(merged_shortest_matches[0])
    * len(merged_shortest_matches[1])
    * len(merged_shortest_matches[2])
)
print(result)
