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
# X - lose
# Y - draw
# Z - win

def throwTranslator(throw):
    if throw == 'Z':
        return 3
    elif throw == 'Y':
        return 2
    elif throw == 'X':
        return 1
    print('ERROR')
    return 0

points = 0

while True:
    throw = input()
    if throw == 'q':
        break
    (opponent, player) = throw.split(' ')

    if(player == 'X'):
        realPlayerThrow = chr(ord(opponent) + 25)
        realPlayerThrow2 = chr(ord(opponent) + 22)
        if throwTranslator(realPlayerThrow) > throwTranslator(realPlayerThrow2):
            points = points + 0 + throwTranslator(realPlayerThrow)
        else:
            points = points + 0 + throwTranslator(realPlayerThrow2)
                
    elif(player == 'Y'):
        realPlayerThrow = chr(ord(opponent) + 23)
        points = points + 3 + throwTranslator(realPlayerThrow)
        
    elif(player == 'Z'):
        realPlayerThrow = chr(ord(opponent) + 24)
        realPlayerThrow2 = chr(ord(opponent) + 21)
        if throwTranslator(realPlayerThrow) > throwTranslator(realPlayerThrow2):
            points = points + 6 + throwTranslator(realPlayerThrow)
        else:
            points = points + 6 + throwTranslator(realPlayerThrow2)
print(points)