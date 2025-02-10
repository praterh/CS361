#display, continue to main menu, exit
import sys


def display_intro():
    print("Welcome to Media Mixer!\n")
    print("Are you bored, but don't know what you want to do?")
    print("Media Mixer is here for you with randomly-generated media recommendations!")
    print("Just enter the genre you're in the mood for and get inspired!")
    print("(Or leave the genre field empty for a true surprise)\n")
    print("Press '1' to Continue: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def reprompt_intro_option():
    print("Invalid input, please try again.")
    print("Press '1' to Continue: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def intro_page():
    user_intro_option = display_intro()
    while user_intro_option != 1 and user_intro_option != 0:
        user_intro_option = reprompt_intro_option()
    if user_intro_option == 1:
        from main_menu_functions import main_menu_page
        main_menu_page()
    else:
        sys.exit()

intro_page()
