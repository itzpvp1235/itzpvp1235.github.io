# Inporting

import random
import time
import os
import pprint
import tkinter as tk

# CODE
# Captcha
print("Please wait, loading CAPTCHA...")

root = tk.Tk()
T = tk.Text(root, height=5, width=100)
T.pack()
T.insert(tk.END, "CAPTCHA:\nPlease close this window to prove that you are not a robot.")
tk.mainloop()

print("You passed the CAPTCHA!\n")

print("\n\n[I]For the best experiences, we recommened you to run both the installer and the game in by running it in explorer, not using a built in terminal application!")

# Setup

setup_start = False
while True:
    setup_selection = input("""----------SETUP----------
HorrorGame setup.
Please type in the following letters to access the following sub-menu

ACTIONS
                   PRESS:   TO:
 +-------------+   S        Start setup
 |             |   
 |             |   H        How to play (Instructions for setup and game)
 +---+     +---+   C        Open credits menu
     |     |      
     |     |       E        Exit the setup
  +--+     +--+    
  |           |    
  +-----------+    

Please enter a selection below:
""")

    if len(setup_selection) == 1:
        setup_selection = setup_selection.upper()
        if setup_selection == "C":
            setup_credits = input("""----------CREDITS----------

HorrorGame Credits
This game was made by the following people:

MAIN PROGRAMMER AND GRAPHICS DESIGNER:
Otto YANG

GRAPHICS DESIGNER (Ur usless)
Foster HUANG

MAIN DEBUGGER
Matti LOO

ACTIONS:
PRESS:   TO:
B        Return to main menu
Please enter a selection below:
""")

            setup_credits = setup_credits.upper()
            if setup_credits == "B":
                pass
            else:
                print("\n]I]Since you did not put in a valid answer, you have been redirected to the home page!")

        elif setup_selection == "S":

            setup_start = True
            break
        elif setup_selection == "H":
            setup_instructions = input("""----------INSTRUCTIONS----------
-Setup instructions:
    in the menu, select "start setup" then you will be prompted to change a file location, once done, press ENTER
    in the second step of setup, you will be prompted about setup mode, if you don't know what to choose, just press ENTER to start writing the files.
    after that, you are done, the setup has finished the installation, to end the setup, press ENTER

-Game instructions and controls:
    the game will start by running "HorrorGame" on the explorer window, it should be in the same directory.
    you will be prompted to enter a selection of 2 or 3, to select an option, just press the letter of the selection and press ENTER
    -How to know what selection is which:
        to know what selection is which, you will see a menu above to select from, it will be A, B or C
        you can just simply follow the steps from the game.

ACTIONS:
PRESS:   TO:
B        Go back to the home screen
""")

            setup_instructions = setup_instructions.upper()
            if setup_instructions == "B":
                pass
            else:
                print("\n]I]Since you did not put in a valid answer, you have been redirected to the home page!")
        
        elif setup_selection == "E":
            print("Terminating setup process...")
            break

if setup_start:
    print("""
                
----------SETUP----------
[...]Please wait, setup is loading...""")

    print("Done!")
    

    setup_failsafe = input("""[!]Pleaase make sure that you do not have a file called the following names!
HorrorGame
If you do, please put it in a file that is not in the current directory of this setup process!

Once done, press ENTER, if you did move the file, you may need to relaunch the program by closing the program and relaunching it!
if you do not want to move the following file(s), please exit this setup!!!

PLEASE NOTE THAT THIS PROGRAM WILL OVERWRITE ANY FILE(S) NAMED IN THE LIST ABOVE!!!

""")

    setup_write_mode = input("""[?] Please select a mode for writing the files, or press ENTER to select the recomended.

PRESS:   TO:
W        Write to file (Recomended)
A        Append to file

Please type an answer, then press ENTER.
""")

    setup_write_mode = setup_write_mode.upper()
    while True:
        if setup_write_mode == "W" or setup_write_mode == "":

            if setup_failsafe == "":
                print("[...]Please wait while setup writes the program files and game...")
                print("This process may take a couple minutes depending on your system hardware capebilities.", end = "\n\n")

                with open("HorrorGame.py", "w") as gamefile:

                    gamefile.write('''import time
import random

# Code

print("Loading game start menu, please waait...")

game_start = input("Welcome to HorrorGame, to start, press ENTER.")

print("Please wait...")

print("GAME--------")
print("""You see a random door, you are now very scared, but curious, what do you do""")
game_q1 = input("""A = Open door, B = Ignore the door
""")

game_q1 = game_q1.upper()
if game_q1 == "A":
    print("You see a chest, what do you do")
    gmae_q2 = input("""A = Open chest, B = Ignore it
""")
    gmae_q2 = gmae_q2.upper()
    if gmae_q2 == "A":
        print("The chest contained a very scary picture of a skelleton so you get scared, you hear a random sound, you freak out")
        game_q3 = input("""A = Scream for help, B = do nothing
""")
        game_q3 = game_q3.upper()
        if game_q3 == "A":
            print("You hear a person, and you see a shadow in the distance, but he looks like he has a gun in his hand!")
            game_q4 = input("""A = Risk it and hope that he dosen't shoot, B = Wait for him to come 
""")        
            game_q4 = game_q4.upper()
            if game_q4 == "A":
                print("You run for the stranger, but he is holding a gun, and killes you thinking thay you will attempt to kill him")
                print("YOU LOSE!")
            elif game_q4 == "B":
                print("The person comes, he takes you away to somewhere you have no clue about,then asks you what you have been doing, but then you dont tell him anything, so the stranger is comfused, he thinks that you can't talk, so he gives you a piece of paper to write with, then you write that you have been in a room and he takes you to a bedroom, when you soon fell asleep.")
                print("CONGRATULATIONS, YOU WON")
        
        elif game_q3 == "B":
            print("Nobody comes, and after days, you starve to death...")
            print("YOU LOSE")

    elif gmae_q2 == "B":
        print("So you ignore the chest, and a voice tells you to open it, but you don't want to. Then a preson walks into the room, and you panic, thinking that he is not a nice person, and the person demands for you to open the chest, but you dont, and the guy shoots you with a gun.")
        print("YOU LOSE")

elif game_q1 == "B":
    print("You ignore the door, then turn arround and see a picture showing the wonderful things that will happen to you if you open the door, so you do, and to your horror, you see an animal that you have never seen before, you touch it, then the animal gets angry and decides to bite you with his venomous teeth, then you die!")
    print("YOU LOSE")

print("Thanks for playing, press enter to finish")
game_end = input("Press ENTER to finish and close the game")


''')

            break
        elif setup_write_mode == "A":
            setup_write_mode_failsafe = input("""Are you sure that you want to choose this, choosing this will not create and write a file, instead it will add the text to the file, please only choose this mode if you are very sure that you do not have the file called HorrorGame!!!
Please press ENTER to continue, otherwise please terminate this program.""")
            if True:
                print("Please wait...")
                

                with open("HorrorGame.py", "a") as gamefile:

                    gamefile.write('''import time
import random

# Code

print("Loading game start menu, please waait...")

game_start = input("Welcome to HorrorGame, to start, press ENTER.")

print("Please wait...")

print("GAME--------")
print("""You see a random door, you are now very scared, but curious, what do you do""")
game_q1 = input("""A = Open door, B = Ignore the door
""")

game_q1 = game_q1.upper()
if game_q1 == "A":
    print("You see a chest, what do you do")
    gmae_q2 = input("""A = Open chest, B = Ignore it
""")
    gmae_q2 = gmae_q2.upper()
    if gmae_q2 == "A":
        print("The chest contained a very scary picture of a skelleton so you get scared, you hear a random sound, you freak out")
        game_q3 = input("""A = Scream for help, B = do nothing
""")
        game_q3 = game_q3.upper()
        if game_q3 == "A":
            print("You hear a person, and you see a shadow in the distance, but he looks like he has a gun in his hand!")
            game_q4 = input("""A = Risk it and hope that he dosen't shoot, B = Wait for him to come 
""")        
            game_q4 = game_q4.upper()
            if game_q4 == "A":
                print("You run for the stranger, but he is holding a gun, and killes you thinking thay you will attempt to kill him")
                print("YOU LOSE!")
            elif game_q4 == "B":
                print("The person comes, he takes you away to somewhere you have no clue about,then asks you what you have been doing, but then you dont tell him anything, so the stranger is comfused, he thinks that you can't talk, so he gives you a piece of paper to write with, then you write that you have been in a room and he takes you to a bedroom, when you soon fell asleep.")
                print("CONGRATULATIONS, YOU WON")
        
        elif game_q3 == "B":
            print("Nobody comes, and after days, you starve to death...")
            print("YOU LOSE")

    elif gmae_q2 == "B":
        print("So you ignore the chest, and a voice tells you to open it, but you don't want to. Then a preson walks into the room, and you panic, thinking that he is not a nice person, and the person demands for you to open the chest, but you dont, and the guy shoots you with a gun.")
        print("YOU LOSE")

elif game_q1 == "B":
    print("You ignore the door, then turn arround and see a picture showing the wonderful things that will happen to you if you open the door, so you do, and to your horror, you see an animal that you have never seen before, you touch it, then the animal gets angry and decides to bite you with his venomous teeth, then you die!")
    print("YOU LOSE")

print("Thanks for playing, press enter to finish")
game_end = input("Press ENTER to finish and close the game")

''')

            
                break
    print("[I] The setup has finished writing the files, please run the file called HorrorGame.py, it should be in this directory, if not, please try re-running the setup.")
    setup_end = input("Press ENTER to finish the installation and close the installer.")
    print("Terminating program, please wait...")
