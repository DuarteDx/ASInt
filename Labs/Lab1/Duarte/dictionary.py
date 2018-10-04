f = open('oneNumberPerLine', 'r')
numberList = f.readlines()
print(numberList)
numberOcurrences = {}

index = 0
for x in numberList:
    numberList[index] = int(x)
    index += 1

print(numberList)

for x in numberList:
    print('Current number: ',x)
    # If number already in dictionary
    if x in numberOcurrences:
        numberOcurrences[x] += 1
    # If number not yet in dictionary
    else:
        numberOcurrences[x] = 1
    

print(numberOcurrences)