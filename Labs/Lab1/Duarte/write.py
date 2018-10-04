f = open('data', 'w')
myString = ['one', 'two', 'three']

for s in range(3):
    f.write(myString[s] + '\n')

f.close()