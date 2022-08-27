#Write a python script to calculate LCM of two numbers

first_num=int(input('Enter First Number : '))
second_num=int(input('Enter Second Number : '))

big=first_num if first_num>second_num else second_num

while big<=first_num*second_num:
    if big%first_num==0 and big%second_num==0:
        print('LCM :',big)
        break
    big+=1