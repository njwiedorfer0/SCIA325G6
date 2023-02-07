import random
import time
from pydub import AudioSegment
from pydub.playback import play

#Player 1 inputs for ship position
coordP1List = []
print('PLAYER 1 ENTER COORDINATES:')
charX1P1 = int(input('Enter a Pirate Ship 1 Y positions (0-3): '))
charY1P1 = int(input('Enter a Pirate Ship 1 X positions (0-5): '))
coordP1List.append([charX1P1, charY1P1])
print()
charX2P1 = int(input('Enter a Pirate Ship 2 Y positions (0-3): '))
charY2P1 = int(input('Enter a Pirate Ship 2 X positions (0-5): '))
coordP1List.append([charX2P1, charY2P1])
print()
charX3P1 = int(input('Enter a Pirate Ship 3 Y positions (0-3): '))
charY3P1 = int(input('Enter a Pirate Ship 3 X positions (0-5): '))
coordP1List.append([charX3P1, charY3P1])
print(coordP1List)

#Player 2 inputs for ship position
coordP2List = []
print('\nPLAYER 2 ENTER COORDINATES:')
charX1P2 = random.randint(4, 7) #int(input('Enter a Pirate Ship 1 Y positions (4-7): '))
charY1P2 = random.randint(0, 5) #int(input('Enter a Pirate Ship 1 X positions (0-5): '))
coordP2List.append([charX1P2, charY1P2])
print()
charX2P2 = random.randint(4, 7) #int(input('Enter a Pirate Ship 2 Y positions (4-7): '))
charY2P2 = random.randint(0, 5) #int(input('Enter a Pirate Ship 2 X positions (0-5): '))
coordP2List.append([charX2P2, charY2P2])
print()
charX3P2 = random.randint(4, 7) #int(input('Enter a Pirate Ship 3 Y positions (4-7): '))
charY3P2 = random.randint(0, 5) #int(input('Enter a Pirate Ship 3 X positions (0-5): '))
coordP2List.append([charX3P2, charY3P2])

charPos = '|   |'  

board = [['|   |' for a in range(6)] for b in range(8)]

#Setting player 1 positions
board[charX1P1][charY1P1] = charPos
board[charX2P1][charY2P1] = charPos
board[charX3P1][charY3P1] = charPos

#Setting player 2 positions
board[charX1P2][charY1P2] = charPos
board[charX2P2][charY2P2] = charPos
board[charX3P2][charY3P2] = charPos

#count = 4
p1Hit = []
p2Hit = []

while True:
    print()
    count = 0
    for i in board:
            print('----- ----- ----- ----- ----- -----')
            print(' '.join(i))
            print('----- ----- ----- ----- ----- -----')
            count += 1
            if  count == 4:
                print('###################################')
    count = 0
    for i in range(1):
        print()
        print('Player 1: CHOOSE A COORDINATE TO ZAP')
        attackListP1 = []
        attackCharX1P1 = int(input('Enter a ZAP Y positions (4-7): '))
        attackCharY1P1 = int(input('Enter a ZAP X positions (0-5): '))
        attackListP1.append([attackCharX1P1, attackCharY1P1])
        try:
            if (coordP2List.index(attackListP1[0])> -1):
                board[attackCharX1P1][attackCharY1P1] = '|XXX|'
                play(AudioSegment.from_mp3("C:\\Users\\aaron\\Desktop\\zap.mp3"))
                attackListP1.clear()
                p1Hit.append(1)
        except ValueError:
            board[attackCharX1P1][attackCharY1P1] = '|■■■|'
            attackListP1.clear()
    
    if len(p1Hit) >= 3:
        print()
        for i in board:
            print('----- ----- ----- ----- ----- -----')
            print(' '.join(i))
            print('----- ----- ----- ----- ----- -----')
            count += 1
            if  count == 4:
                print('###################################')
        print("CPU COULDN'T AVOID THE LIGHT: PLAYER 1 WINS")
        break
    count = 0
    for i in board:
            print('----- ----- ----- ----- ----- -----')
            print(' '.join(i))
            print('----- ----- ----- ----- ----- -----')
            count += 1
            if  count == 4:
                print('###################################')
            
    for i in range(1):
            print('Player CPU: COORDINATE TO ZAP')
            attackListP2 = []
            attackCharX1P2 = random.randint(0, 3)
            attackCharY1P2 = random.randint(0, 5)
            attackListP2.append([attackCharX1P2, attackCharY1P2])
            try:
                if (coordP1List.index(attackListP2[0])> -1):
                    board[attackCharX1P2][attackCharY1P2] = '|XXX|'
                    play(AudioSegment.from_mp3("C:\\Users\\aaron\\Desktop\\zap.mp3"))
                    attackListP2.clear()
                    p2Hit.append(1)
            except ValueError:
                board[attackCharX1P2][attackCharY1P2] = '|■■■|'
                attackListP2.clear()

    time.sleep(1)
    
    if len(p2Hit) >= 3:
        print()
        for i in board:
            print('----- ----- ----- ----- ----- -----')
            print(' '.join(i))
            print('----- ----- ----- ----- ----- -----')
            count += 1
            if  count == 4:
                print('###################################')
        print("PLAYER 1 COULDN'T AVOID THE LIGHT: CPU WINS")
        break
            
