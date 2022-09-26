import random
import time

score = 0
singin = input("Your Name : ")
time.sleep(0.5)
print("\nhello" , singin , "!")
time.sleep(0.5)
print("your score is : ", score)
time.sleep(0.5)
print("Lets begins\n")
time.sleep(0.5)
javab = random.randint(1,99)

console = '1'

while console != '2':
    console = input("Do you Want to Start Game ? [1=yes , 2=exit] >>> ")
    if console == '1':
        myhads = input("Enter your Hads : ")
        myhads = int(myhads)
        while javab != myhads :
            if myhads > javab:
                print("The Number Is Smaller ! ")
                myhads = input("Enter your Hads agian : ")
                myhads = int(myhads)
            else : 
                print("The Number Is Larger ! ")
                myhads = input("Enter your Hads agian : ")
                myhads = int(myhads)
        print("\n\nWinner Winner Chicken Dinner !!! ")
        score = random.randint(30,300)
        print("your score is :" , score)
        time.sleep(1)
        print("\n")
        javab = random.randint(1,99)
    else :
        console = input("are you sure ? [1=yes , 2=exit] >>> ")

exit()

# Created By AMIRX
