# # part 1
# def is_repeating(stri):
#     length = len(stri)
#     if length % 2 != 0:
#         return False

#     halfway = length // 2
#     first_half = stri[0:halfway]
#     second_half = stri[halfway:]
#     if first_half == second_half:
#         return True
#     else:
#         return False


# sum = 0
# with open("input-2.txt", "r") as f:
#     line = f.readline().strip()
#     ranges = line.split(",")

#     for rg in ranges:
#         num1, num2 = "", ""
#         rge = rg.strip()
#         breakpoint = 0
#         for i in range(len(rge)):
#             if rge[i] != "-":
#                 num1 += rge[i]
#             else:
#                 breakpoint = i
#                 break
#         for i in range(breakpoint + 1, len(rge)):
#             num2 += rge[i]

#         for num in range(int(num1), int(num2) + 1):
#             if is_repeating(str(num)):
#                 sum += int(num)

# print(sum)

# part 2

# got this from the the broski!
def can_be_sliced_equally(piece, whole):
    if (len(whole) % len(piece)) != 0:
        return False
    times = len(whole) // len(piece)
    return piece * times == whole


def is_invalid(num):
    num_str = str(num)
    for i in range(1, len(num_str)):
        part = num_str[:i]
        if can_be_sliced_equally(part, num_str):
            return True
    return False


sum = 0
with open("input-2.txt", "r") as f:
    line = f.readline().strip()
    ranges = line.split(",")

    for rg in ranges:
        num1, num2 = "", ""
        rge = rg.strip()
        breakpoint = 0
        for i in range(len(rge)):
            if rge[i] != "-":
                num1 += rge[i]
            else:
                breakpoint = i
                break
        for i in range(breakpoint + 1, len(rge)):
            num2 += rge[i]

        for num in range(int(num1), int(num2) + 1):
            if is_invalid(str(num)):
                sum += int(num)

print(sum)
