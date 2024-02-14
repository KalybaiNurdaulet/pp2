# Create a generator that generates the squares of numbers up to some number N.
v = int(input())
generator = (i*i for i in range(v))

for i in generator:
    print(i)