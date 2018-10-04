sum = 0

for x in range(5):
    newValue = int(input('Insert number ' + str(x + 1) + ': '))
    sum = sum + newValue

average = sum / 5
print('The average is', average)