##multiplication quiz jel

#initial
import random

#functions
def quiz():
    print("choose your gamemode:")
    gamemode = int(input("1 for easy, 2 for medium, 3 for hard:"))
    endless = int(input("would you like to play endless mode? click 1 for yes, 2 for no"))
    if endless == 2:          
        if gamemode == 1:
            times = int(input("how many questions would you like?"))
            score = 0
            for i in range (times):
                p1= random.randint(1,10)
                p2= random.randint(1,10)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    score += 1
                else:
                    print("incorrect")
            print("your final score is: " + str(score))
            
        elif gamemode == 2:
            times = int(input("how many questions would you like?"))
            score = 0
            for i in range (times):
                p1= random.randint(1,100)
                p2= random.randint(1,100)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    score += 1
                else:
                    print("incorrect")
            print("your final score is: " + str(score))
            
        elif gamemode == 3:
            times = int(input("how many questions would you like?"))
            score = 0
            for i in range (times):
                p1= random.randint(1,100)
                p2= random.randint(1,100)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    score += 1
                else:
                    print("incorrect")
            print("your final score is: " + str(score))
        

    elif endless == 1:           
        if gamemode == 1:
            playagain = 0
            while playagain == 0:
                p1= random.randint(1,10)
                p2= random.randint(1,10)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    print("Do you want to continue?")
                    playagain = int(input("1 for yes, 0 for no"))
                else:
                    print("incorrect")
                    playagain = int(input("1 for yes, 0 for no"))
            
        if gamemode == 2:
            playagain = 0
            while playagain == 0:
                p1= random.randint(1,10)
                p2= random.randint(1,10)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    print("Do you want to continue?")
                    playagain = int(input("1 for yes, 0 for no"))
                else:
                    print("incorrect")
                    playagain = int(input("1 for yes, 0 for no"))

        if gamemode == 3:
            playagain = 0
            while playagain == 0:
                p1= random.randint(1,10)
                p2= random.randint(1,10)
                print(str(p1) + " x " + str(p2))
                useranswer = int(input(""))
                answer = p1*p2
                if useranswer == answer:
                    print("correct!")
                    print("Do you want to continue?")
                    playagain = int(input("1 for yes, 0 for no"))
                else:
                    print("incorrect")
                    playagain = int(input("1 for yes, 0 for no"))

#main
quiz()
