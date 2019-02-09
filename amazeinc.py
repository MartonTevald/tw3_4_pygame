import os


def main():

    level = []
    lives = 0
    size = 0
    map_num = 0

    # main menu, where it all begins
    def game_menu():
        os.system('clear')
        print('Welcome ' + name + '!\n')
        print('\nMain menu:\n 1.New Game\n 2.Guide\n 3.Exit\n')

    # main menu selections and game start (important, don't accidentally delete again)
    def gameplay():
        game_menu()
        try:
            mainmenu_select = int(input('Select: '))
            if mainmenu_select > 3 or mainmenu_select < 1: #mainmenu_select in [1, 2, 3]
                gameplay()
        except ValueError:
            gameplay()
        os.system('clear')
        if mainmenu_select == 1:
            difficulty_select()
        elif mainmenu_select == 2:
            os.system('clear')
            print("\nThe Story:\nYou control an adventurer who, after stealing a valued artifact from a native tribe, is being chased. Guide him through the various maps to safety.")
            print("\nControls:\n Use W,A,S,D keys to move.\n W = UP\n S = Down\n A = Left\n D = Right")
            print("\nDeveloped by A_Maze.inc")
            submenu_select = input('\nPress enter to continue. ')
            if submenu_select == '':
                main()
            else:
                main()
        elif mainmenu_select == 3:
            os.system('clear')
            print('Good Bye!')
            quit()

    # submenu of newgame submenu
    def difficulty_select():
        try:
            print('\nChose a difficulty:\n 1. Easy (5 lives)\n 2. Normal (3 lives)\n 3. Dark Souls (1 life)\n')
            diff_menu_select = int(input('Select: '))
            if diff_menu_select >= 1 and diff_menu_select <= 3:
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
            else:
                os.system('clear')
                difficulty_select()
        except ValueError:
            os.system('clear')
            difficulty_select()

    # movement functions for 24/7 user input support (incl super-secret gm cheatcode)
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

    # game story texts for imporved immersion depth
    def story(scenario):
        if scenario == 1:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")
        elif scenario == 2:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")
        elif scenario == 3:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")
        elif scenario == 4:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")
        elif scenario == 5:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")
        elif scenario == 6:
            os.system('clear')
            readbedtimestory(scenario-1)
            cont = input("\nPress enter to continue.")

    def readbedtimestory(scenario):
        with open('story.txt') as f:
            read = f.readlines()
            print(read[scenario])

    # map handling for enhanced UTF-8 and .txt experience
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

    # next map counter for dynamic level loading system implementation
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
            print('\nCongratulations ' + name + '!' + '\nYou managed to get away from the bloodthirsty cannibals and hid in a cave safely... \n...or did you?')
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

'''
review:

good:
variable naming (noun)
no code outside functions
lenght of functions not too big

bad:
global variables remain
nested functions in this type of use not particularly preferable: useless to put everything within main()
function naming (should be: verb + something)
functions do not end (can cause stackoverflow)
not used "return" in functions
'''
