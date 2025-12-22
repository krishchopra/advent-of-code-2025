zeroes = 0
dial_pos = 50

with open("data.txt") as file:
    for move in file:
        move = move.strip()
        direction = move[0]
    distance = int(move[1:])
    if direction == "L":
            dial_pos = (dial_pos - distance) % 100
    else:  # direction == "R"
            dial_pos = (dial_pos + distance) % 100

    if dial_pos == 0:
            zeroes += 1

print(zeroes)