# points:
# rock - 1
# paper - 2
# scissors - 3

# win - 6
# draw - 3
# lose - 0

# opponent:
# A - rock
# B - paper
# C - scissors

# you:
# X - rock
# Y - paper
# Z - scissors

def windeterminer(opponent, player):
    result = ord(opponent) - ord(player)
    if result == -23:
        return 3 # draw
    elif result == -24 or result == -21:
        return 6 # win
    elif result == -25 or result == -22:
        return 0 # loss
    else:
        print('ERROR')
        return -1

points = 0

while True:
    throw = input()
    if throw == 'q':
        break
    (opponent, player) = throw.split(' ')

    if(player == 'X'):
        points = points + 1 + windeterminer(opponent, player)
    elif(player == 'Y'):
        points = points + 2 + windeterminer(opponent, player)
    elif(player == 'Z'):
        points = points + 3 + windeterminer(opponent, player)
print(points)