from main_menu_functions import main_menu_page
import sys

def reprompt_help():
    print("Invalid input, please try again.")
    print("Press '1' to Go Back: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option


def help_page():
    print("\nHelpful Information\n")
    print("Pressing '1' to 'generate a movie' will show you the title, director,\n" 
    "and release year of a randomly chosen movie.\n")

    print("After pressing '1', you will be given the option to enter a genre. If \n"
    "you enter a genre, the randomly chosen movie will be limited to within \n"
    "that genre(for example, if you enter 'comedy', 'Jaws' will not be generated).\n")

    print("If you enter a genre that the computer doesn't recognize, it will ask you \n"
    "to try again (maybe broaden your search, try 'horror' instead of 'murder \n"
    "mystery').\n")

    print("If you leave the genre field empty, the movies that can be generated \n"
    "will not be limited and you may see any genre of movie through your \n"
    "search.\n")

    print("After generating a movie, you may choose to learn more about it or to\n"
    "generate an entirely new result (be careful though, the previous\n"
    "recommendation will be lost upon requesting a new one).\n")

    print("If you choose to view the streaming services a movie is on, it will\n"
          "show the services that are subscription-based. If a movie is 'available\n"
          "for rent' on a streaming service, that service will not be included.\n")

    print("Pressing '3' to 'go back' will take you back to the page before\n"
    "the one you are currently on (for example, if you choose to 'go back' \n"
    "whilst on the main menu, you will return to the intro display.\n")

    print("Pressing '0' to 'exit' will remove you from the application.\n")

    print("Example use of the app: Sammie opens Media Mixer, presses '1' to continue,\n"
    "then presses '1' again to generate a recommendation. Sammie is in the mood for \n"
    "something funny, so when they are asked to input a genre, they enter 'comedy'. The \n"
    "movie they are shown is 'Step Brothers' (2008) directed by Adam McKay. Sammie saw \n"
    "'Step Brothers' recently, so they want a different recommendation. They press '2' \n"
    "to generate a new movie. The movie they are shown is 'No Hard Feelings' (2023) \n"
    "directed by Gene Stupnitsky. That sounds interesting to Sammie, so they press '1' \n"
    " to discover what streaming services 'No Hard Feelings' is on. They find out it is \n"
    "streaming on Netflix. They are satisfied with that recommendation, so they press '0' \n"
    "to exit the application. \n")

    print("Press '1' to Go Back: ")
    user_help_option = int(input("Press '0' to Exit: "))
    while user_help_option != 1 and user_help_option != 0:
        user_help_option = reprompt_help()
    if user_help_option == 1:
        main_menu_page()
    else:
        sys.exit()

