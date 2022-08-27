#Write a python script to print first N terms of a Fibonacci series

first=0
second=1
for x in range(int(input('Enter N Value : '))):
    if x==0:
        print(x,end=' ')
        continue
    first,second=second,first+second
    print(first,end=' ')