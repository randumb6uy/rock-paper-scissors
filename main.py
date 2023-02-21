import random
import time

#variables
p = 0
c = 0
#intro
print("WELCOME to the stone-paper-scissors arena, you are being currently matched against a ai with top-notch skills , so prepare for the worse")

print("")

print("RULES: \ndont cheat \ndon't close the program \nhe mtach will be held in a set of thirteen \none who wins most matches will win")
time.sleep(.6)

print("")

print('your match will start in:')

print("")
#starting coundown
time.sleep(.6)
print("3....")
time.sleep(.6)
print("2....")
time.sleep(.6)
print('1....')

print("")
#
# match
for j in range(13):
    moves = ( 'stone','paper','scissors')
    player = 0

    comp = random.choice(moves)

    while player not in moves:
        player = input('enter your move ( stone , paper , scissors) : ')

    for i in range(3):
        print(moves[i]+"....")
        time.sleep(0.8)

    print("computer played "+comp)
    
    print("")
    
    if player == "stone":
        if comp == "paper":
            print("YOU LOSE!!!")
            c += 1
        elif comp == "scissors":
            print("YOU WIN!!!")
            p += 1
        else:
            print("TIE!!!")
    elif player == "paper":
        if comp == "scissors":
            print("YOU LOSE!!!")
            c += 1
        elif comp == "stone":
            print("YOU WIN!!!")
            p += 1
        else:
            print("TIE!!!")
    else:
        if comp == "stone":
            print("YOU LOSE!!!")
            c += 1
        elif comp == "paper":
            print("YOU WIN!!!")
            p += 1
        else:
            print("TIE!!!")

    print("")
    time.sleep(1)
    if i != 9 :
        print("next match will start in")
        for i in range(3):
            print( str(4 - i) +"....")
            time.sleep(0.6)

if p > c:
    print("well well well")
    time.sleep(0.6)
    print('')
    print("CONGRATULATIONS THE PLAYER WINS!!!")
elif c > p:
    print("sorry to hurt your feelings but COMPUTER WINS!!!")
else:
    print("uhhhhhhh")
    time.sleep(0.6)
    print('')
    print("ITS A TIE??")

