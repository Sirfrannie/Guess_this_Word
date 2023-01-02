import gameSys
import interface
import os , sys

os.system('cls')
interface.Welcome()
react = input("Press Enter to continue")
os.system('cls')


while True :
    os.system('cls')
    interface.menu()
    # input user dicisions
    user_select = input("input the number ::> ")
    
    if (user_select == '1'): # for play game
        os.system('cls')
        gameSys.maingame()

    elif (user_select == '2'): # for read in game's details
        os.system('cls')
        interface.gameinfo()
        react = input("\nPress Enter to return to menu")

    elif (user_select == '0'): # for exit game
        os.system('cls')
        interface.gamequit()
        os.system('cls') 
        sys.exit()    

    else : # if user input are not in above 
        os.system('cls')
        print ("    Something wrong")
        print ("    please select correct number")
        react = input("\nPress Enter to return to menu")
