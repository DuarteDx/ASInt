import operator
f = open('data.txt', 'r')

text = f.readlines()
s = set()
v = []
d = {}

for i in range(len(text)):
    v.append(int(text[i]))
    s.add(int(text[i]))

for i in s:
    d[i] = 0

for i in range(len(text)):
    d[int(text[i])] = d[int(text[i])]+1

sorted_d = sorted(d.items(), key=operator.itemgetter(1))
print(sorted_d)