import random
number=random.randint(1,100)
n=-1
guesses=0
while(n!=number):
    guesses+=1
    n=int(input("guess a number: "))
    if(n>number):
        print(" you have entered higher number guess again")
    elif(n<number):
        print("you have entered lower number guess again")
    else:
       print(f"you have guessed the number in {guesses} attempt")
        