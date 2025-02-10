import sys

def display_streaming_info(random_movie):
    print(f"\n{random_movie['title']} Streaming Services: \n")
    for service in random_movie['streaming_services']:
        print(service)

def display_streaming_menu():
    print("\nPress '1' to Generate a New Movie: ")
    print("Press '2' to Go Back: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def reprompt_streaming_menu():
    print("Invalid input, please try again.")
    print("Press '1' to Generate a New Movie: ")
    print("Press '2' to Go Back: ")
    user_option = int(input("Press '0' to Exit: "))
    return user_option

def streaming_page(random_index, random_movie, genre, streaming):
    display_streaming_info(random_movie)
    user_stream_option = display_streaming_menu()
    while user_stream_option < 0 or user_stream_option > 3:
        user_stream_option = reprompt_streaming_menu()
    if user_stream_option == 1:
        from generate_a_movie_page import generate_a_movie_page
        generate_a_movie_page(genre, random_index, "not yet", "")
    elif user_stream_option == 2:
        from generate_a_movie_page import generate_a_movie_page
        generate_a_movie_page(genre, random_index, "yes", random_movie)
    else:
        sys.exit()