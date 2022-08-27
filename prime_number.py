#Write a python script to check whether a given number is Prime or not

number=int(input('Enter a Number : '))
if number==0 or number==1:
    print('Enter Valid Input')
else:
    for x in range(2,number):
        if number%x==0:
            print('Not Prime Number')
            break
    else:
        print('Prime Number')