import os

name = input('Please enter your name: ')


def main():
    
    map1 = []
    lives = 3
    size = 0
    a = 0

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
        restart = ''       
        while restart != 'y' or 'n': 
            restart = input('\nDo you want to start a new game? [y/n]: ')    
            if restart == 'y':
                main()
            elif restart == 'n':
                os.system('clear')
                print('Good Bye!')
                quit()
            else:
                re_print()
                print('\nOnly <y> or <n> is accepted!')

    def finish_line(b):
        j = map1.index('o ')
        map1.insert(b, 'o ')
        del map1[j]
        del map1[j]
        map1.insert(j, '  ')
        nonlocal a
        a += 1
        next_map()

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

    def game_menu():
        os.system('clear')
        print('Welcome ' + name + '!\n')
        print('\nMain menu:\n 1.New Game\n 2.Guide\n 3.Exit\n')

    def move_func():
        while True:
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

    def next_map():
        nonlocal a
        if a == 1:
            imp_map2()
        else:
            imp_map3()
        

    def imp_map2():
        nonlocal map1
        map1 = []
        os.system('clear')
        nonlocal size
        size = 15
        import_map('map2.txt')
        move_func()
        

    def imp_map3():
        nonlocal map1
        map1 = []
        os.system('clear')
        nonlocal size
        size = 9
        import_map('map1.txt')
        move_func()

    def gameplay():
        game_menu()
        x = int(input('Select: '))
        os.system('clear')
        if x == 1:
            nonlocal size
            size = 9
            import_map('map1.txt')
            move_func()
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
    gameplay()

    

main()