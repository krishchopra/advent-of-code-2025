# # part 1
# total_voltage = 0

# with open("input-3.txt", "r") as f:
#     line = f.readline().strip()
#     while line:
#         highest_num = int(line[0])
#         next_num = int(line[1])
#         for i in range(len(line)):
#             if int(line[i]) > highest_num and i < (len(line) - 1):
#                 highest_num = int(line[i])
#                 next_num = int(line[i + 1])
#             elif int(line[i]) > int(next_num):
#                 next_num = int(line[i])

#         num = str(highest_num) + str(next_num)
#         total_voltage += int(num)

#         line = f.readline().strip()

# print(total_voltage)

# part 2
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
