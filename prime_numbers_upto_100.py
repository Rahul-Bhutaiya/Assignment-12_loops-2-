#Write a python script to print all Prime numbers under 100

for x in range(2,100):
    if x==2:
        print(x)
        continue
    for y in range(2,x):
        if x%y==0:
            break
    else:
        print(x,end=' ')