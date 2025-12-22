def perform_op(sym, nums):
    if sym == '*':
        answer = 1
        for num in nums:
            answer *= int(num)
        return answer
    elif sym == '+':
        answer = 0
        for num in nums:
            answer += int(num)
        return answer
    return 0

total_sum = 0
operations = []
with open("input-6.txt", "r") as f:
    line = f.readline().strip()
    while line:
        nums = line.split()
        operations.append(nums)
        line = f.readline().strip()

for i in range(len(operations[-1])):
    numbers = [operations[j][i] for j in range(len(operations) - 1)]
    total_sum += perform_op(operations[-1][i], numbers)

print(total_sum)
