ranges = []
numbers = []
with open("input-5.txt", "r") as f:
    line = f.readline().strip()
    while line:
        rgee = line.split("-")
        rge = (rgee[0], rgee[1])
        ranges.append(rge)
        line = f.readline().strip()
    
    line = f.readline().strip()
    while line:
        numbers.append(line)
        line = f.readline().strip()

fresh_count = 0
for num in numbers:
    for start, end in ranges:
        if int(num) >= int(start) and int(num) <= int(end):
            fresh_count += 1
            break

print(fresh_count)
