# Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

a = int(input())
b = int(input())


squares = (i*i for i in range(a,b))

for i in squares:
    print(i , end = " ")
    
print()

for i in range(a,b):
    print(i*i ,end = ",")