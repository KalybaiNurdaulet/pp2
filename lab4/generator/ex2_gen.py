# Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console

v = int(input())

generator = (i for i in range(0,v,2))

for i in generator:
    print(i,end = ",")