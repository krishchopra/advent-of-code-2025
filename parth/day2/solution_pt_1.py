def is_invalid(num):
    if len(str(num)) % 2 != 0:
        return False
    first_half = int(str(num)[:len(str(num))//2])
    second_half = int(str(num)[len(str(num))//2:])
    return first_half == second_half

with open('data.txt') as f:
    lines = [line.rstrip('\n') for line in f]

ranges = lines[0].split(',')
num_ranges = [(int(r.split('-')[0]), int(r.split('-')[1])) for r in ranges]

invalid_sum = 0
for start, end in num_ranges:
    for num in range(start, end + 1):
        if is_invalid(num):
            invalid_sum += num

print(f"Sum of invalid numbers: {invalid_sum}")

