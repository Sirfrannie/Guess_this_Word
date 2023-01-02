from pydictionary import Dictionary
import random , time , sys , os
import interface

# open read words from Word.txt
lines = []
with open('Word.txt') as f:
    lines = f.readlines()

# function for checking the answer
def answercheck(word,answer) :
    word.lower()
    answer.lower()
    if (answer == word) :
        return True
    else :return False    
  

# game logic handle here!
def maingame():
    score = 0
    while True : # continue loop untill user stop
        os.system('cls')

        # random the word 
        lword = random.choice(lines)
        lword = lword.split("\n")
        word = lword[0]

        dict = Dictionary(word)
        # find word's meaning and defination
        hint = dict.meanings()

        # censor the answer in the meaning list
        list = []
        for meaning in hint :
            a = meaning.split()
            for i in range (len(a)) :
            
                if a[i] == word or a[i].capitalize() == word.capitalize() or a[i] == word + "." :
                    a[i] = "\".....\""

            list.append(a)

        # remove some character from the word and replace it with _            
        Char = []
        for i in range (len(word)):
            Char.append(word[i])

        x = int((len(word)/2)+1)
        loop = True
        count = 0 
        while (loop) :
            i = random.randint(0,(len(Char))-1)
            if (Char[i] != "_"):
                Char[i] = "_"
                count += 1
            else : continue
            if (count == x) :
                loop = False

        # box animation
        for i in range (int(interface.Lbox)) :
            time.sleep(.01)
            sys.stdout.write("--")
            sys.stdout.flush()
        print ()
        
        # game's interface 
        print("    Guess This Word!")
        print(f"                               your score : {score}")
        print("          ",*Char)
        print()
        print(" Meaning :")

        # hint or meaning
        for i in range (2):
            print (f"{i+1}. ", *list[i])
        
        # box animation
        for i in range (int(interface.Lbox)) :
            time.sleep(.01)
            sys.stdout.write("--")
            sys.stdout.flush()
        print ()

        # read answer
        user_answer = input("tell me your answer ::> ")
        # check answer
        result = answercheck(word,user_answer)

        # display result
        if (result): # correct
            os.system('cls')
            score += 1 # add score
            interface.correct()
        else : # incorrect
            os.system('cls')
            score = 0  # delete score
            # show correct answer
            interface.incorrect(word,hint[0],hint[1])  
        print ()

        # continue or end
        print ("menu -> 0 ; continue -> Enter")
        user_choose = str(input("type the number ::>"))

        # check if user type "0" break the loop
        if user_choose == '0' :
            os.system('cls')
            interface.exit(score)
            break


