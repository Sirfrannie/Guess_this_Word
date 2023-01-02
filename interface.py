import time
import sys


box = "--------------------------------------------------------"
Lbox = (float(len(box)))/2 
def Welcome() :
    print (box)
    time.sleep(1)
    print ("              H E L L O   P L A Y E R ")
    print()
    time.sleep(1)
    print ("                    welcome to")
    print()
    time.sleep(1)
    print ("           G U E S S   T H E   W O R D S ")
    for i in range (int(Lbox)) :
        time.sleep(.1)
        sys.stdout.write("--")
        sys.stdout.flush()
    print ()    

def gameinfo() :
    print()
    print ("        :::: About this game ::::")
    print ("    (sorry for my bad English)")
    print ()
    print ("    This is a guess the words game.")
    print ("    to play this game I'll give you a meaning ")
    print ("    and some character of that word.")
    print ("    all you need to do is type the word in your mind.")
    print ("    if you are correct you got 1 point.")
    print ("    but if you are incorrect your point will turn to  Z E R O")

def menu():
    print()
    print ("Where you wanna go?\n")
    print ("Start the game --> 1")
    print ("To know about this game --> 2")
    print ("quit the game --> 0")
    print()

def gamequit():
    print("-----------------------------------------------------")
    print()
    print(":::::::::          GAME IS CLOSING          :::::::::")
    print(":                  thank for playing                :")
    print("::             hope to see you next time           ::")
    print()
    print("-----------------------------------------------------")
    sys.stdout.write("Closing")
    for i in range (5) :
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()

def correct():
    print("----------------------------------------------------")
    print()
    print("                    W O W !!                        ")
    print("              you are correct !!!")
    print()
    print("score +1")
    print("----------------------------------------------------")

def incorrect(answer,def1,def2):
    print("----------------------------------------------------")
    print()
    print("                    Oops ~ ~                        ")
    print("             ~ you are incorrect ~")
    print("\n")
    print(f"the answer is : {answer}")
    print("meaning : \n")
    print(f"1. {def1}")
    print(f"2. {def2}\n")
    print("score -> 0")
    print("----------------------------------------------------")

def exit(score):
    print("----------------------------------------------------")
    print()
    print(f"your score {score}")
    print()
    sys.stdout.write("exiting")
    for i in range (5) :
        time.sleep(1)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()    
    for i in range (55) :
        time.sleep(.001)
        sys.stdout.write("-")
        sys.stdout.flush()    
    