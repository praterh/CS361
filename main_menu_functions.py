#display, go to generated a movie, go to help, go back to intro, exit
import sys

def display_main_menu():
    print("\nGet Recommendations!\n")
    print("Press '1' to Generate a Movie: ")
    print("Press '2' for Help: ")
    print("Press '3' to Go Back: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def reprompt_main_menu_option():
    print("Invalid input, please try again.")
    print("Press '1' to Generate a Movie: ")
    print("Press '2' for Help: ")
    print("Press '3' to Go Back: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def main_menu_page():
    user_menu_option = display_main_menu()
    while user_menu_option < 0 or user_menu_option > 3:
        user_menu_option = reprompt_main_menu_option()
    if user_menu_option == 1:
        from generate_a_movie_page import get_genre, generate_a_movie_page
        user_genre = get_genre()
        generate_a_movie_page(user_genre, -1, "not yet", "")
    elif user_menu_option == 2:
        from help import help_page
        help_page()
    elif user_menu_option == 3:
        from intro_functions import intro_page
        intro_page()
    else:
        sys.exit()
