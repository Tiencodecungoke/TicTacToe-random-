#import thu vien ngau nhien
import random
#tao ban co
broad = ["-","-","-","-","-","-","-","-","-"]
#input_X_or_Y
X_Y = input("Choose X or Y : ").upper()
X_Y_B = "Y"
if X_Y == "Y":
    X_Y_B = "X"
#in ban co
def printbroad():
    print(broad[0]+"|"+broad[1]+"|"+broad[2])
    print(broad[3]+"|"+broad[4]+"|"+broad[5])
    print(broad[6]+"|"+broad[7]+"|"+broad[8])
#dieu kien thang 
def check_win():
    if (broad[0] == broad[1] and broad[0] == broad[2] and broad[0]!="-")                                                           or (broad[3] == broad[4] and broad[3] == broad[5] and broad[3]!="-")                                                             or (broad[6] == broad[7] and broad[6] == broad[8] and broad[6]!="-")                                                             or (broad[0] == broad[3] and broad[0] == broad[6] and broad[0]!="-")                                                               or (broad[1] == broad[4] and broad[1] == broad[7] and broad[1]!="-")                                                             or (broad[2] == broad[5] and broad[2] == broad[8] and broad[2]!="-")                                                             or (broad[2] == broad[4] and broad[2] == broad[6] and broad[2]!="-")                                                             or (broad[0] == broad[4] and broad[0] == broad[8] and broad[0]!="-") :
        return True
    return False
#check trung buoc di
def check(choose,Key_Word):
    if broad[choose] != "-":
        return False
    else:
        return True
#buoc di cho player
def playerMove():    
    move_input_player=int(input("choose(1-9) : "))-1

    if check(move_input_player,X_Y):
        broad[move_input_player]=X_Y
        printbroad()
        print("------")
    else:
        playerMove()
    if check_win():
        print("you win")
        exit()
#buoc di cho bot
def botMove():    
    move_bot= random.randint(0,8)
    if check(move_bot,X_Y_B):
        broad[move_bot]=X_Y_B
        printbroad()
    else:
        botMove()
    if check_win():
        print("you lose")
        exit()
#chay ham
def rungame():
    printbroad()
    for i in range(4):
        playerMove()
        botMove()
        if check_win == False and i == 3:
            print("draw")
            exit()
#chay nhaaa
rungame()