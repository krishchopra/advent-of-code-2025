with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]

max_length = max(len(line) for line in lines)
ptr = max_length - 1
numbers, operator = [], ""
total = 0

def perform_calculation(numbers, operator):
    total = 0 if operator == "+" else 1
    for num in numbers:
        if operator == "*":
            total *= int(num)
        else:
            total += int(num)
    return total

# work backwards:
while True:
    is_line_break = all(line[ptr] == ' ' for line in lines) or ptr < 0
    if is_line_break:
        total += perform_calculation(numbers, operator)
        # reset numbers and operator
        numbers, operator = [], ""
        # break once we've exhausted entire file
        if ptr < 0:
            break
    else:
        digits = []
        for line in lines:
            char = line[ptr]
            if char != ' ':
                if char == "*" or char == "+":
                    operator = char
                else:
                    digits.append(char)
        numbers.append(int(''.join(digits)))
    ptr -= 1

print(total)
    