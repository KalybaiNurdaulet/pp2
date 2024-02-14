# Implement a generator that returns all numbers from (n) down to 0.

v = int(input())

gene = (i for i in range(v,0,-1))

for i in gene:
    print(i, end =",")