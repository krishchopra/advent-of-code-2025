num_zeroes = 0

with open("input.txt", 'r') as f:
    cur_pos = 50
    line = f.readline().strip()
    while line:
        dir = line[0]
        num = int(line[1:])
        if dir == 'L':
            for i in range(num):
                cur_pos -= 1
                if cur_pos % 100 == 0:
                    num_zeroes += 1
        else:
            for i in range(num):
                cur_pos += 1
                if cur_pos % 100 == 0:
                    num_zeroes += 1
        
        line = f.readline().strip()

print(num_zeroes)
