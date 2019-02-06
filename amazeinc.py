import os

name = input('\nPlease enter your name: ')


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
            print('\nCongratulations ' + name + '!' ' You managed to get away from the bloodthirsty cannibals and hid in a cave safely... \n...or did you?')
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
        if a == 0:
            story(2)
        elif a == 1:
            story(4)
        elif a == 2:
            story(6)
        a += 1
        next_map()

    def story(c):
        if c == 1:
            os.system('clear')
            print("The adventurer carefully picked his way through confines of the dark cave. \nHis torch flickered and danced in the moist air. He could still hear \nthe distant drums echoing in the faint breeze in the tunnel behind him. \nSuddenly, his torch went out, and his world was plunged into darkness. \nBut not complete darkness, there was a faint light ahead, a hazy, green, \ntinge light…")
            d = input("\nPress enter to continue.")
        elif c == 2:
            os.system('clear')
            print("Shuffling forward, he startled, as his hands touched the rough outline of \nvegetation. Wielding his machete, he started cutting an opening and the \nlight grew brighter. Suddenly he stumbled, falling forward, rolling and \nrolling into bright sunlight and tall, thick grass.")
            d = input("\nPress enter to continue.")
        elif c == 3:
            os.system('clear')
            print("He found himself standing in a vast open plain with high mountains in the \ndistance encompassing the area in a huge crescent. Despite the terrors \nof the long grass there was an ominous feeling of vulnerability in this \nopen environment. As if it was some kind of... focal point for a devious, \nbut as yet unsprung trap. Towards the far end of the plain a large \noutcropping could be seen, rising sharply, like a dark, black mesa. \nAs swiftly as his heart would beat, he made for the higher ground...")
            d = input("\nPress enter to continue.")
        elif c == 4:
            os.system('clear')
            print("The adventurer gazed down from the mesa towards the thick jungle that was \nnow between him and the mountains. Mountains that were so much closer \nnow, looming over him like claws, their shadow casting darkness stretching \ntowards him over the vast greenery. Yet, looking closer, in the distance, \nhe could see a clearing. Rising gently from within, was a ghost \nlike smirk. A welcome...?\n…or a warning?")
            d = input("\nPress enter to continue.")
        elif c == 5:
            os.system('clear')
            print("He ran, as hard as he could, the shouts and wails of the cannibals were all \ntoo close. Darts zipping past his cheeks as he half ran, half fell \ndown the steep jungle hill: not this time will he plan of waiting at bottom \nof the hill with a plain and easy escape. Alas, there was a cave in the \nfoot of the mountains, perhaps, he could reach it, he might have a chance… ")
            d = input("\nPress enter to continue.")
        elif c == 6:
            os.system('clear')
            print("Oblivious to him, the pursuers have halted with a sudden sensation of fear \nand silence. As if they feared to tread further into the valley, lest \nthey disturb something not of this world...")
            d = input("\nPress enter to continue.")

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
            elif movement == "gm powers":  # cheat code to jump to next map
                finish_line(map1.index('o '))
            else:
                re_print()
                print("\nEnter the correct key!")
            if lives == 0:
                win_restart()

    def next_map():
        nonlocal a
        if a == 1:
            story(3)
            imp_map2()
        elif a == 2:
            story(5)
            imp_map3()
        else:
            win_restart()

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
        size = 23
        import_map('map3.txt')
        move_func()

    def gameplay():
        game_menu()
        try:
            mainmenu_select = int(input('Select: '))
            if mainmenu_select > 3 or mainmenu_select < 1:
                gameplay()
        except ValueError:
            gameplay()
        os.system('clear')
        if mainmenu_select == 1:
            print('\nChose a difficulty:\n 1. Easy (5 lives)\n 2. Normal (3 lives)\n 3. Dark Souls (1 life)\n')
            diff_menu_select = int(input('Select: '))
            nonlocal lives
            if diff_menu_select == 1:
                lives = 5
            elif diff_menu_select == 2:
                lives = 3
            elif diff_menu_select == 3:
                lives = 1
            nonlocal size
            size = 9
            story(1)
            os.system('clear')
            import_map('map1.txt')
            move_func()
        elif mainmenu_select == 2:
            os.system('clear')
            print("\nControls:\n Use W,A,S,D keys to move.\n W = UP\n S = Down\n A = Left\n D = Right")
            print("\nDeveloped by A_Maze.inc")
            b = input('\nPress enter to continue. ')
            if b == '':
                main()
        elif mainmenu_select == 3:
            os.system('clear')
            print('Good Bye!')
            quit()
    gameplay()

main()
