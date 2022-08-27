#Write a python script to find next prime number of a given number

number=int(input('Enter a Number : '))+1
if number==1:
    print('Enter Valid Input')
else:
    while True:
        for x in range(2,number):
            if number%x==0:
                number+=1
                break
        else:
            print('Next Prime Number :',number)
            break