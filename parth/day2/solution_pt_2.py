def can_be_sliced_equally(piece: str, whole: str) -> bool:
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

