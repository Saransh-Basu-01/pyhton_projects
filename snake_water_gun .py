''' 
1 for snake
-1 for water
0 for gun 
'''
import  random
computer=random.choice([-1,0,1])
your_choice=input("enter your choice")#only choose s,w,g
youdict={ "s":1,"w":-1,"g":0}
reversedict={ 1:"snake",-1:"water",0:"gun"}
you=youdict[your_choice]
if(your_choice=="s"or your_choice=="w" or your_choice=="g"):
    print(f"You choose {reversedict[you]}\ncomputer chooses {reversedict[computer]}")
    if(you==computer):
        print("its a draw")
    else:
        if(you==1 and computer==-1):
            print("you have won the round")
        elif(you==1 and computer==0):
            print("you have lost the round")
        elif(you==-1 and computer==0):
            print("you have won the round")
        elif(you==-1 and computer==1):
            print("you have lost the round")
        elif(you==0 and computer==1):
            print("you have won the round")
        elif(you==0 and computer==-1):
            print("you have lost the round")
else:
    print("invalid input")