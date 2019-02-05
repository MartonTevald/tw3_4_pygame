import os

name = input('Please enter your name: ')

def main():

    map1 = []
    map2 = ['▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ',
            '▒ ','  ','  ','  ','  ','  ','  ','  ','▉ ',
            '▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','  ','▉ ',
            '▉ ','  ','  ','  ','  ','  ','  ','  ','▉ ',
            '▉ ','  ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ',
            '▉ ','  ','  ','  ','  ','  ','  ','  ','▉ ',
            '▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','  ','▉ ',
            'o ','  ','  ','  ','  ','  ','  ','  ','▉ ',
            '▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ']
    map3 = ['▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ',
            'o ','  ','  ','  ','  ','▉ ','  ','  ','  ','▉ ','  ','  ','  ','▉ ','▉ ',
            '▉ ','  ','▉ ','▉ ','  ','▉ ','  ','▉ ','  ','  ','  ','▉ ','  ','  ','▉ ',
            '▉ ','  ','▉ ','  ','  ','▉ ','  ','  ','▉ ','  ','▉ ','  ','▉ ','  ','▉ ',
            '▉ ','  ','▉ ','▉ ','▉ ','▉ ','▉ ','  ','▉ ','  ','  ','  ','▉ ','  ','▉ ',
            '▉ ','  ','  ','▉ ','  ','  ','▉ ','  ','▉ ','▉ ','  ','▉ ','  ','  ','▉ ',
            '▉ ','▉ ','  ','▉ ','  ','▉ ','  ','  ','  ','▉ ','▉ ','▉ ','  ','▉ ','▉ ',
            '▉ ','  ','  ','  ','  ','▉ ','  ','▉ ','  ','  ','▉ ','  ','  ','  ','▉ ',
            '▉ ','  ','▉ ','▉ ','▉ ','  ','  ','  ','▉ ','  ','▉ ','  ','▉ ','▉ ','▉ ',
            '▉ ','  ','  ','  ','  ','  ','▉ ','  ','  ','▉ ','  ','  ','  ','  ','▒ ',
            '▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ','▉ ']

    def printmap1():
        n = ''
        for i in range(len(map1)):
            n += map1[i]
            if (i + 1) % size == 0:
                print(n)
                n = ''
    def win_restart():
        os.system('clear')
        printmap1()
        print('\nYou Win ' + name + '!')
        restart = input('\nDo you want to start a new game? [y/n]: ')
        if restart == 'y':
            main()
        elif restart == 'n':
            os.system('clear')
            print('Good Bye!')
            quit()

    def finish_line(a):
        j=map1.index('o ')
        map1.insert(a, 'o ')
        del map1[j]
        del map1[j]
        map1.insert(j, '  ')
        win_restart()

    def D_KEY():
        j = map1.index('o ')
        if map1[j+1] == '▉ ' :
            j
        elif map1[j+1] == '▒ ':
            finish_line(j+1)
        else: 
            del map1[j]
            map1.insert(j+1, 'o ')

    def A_KEY():
        j=map1.index('o ')
        if map1[j-1] == '▉ ':
            j
        elif map1[j-1] == '▒ ':
            finish_line(j-1)
        else:
            del map1[j]
            map1.insert(j-1, 'o ')

    def W_KEY():
        j=map1.index('o ')
        if map1[j-size] == '▉ ':
            j
        else:
            del map1[j]
            map1.insert(j, '  ')
            del map1[j-size]
            map1.insert(j-size, 'o ')

    def S_KEY():
        j=map1.index('o ')
        if map1[j+size] == '▉ ':
            j
        else:
            del map1[j]
            map1.insert(j, '  ')
            del map1[j+size]
            map1.insert(j+size, 'o ')

    os.system('clear')
    print('Welcome ' + name + '!\n')
    print('\nMain menu:\n 1.New Game\n 2.Guide\n 3.Exit\n')
    x = int(input('Select: '))

    if x == 1:
        os.system('clear')
        print('\nChoose difficulty level:\n 1. Easy\n 2. Medium\n 3. Hard\n')
        mapnum = int(input('Select: '))
        play = 'y'
        if mapnum == 1:
            size = 9
            map1 = map2
            printmap1()
        elif mapnum == 2:
            size = 15
            map1 = map3
            printmap1()
        elif mapnum == 3:
            size = 23
            file = open("map3.txt", "r")
            for char in file:
                char = file.read(2)
                map1.append(char)
            printmap1()
            file.close()
    elif x == 2:
        os.system('clear')
        print("\nControls:\n Use W,A,S,D keys to move.\n W = UP\n S = Down\n A = Left\n D = Right")
        print("\nDeveloped by A_Maze.inc")
        b = input('\nPress enter to continue. ')
        if b == '':
            main()
    elif x == 3:
        os.system('clear')
        print('Good Bye!')
        quit()

    os.system('clear')
    printmap1()

    while play == 'y':
        movement=input("\nMove(w,a,s,d): ")
        if movement == "d":
            D_KEY()
            os.system('clear')
            printmap1()
        elif movement == "a":
            A_KEY()
            os.system('clear')
            printmap1()
        elif movement == "w":
            W_KEY()
            os.system('clear')
            printmap1()
        elif movement == "s":
            S_KEY()
            os.system('clear')
            printmap1()       
        else:
            os.system('clear')
            printmap1()
            print("\nEnter the correct key!")
        
main()