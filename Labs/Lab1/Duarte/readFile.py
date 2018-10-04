f = open('oneNumberPerLine', 'r')

linesList = f.readlines()
print(linesList)

for x in linesList:
    print(x)

index = 0

for x in linesList:

    linesList[index] = int(x)
    index += 1

print(linesList)