with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]

def perform_calculation(args):
    numbers, operator = args[:-1], args[-1]
    total = 0 if operator == "+" else 1
    for num in numbers:
        if operator == "*":
            total *= int(num)
        else:
            total += int(num)
    return total
        

numbers_and_operators = []

for line in lines:
    numbers_and_operators.append(line.split())

calculations = zip(*numbers_and_operators)

sum_total = 0

for calc in calculations:
    res = perform_calculation(calc)
    sum_total += res

print(sum_total)
    