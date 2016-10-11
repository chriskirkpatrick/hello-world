#!/usr/bin/python
#thousand = [i*1 for i in range(1,1001)]
thousand = []
for i in range(1,1000001):
    thousand.append(i)
#print(thousand)
print(min(thousand))
print(max(thousand))
print(sum(thousand))
