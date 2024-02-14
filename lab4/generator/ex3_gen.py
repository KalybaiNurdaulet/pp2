# Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.

v = int(input())

def gen3and4(v):
    for i in range(v):
        if i%4 == 0 or i%3 == 0:
            print(i)

gen3and4(v)

        