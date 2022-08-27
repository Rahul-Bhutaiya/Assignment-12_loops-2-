#Write a python script to check whether a given pair of numbers are co-Prime numbers or not.

num_1=int(input('Enter First Number : '))
num_2=int(input('Enter Second Number : '))

small=num_1 if num_1<num_2 else num_2

while small>0:
    if num_1%small==0 and num_2%small==0:
        if small==1:
            print('Co-Prime Numbers...')
        else:
            print('Not Co-Prime Numbers...')
            break
    small-=1