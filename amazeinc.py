import os


def main():

    level = []
    lives = 0
    size = 0
    map_num = 0

    # main menu
    def game_menu():
        os.system('clear')
        print('Welcome ' + name + '!\n')
        print('\nMain menu:\n 1.New Game\n 2.Guide\n 3.Exit\n')

    # sub menus and game start
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
            story(1)
            os.system('clear')
            load_map('map1.txt', 9)
        elif mainmenu_select == 2:
            os.system('clear')
            print("\nThe Story:\nYou control an adventurer who, after stealing a valued artifact from a native tribe, is being chased. Guide him through the various maps to safety.")
            print("\nControls:\n Use W,A,S,D keys to move.\n W = UP\n S = Down\n A = Left\n D = Right")
            print("\nDeveloped by A_Maze.inc")
            submenu_select = input('\nPress enter to continue. ')
            if submenu_select == '':
                main()
        elif mainmenu_select == 3:
            os.system('clear')
            print('Good Bye!')
            quit()

    # movement functions
    def move_func():
        while True:
            movement = input("\nMove(w,a,s,d): ")
            if movement == "d":
                movement_key(1)
                re_print()
            elif movement == "a":
                movement_key(-1)
                re_print()
            elif movement == "w":
                movement_key(-size)
                re_print()
            elif movement == "s":
                movement_key(size)
                re_print()
            elif movement == "gm powers":  # cheat code to jump to next map
                finish_line(level.index('o '))
            else:
                re_print()
                print("\nEnter the correct key!")
            if lives == 0:
                win_restart()

    def movement_key(way):
        position = level.index('o ')
        if level[position + way] == '▉ ':
            position
            nonlocal lives
            lives = lives - 1
        elif level[position + way] == '▒ ':
            finish_line(position + way)
        else:
            del level[position]
            level.insert(position, '  ')
            del level[position + way]
            level.insert(position + way, 'o ')

    # game story texts
    def story(scenario):
        if scenario == 1:
            os.system('clear')
            print("The adventurer carefully picked his way through confines of the dark cave. \nHis torch flickered and danced in the moist air. He could still hear \nthe distant drums echoing in the faint breeze in the tunnel behind him. \nSuddenly, his torch went out, and his world was plunged into darkness. \nBut not complete darkness, there was a faint light ahead, a hazy, green, \ntinge light…")
            cont = input("\nPress enter to continue.")
        elif scenario == 2:
            os.system('clear')
            print("Shuffling forward, he startled, as his hands touched the rough outline of \nvegetation. Wielding his machete, he started cutting an opening and the \nlight grew brighter. Suddenly he stumbled, falling forward, rolling and \nrolling into bright sunlight and tall, thick grass.")
            cont = input("\nPress enter to continue.")
        elif scenario == 3:
            os.system('clear')
            print("He found himself standing in a vast open plain with high mountains in the \ndistance encompassing the area in a huge crescent. Despite the terrors \nof the long grass there was an ominous feeling of vulnerability in this \nopen environment. As if it was some kind of... focal point for a devious, \nbut as yet unsprung trap. Towards the far end of the plain a large \noutcropping could be seen, rising sharply, like a dark, black mesa. \nAs swiftly as his heart would beat, he made for the higher ground...")
            cont = input("\nPress enter to continue.")
        elif scenario == 4:
            os.system('clear')
            print("The adventurer gazed down from the mesa towards the thick jungle that was \nnow between him and the mountains. Mountains that were so much closer \nnow, looming over him like claws, their shadow casting darkness stretching \ntowards him over the vast greenery. Yet, looking closer, in the distance, \nhe could see a clearing. Rising gently from within, was a ghost \nlike smirk. A welcome...?\n…or a warning?")
            cont = input("\nPress enter to continue.")
        elif scenario == 5:
            os.system('clear')
            print("He ran, as hard as he could, the shouts and wails of the cannibals were all \ntoo close. Darts zipping past his cheeks as he half ran, half fell \ndown the steep jungle hill: not this time will he plan of waiting at bottom \nof the hill with a plain and easy escape. Alas, there was a cave in the \nfoot of the mountains, perhaps, he could reach it, he might have a chance… ")
            cont = input("\nPress enter to continue.")
        elif scenario == 6:
            os.system('clear')
            print("Oblivious to him, the pursuers have halted with a sudden sensation of dread \nand silence. As if they feared to tread further into the valley, lest \nthey disturb something not of this world...")
            cont = input("\nPress enter to continue.")

    # map handling
    def next_map():
        nonlocal map_num
        if map_num == 1:
            story(3)
            load_map('map2.txt', 15)
        elif map_num == 2:
            story(5)
            load_map('map3.txt', 23)
        else:
            win_restart()

    def import_map(filename):
        with open(filename) as f:
            line = f.read().split(',')
            for char in line:
                if char.startswith('\n'):
                    level.append(char[1:])
                else:
                    level.append(char)
        printlevel()

    def load_map(filename, width):
        nonlocal level
        level = []
        os.system('clear')
        nonlocal size
        size = width
        import_map(filename)
        move_func()

    def printlevel():
        print(f"You have {lives} lives left\n")
        row = ''
        for index in range(len(level)):
            row += level[index]
            if (index + 1) % size == 0:
                print(row)
                row = ''

    def re_print():
        os.system('clear')
        printlevel()

    # next map counter
    def finish_line(lastpos):
        position = level.index('o ')
        level.insert(lastpos, 'o ')
        del level[position]
        del level[position]
        level.insert(position, '  ')
        nonlocal map_num
        if map_num == 0:
            story(2)
        elif map_num == 1:
            story(4)
        elif map_num == 2:
            story(6)
        map_num += 1
        next_map()

    # endgame restart trigger
    def win_restart():
        os.system('clear')
        printlevel()
        if lives == 0:
            print("\nYou have lost all of your lives!")
        else:
            print('\nCongratulations ' + name + '!' '\nYou managed to get away from the bloodthirsty cannibals and hid in a cave safely... \n...or did you?')
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
    gameplay()
name = input('\nPlease enter your name: ')
main()
