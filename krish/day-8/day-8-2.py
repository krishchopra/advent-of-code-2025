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


parent = {box: box for box in lines}
rank = {box: 0 for box in lines}


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    px, py = find(x), find(y)
    if px == py:
        return
    if rank[px] < rank[py]:
        parent[px] = py
    elif rank[px] > rank[py]:
        parent[py] = px
    else:
        parent[py] = px
        rank[px] += 1


all_pairs = []
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        dist = calc_distance(lines[i], lines[j])
        all_pairs.append((dist, lines[i], lines[j]))

all_pairs.sort(key=lambda x: x[0])

x_coords = []
for i in range(len(all_pairs)):
    _, box1, box2 = all_pairs[i]
    union(box1, box2)

    parents = set()
    for c in parent.keys():
        parents.add(find(c))
    if len(parents) == 1:
        x_coords.append(box1)
        x_coords.append(box2)
        break

result = x_coords[0][0] * x_coords[1][0]
print(result)
