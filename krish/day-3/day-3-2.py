total_voltage = 0

with open("input-3.txt", "r") as f:
    line = f.readline().strip()
    while line:
        curr_num = ""
        start_idx = 0

        for digits_left in range(12, 0, -1):
            max_digit = -1
            max_pos = start_idx
            for i in range(start_idx, len(line) - digits_left + 1):
                if int(line[i]) > max_digit:
                    max_digit = int(line[i])
                    max_pos = i

            curr_num += str(max_digit)
            start_idx = max_pos + 1

        total_voltage += int(curr_num)

        line = f.readline().strip()

print(total_voltage)
