total = 0

while True:
    firstSet = set()
    secondSet = set()
    sections = input()
    if sections == 'q':
        break
    (first, second) = sections.split(',')
    (firstFirst, firstSecond) = first.split('-')
    (secondFirst, secondSecond) = second.split('-')

    firstRange = int(firstSecond) - int(firstFirst)
    secondRange = int(secondSecond) - int(secondFirst)
    for i in range(0,firstRange+1):
        firstSet.add(i+int(firstFirst))
    for i in range(0,secondRange+1):
        secondSet.add(i+int(secondFirst))
    output = firstSet & secondSet
    if len(output) > 0:
        total = total + 1
print(total)