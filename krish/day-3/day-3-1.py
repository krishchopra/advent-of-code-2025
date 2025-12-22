total_voltage = 0

with open("input-3.txt", "r") as f:
    line = f.readline().strip()
    while line:
        highest_num = int(line[0])
        next_num = int(line[1])
        for i in range(len(line)):
            if int(line[i]) > highest_num and i < (len(line) - 1):
                highest_num = int(line[i])
                next_num = int(line[i + 1])
            elif int(line[i]) > int(next_num):
                next_num = int(line[i])

        num = str(highest_num) + str(next_num)
        total_voltage += int(num)

        line = f.readline().strip()

print(total_voltage)
