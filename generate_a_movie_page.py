#prompt for genre, generate a movie, display, go to streaming, go to movie, go to main menu, exit

import json
import random
import sys

with open('data.json', 'r') as f:
    data = json.load(f)

def display_genre_prompt():
    genre = str(input("\nEnter a genre in all lowercase letters (or leave blank for a true surprise): "))
    return genre

def test_genre(genre):
    bad = False
    if genre == "":
        return bad
    movie_array = [movie for movie in data['movies'] if movie['genre'] == genre]
    if len(movie_array) == 0:
        bad = True
        return bad
    return bad

def reprompt_genre():
    genre = str(input("That didn't match any genres in Media Mixer's database, make sure you're using all lowercase "
    "and maybe try broadening your search: "))
    return genre

def get_genre():
    user_genre = display_genre_prompt()
    is_genre_bad = test_genre(user_genre)
    while is_genre_bad:
        user_genre = reprompt_genre()
        is_genre_bad = test_genre(user_genre)
    return user_genre

def generate_a_movie(user_genre, random_index):
    if user_genre == "":
        movie_array = [movie for movie in data['movies']]
    else:
        movie_array = [movie for movie in data['movies'] if movie['genre'] == user_genre]

    placeholder_index = random_index
    while placeholder_index == random_index:
        random_index = random.randint(0, (len(movie_array) - 1))
    random_movie = movie_array[random_index]
    return random_movie, random_index

def are_you_sure_regenerate(movie_title):
    print(f"\nAre you sure you want to generate a new movie? You'll "
          f"lose the chance to learn more about '{movie_title}'.\n")
    print("Press '1' to Continue: ")
    user_sure_input = int(input("Press '2' to Go Back: "))
    return user_sure_input

def display_movie(user_genre, movie_title, movie_year, movie_director):
    if user_genre == "":
        print("\nThe movie you generated is...\n")
    else:
        print(f"\nThe {user_genre} movie you generated is...\n")
    print(f"{movie_title} ({movie_year}) directed by {movie_director}\n")

def display_generate_a_movie(movie_title):
    print(f"Press '1' to See Where {movie_title} is Streaming:")
    print("Press '2' to Generate a New Movie: ")
    print("Press '3' to Go Back: ")
    user_movie_option = int(input("Press '0' to Exit: "))
    return user_movie_option

def reprompt_movie_option(movie_title):
    print("Invalid input, please try again.")
    print(f"Press '1' to See Where {movie_title} is Streaming:")
    print("Press '2' to Generate a New Movie: ")
    print("Press '3' to Go Back: ")
    user_movie_option = int(input("Press '0' to Exit: "))
    return user_movie_option

def generate_a_movie_page(user_genre, random_index, streaming, movie):
    are_you_sure_option = 2
    if streaming == "not yet":
        movie, random_index = generate_a_movie(user_genre, random_index)
    streaming = "not yet"
    display_movie(user_genre, movie['title'], movie['year'], movie['director'])
    while are_you_sure_option == 2:
        are_you_sure_option = 1
        user_movie_option = display_generate_a_movie(movie['title'])
        while user_movie_option < 0 or user_movie_option > 3:
            user_movie_option = reprompt_movie_option(movie['title'])
        if user_movie_option == 1:
            from streaming_service import streaming_page
            streaming_page(random_index, movie, user_genre, streaming)
        elif user_movie_option == 2:
            are_you_sure_option = are_you_sure_regenerate(movie['title'])
            if are_you_sure_option == 2:
                continue
            else:
                generate_a_movie_page(user_genre, random_index, "not yet", movie)
        elif user_movie_option == 3:
            from main_menu_functions import main_menu_page
            main_menu_page()
        else:
            sys.exit()
