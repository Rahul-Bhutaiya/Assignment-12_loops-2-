#Write a python script to print all Prime numbers between two given numbers (both values inclusive)


for x in range(int(input('Enter First Number : ')),int(input('Enter Second Number : '))+1):
    if x==1 or x==0:
        continue
    if x==2:
        print(x)
        continue
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')