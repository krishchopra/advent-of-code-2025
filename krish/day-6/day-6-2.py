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
    line = f.readline().strip('\n')
    while line:
        operations.append(line)
        line = f.readline().strip('\n')

new_ops = ""
for i in range(len(operations[-1])):
    if operations[-1][i] != ' ':
        new_ops += operations[-1][i]
operations[-1] = new_ops

curr_idx = 0
for i in range(len(operations[-1])):
    num_is_there = True
    op = operations[-1][i]
    numbers = []
    while num_is_there:
        curr_num = ""
        for j in range(len(operations) - 1):
            if curr_idx < len(operations[j]):
                curr_num += operations[j][curr_idx]
            else:
                break
        if curr_num.strip() == "":
            num_is_there = False
        else:
            numbers.append(int(curr_num.strip()))
        curr_idx += 1
    
    total_sum += perform_op(op, numbers)

print(total_sum)
