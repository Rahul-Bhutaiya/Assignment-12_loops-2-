#Write a python script to calculate HCF of two numbers

num_1=int(input('Enter First Number : '))
num_2=int(input('Enter Second Number : '))

small=num_1 if num_1<num_2 else num_2

while small>0:
    if num_1%small==0 and num_2%small==0:
        print('HCF :',small)
        break
    small-=1