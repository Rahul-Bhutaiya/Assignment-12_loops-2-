#Write a python script to print first N prime numbers

x=2
prime=0
n_value=int(input('Enter N Value : '))
while prime<n_value:
    while True:
        if x==2:
            print(x,end=' ')
            prime+=1
            x+=1
            break
        for k in range(2,x):
            if x%k==0:
                x+=1
                break
        else:
            print(x,end=' ')
            prime+=1
            x+=1
            break