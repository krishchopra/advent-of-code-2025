def is_repeating(stri):
    length = len(stri)
    if length % 2 != 0:
        return False

    halfway = length // 2
    first_half = stri[0:halfway]
    second_half = stri[halfway:]
    if first_half == second_half:
        return True
    else:
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
            if is_repeating(str(num)):
                sum += int(num)

print(sum)
