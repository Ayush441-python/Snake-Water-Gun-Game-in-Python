import random
computer = random.choice([1,-1,0])
youstr = input("Enter your choice(s,w,g): ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]
if(computer==youstr):
    print("Draw")
else:
    if(computer==-1 and you==1):
        print("You Win")
    elif(computer==-1 and you==0):
        print("You Lose")
    elif(computer==1 and you==-1):
        print("You Lose")
    elif(computer==1 and you==0):
        print("You Win")
    elif(computer==0 and you==-1):
        print("You Win")
    elif(computer==0 and you==1):
        print("You Lose")
    else:
        print("Error")




