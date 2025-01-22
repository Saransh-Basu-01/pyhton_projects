import random
while True:
    choice=input("enter your choice(y/n)").lower()
    if choice=='y':
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        print(f"{die1},{die2}")
        if(die1==6 and die2==6):
            print("you win the game \n")
        else:
            print("you lost the game")
    elif choice=='n':
        print("thanks for playing")
    else:
        print("invalid choice")
    