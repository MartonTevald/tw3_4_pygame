import os

name = input('Please enter your name: ')


def main():
    lives = 3

    map1 = []

    def printmap1():
        print(f"You have {lives} lives left\n")
        n = ''
        for i in range(len(map1)):
            n += map1[i]
            if (i + 1) % size == 0:
                print(n)
                n = ''

    def import_map(filename):
            with open(filename) as f:
                line = f.read().split(',')
                for i in line:
                    if i.startswith('\n'):
                        map1.append(i[1:])
                    else:
                        map1.append(i)
            printmap1()

    def win_restart():
        os.system('clear')
        printmap1()
        if lives == 0:
            print("\nYou have lost all of your lives!")
        else:
            print('\nYou Win ' + name + '!')
        restart = input('\nDo you want to start a new game? [y/n]: ')
        if restart == 'y':
            main()
        elif restart == 'n':
            os.system('clear')
            print('Good Bye!')
            quit()

    def finish_line(a):
        j = map1.index('o ')
        map1.insert(a, 'o ')
        del map1[j]
        del map1[j]
        map1.insert(j, '  ')
        win_restart()

    def re_print():
        os.system('clear')
        printmap1()

    def D_KEY():
        j = map1.index('o ')
        if map1[j + 1] == '▉ ':
            j
            nonlocal lives
            lives = lives - 1
        elif map1[j + 1] == '▒ ':
            finish_line(j + 1)
        else: 
            del map1[j]
            map1.insert(j + 1, 'o ')

    def A_KEY():
        j = map1.index('o ')
        if map1[j - 1] == '▉ ':
            j
            nonlocal lives
            lives = lives - 1
        elif map1[j - 1] == '▒ ':
            finish_line(j - 1)
        else:
            del map1[j]
            map1.insert(j - 1, 'o ')

    def W_KEY():
        j = map1.index('o ')
        if map1[j - size] == '▉ ':
            j
            nonlocal lives
            lives = lives - 1
        else:
            del map1[j]
            map1.insert(j, '  ')
            del map1[j - size]
            map1.insert(j - size, 'o ')

    def S_KEY():
        j = map1.index('o ')
        if map1[j + size] == '▉ ':
            j
            nonlocal lives
            lives = lives - 1
        else:
            del map1[j]
            map1.insert(j, '  ')
            del map1[j + size]
            map1.insert(j + size, 'o ')

    os.system('clear')
    print('Welcome ' + name + '!\n')
    print('\nMain menu:\n 1.New Game\n 2.Guide\n 3.Exit\n')
    x = int(input('Select: '))
    os.system('clear')

    if x == 1:
        os.system('clear')
        print('\nChoose difficulty level:\n 1. Easy\n 2. Medium\n 3. Hard\n')
        mapnum = int(input('Select: '))
        play = 'y'
        if mapnum == 1:
            size = 9
            import_map(r'/home/marton1812/codecool/codes/3rd_tw/tw3_4_pygame/map1.txt')
            printmap1()
        elif mapnum == 2:
            size = 15
            import_map()
            printmap1()
        elif mapnum == 3:
            size = 23
            import_map()
            printmap1()
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
        movement = input("\nMove(w,a,s,d): ")
        if movement == "d":
            D_KEY()
            re_print()
        elif movement == "a":
            A_KEY()
            re_print()
        elif movement == "w":
            W_KEY()
            re_print()
        elif movement == "s":
            S_KEY()
            re_print()
        else:
            re_print()
            print("\nEnter the correct key!")
        if lives == 0:
            win_restart()
main()
