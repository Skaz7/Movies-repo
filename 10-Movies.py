import os
import json
from datetime import date
import time

choice = -1 # Deklaracja opcji wybór
movies = [] # Tworzenie pustej listy filmów
genres = [] # Tworzenie pustej listy gatunków
current_year = date.today().year

#########################################################################
# Czyszczenie ekranu

def clear_screen():

    os.system('cls')

#########################################################################
# Wyświetlenie samych tytułów

def show_titles_only():

    clear_screen()
    for i in range(len(movies)):
        print(i + 1, ". ", '"', movies[i][0], '"', sep = "")

    if input("\n0 - BACK ") =="0":
        return  

#########################################################################
# Wyświetlenie kompletnej bazy

def full_database():

    clear_screen()
    for i in range(len(movies)): # Pętla przechodząca przez wszystkie filmy po kolei
        print("\n", i + 1, ". ", '"', movies[i][0], '": ', sep = "") # movies[i to kolejny film][0] to pierwszy element listy tego filmu
        print("\t\t", "Year    -", movies[i][1])                     # movies[i to kolejny film][1] to drugi element listy tego filmu
        print("\t\t", "Length  -", movies[i][2], "min")              # j.w.
        print("\t\t", "Genre   - ", end = "") 

        if len(movies[i][3][0]) > 1:         # Jeśli film ma więcej niż 1 gatunek:
            print(*movies[i][3], sep = ", ") # to drukuj w jednej linii, gatunki z zagnieżdżonej listy oddzielone ,
        else:                                # Jeśli film ma tylko jeden gatunek:
            print(*movies[i][3], sep = "")   # to drukuj ten gatunek bez seraparorów (żeby uniknąć 'h o r r o r')

        print("\t\t", "Country -", movies[i][4])

    if input("\n0 - BACK ") =="0":
        return  

#########################################################################
# Wyświetlanie detali filmów wg liter alfabetu

def details_by_letter():

    clear_screen()
    start_letter = str(input("Which letter should the movie begin with? : ")).upper()
    selected_movies = [movie for movie in movies if str(movie[0]).startswith(start_letter)]
    if len(selected_movies) == 0:
        print("No movie starts with '" + start_letter + "'. ")
    
    for i in range(len(selected_movies)): # Pętla przechodząca przez wszystkie filmy po kolei
        print("\n", i + 1, ". ", '"', selected_movies[i][0], '": ', sep = "") # movies[i to kolejny film][0] to pierwszy element listy tego filmu
        print("\t\t", "Year    -", selected_movies[i][1])                     # movies[i to kolejny film][1] to drugi element listy tego filmu
        print("\t\t", "Length  -", selected_movies[i][2], "min")              # j.w.
        print("\t\t", "Genre   - ", end = "") 

        if len(selected_movies[i][3][0]) > 1:         # Jeśli film ma więcej niż 1 gatunek:
            print(*selected_movies[i][3], sep = ", ") # to drukuj w jednej linii, gatunki z zagnieżdżonej listy oddzielone ,
        else:                                # Jeśli film ma tylko jeden gatunek:
            print(*selected_movies[i][3], sep = "")   # to drukuj ten gatunek bez seraparorów (żeby uniknąć 'h o r r o r')

        print("\t\t", "Country -", selected_movies[i][4])

    if input("\n0 - BACK ") =="0":
        return   

#########################################################################
# Wyszukiwanie filmu

def search_movie():

    clear_screen()
    search_movie_choice = -1
    
    print("1 - Search by Title")
    print("2 - Search by Year")
    print("3 - Search by Genre")
    print("4 - Search by Country")

    if search_movie_choice != 0:
        try: 
            search_movie_choice = int(input("\n0 - BACK \n\nSearch movies by: "))
            if search_movie_choice < 0 or search_movie_choice > 4:
                print("\nWrong option, choose again.\n")
                return
            elif search_movie_choice == 1:
                search_movie_by_title()

            elif search_movie_choice == 2:
                search_movie_by_year()

            elif search_movie_choice == 3:
                search_movie_by_genre()
            
            elif search_movie_choice == 4:
                search_movie_by_country()
                
        except ValueError:
            print("-" * 33)
            print("\n|  Wrong option, choose again.  |\n")
            print("-" * 33)
            return
    if search_movie_choice == 0:
        main_screen()

#########################################################################
# Wyświetlanie filmu wg wpisanego tytułu

def search_movie_by_title():

    while True:

        searched_movie = input("Movie title: ").lower()

        if searched_movie == "0":
            search_movie()
        else:
            result = [movie for movie in movies if searched_movie in movie[0].lower()]

            if result == []:
                print("-" * (24 + len(searched_movie)))
                print('|  Movie "' + searched_movie + '" not found  |')
                print("-" * (24 + len(searched_movie)))
                time.sleep(2)
                search_movie()
            else:
                for title in result:
                    print('\n"' + title[0] + '":')
                    print("\t\t Year    -", title[1])
                    print("\t\t Length  -", title[2], 'min')
                    print("\t\t Genre   - ", end = "") 

                    if len(title[3][0]) > 1:         # Jeśli film ma więcej niż 1 gatunek:
                        print(*title[3], sep = ", ") # to drukuj w jednej linii, gatunki z zagnieżdżonej listy oddzielone ,
                    else:                                # Jeśli film ma tylko jeden gatunek:
                        print(*title[3], sep = "")   # to drukuj ten gatunek bez seraparorów (żeby uniknąć 'h o r r o r')

                    print("\t\t", "Country -", title[4])
                    print()
                    continue

#########################################################################
# Wyświetlanie filmu wg roku

def search_movie_by_year():

    searched_year = -1

    while True:
        if searched_year != 0:
            try:
                searched_year = int(input("\nEnter year of movie you want to find: "))
                if searched_year < 1895 or searched_year > current_year: 
                    print("\nYear must be between 1895 and current year.\n")
                    continue
            except ValueError:
                print()
                print("-" *22)
                print("| Wrong year format! |")
                print("-" *22, "\n")
                continue
            else:
                result = [movie for movie in movies if searched_year == movie[1]]

                if result == []:
                    print()
                    print("-" * 23)
                    print('| Year', searched_year, 'not found |')
                    print("-" * 23, "\n")
                else:
                    for year in result:
                        print('\n"' + year[0] + '":')
                        print("\t\t Year    -", year[1])
                        print("\t\t Length  -", year[2], 'min')
                        print("\t\t Genre   - ", end = "") 

                        if len(year[3][0]) > 1:         # Jeśli film ma więcej niż 1 gatunek:
                            print(*year[3], sep = ", ") # to drukuj w jednej linii, gatunki z zagnieżdżonej listy oddzielone ,
                        else:                                # Jeśli film ma tylko jeden gatunek:
                            print(*year[3], sep = "")   # to drukuj ten gatunek bez seraparorów (żeby uniknąć 'h o r r o r')

                        print("\t\t", "Country -", year[4])
                        print()
                continue
        else:
            search_movie()


#########################################################################
# Wyświetlanie filmu wg gatunku

def search_movie_by_genre():

    genres.sort() 
    print("\nAvailable genres:\n")
    
    for i, genre in enumerate(genres, start = 1):
        print(i, genre)
    print("\n0 - BACK")

    while True:

        selected_genre = -1

        try:
            selected_genre = int(input("\nWhich genre to find? : "))

            if selected_genre == 0:
                search_movie()
            elif selected_genre < 0 or selected_genre > len(genres):
                print("\nWrong number!\n")
                continue
            else:
                selected_genre = genres[selected_genre - 1]
                print("\n\n", selected_genre.capitalize(), "movies:\n")
                for movie in range(len(movies)):
                    if selected_genre in movies[movie][3]:
                        print('"' + movies[movie][0] + '"')
                        print("\t\tYear     - ", movies[movie][1])
                        print("\t\tLength   - ", movies[movie][2])
                        print("\t\tGenre    -  ", end = "")

                        if type(movies[movie][3]) is list != True:      
                            print(*movies[movie][3], sep = ", ") 
                        else:                             
                            print(*movies[movie][3], sep = "")  
                        print("\t\tCountry  - ", movies[movie][4])
                        print()
                        
        except ValueError:
            print("\nWrong format!")

#########################################################################
# Wyświetlanie filmu wg kraju

def search_movie_by_country():

    countries = set()
    print()

    for country in movies:
        countries.add(country[4])

    countries = sorted(countries)

    for i, country in enumerate(countries, start = 1):
        print(i, country)
    
    while True:
        try:
            selected_country = int(input("\n0 - BACK \n\nSelect country: "))
        except ValueError:
            print("\nWrong country format...\n")
            continue

        if selected_country == 0:
            search_movie()
        elif selected_country < 0 or selected_country > len(countries):
            print("\nCountry number must be between 1 and ", len(countries))
            continue
        else:
            countries = list(countries)

            for movie in range(len(movies)):
                if movies[movie][4] == countries[selected_country - 1]:
                    print('"' + movies[movie][0] + '"')
                    print("\t\tYear     - ", movies[movie][1])
                    print("\t\tLength   - ", movies[movie][2])
                    print("\t\tGenre    -  ", end = "")

                    if type(movies[movie][3]) is list != True:      
                        print(*movies[movie][3], sep = ", ") 
                    else:                             
                        print(*movies[movie][3], sep = "")  
                    print("\t\tCountry  - ", movies[movie][4])
                    print()
                else:
                    continue

#########################################################################
# Wyświetlanie opcji

def show_options():

    clear_screen()

    print("1 - Add movie.")
    print("2 - Edit movie.")
    print("3 - Delete movie.")
    print("4 - Add genre.")
    print("5 - Delete genre.")
    print("\n0 - BACK\n")

    options_choice = input("Choose an option: ")
    
    if options_choice == '1':
        add_movie()
    elif options_choice == '2':
        edit_movie()
    elif options_choice == '3':
        delete_movie()
    elif options_choice == '4':
        add_genre()
    elif options_choice == '5':
        delete_genre()
    elif options_choice == '0':
        return
    else:
        print("Wrong option!")

#########################################################################
# Dodawanie filmu do bazy    

def add_movie():

    clear_screen()
    add_title = str(input("Title: ")).title() # title z modułu string zmienia wielkość pierwszych liter z tytułu na wielkie
    
    while True: # Pętla sprawdzająca żeby rok był właściwego formatu i nie wykraczał poza historię kina
        try:
            add_year = int(input("\nYear: "))

            if add_year < 1895 or add_year > current_year:
                print("\nYear must be between 1895 - today...")
                continue
        except ValueError:
            print("\nWrong year format!")
            continue
        else: 
            break
    
    while True: # Pętla sprawdzająca żeby długość była liczbą całkowitą
        try:
            add_length = int(input("\nLength: "))
        except ValueError:
            print("\nWrong length format!")
            continue
        else:
            break

    genres.sort() 
    print("Available genres:")
    
    for i, genre in enumerate(genres, start = 1):
        print(i, genre)
    
    # Dodawanie jednego lub kilku gatunków do filmu
    add_genres = []
    add_genre = -1
    while True:
        try:
            add_genre = int(input("\nMovie genre? (0 - Stop adding genres): "))

            if add_genre == 0:
                break

            elif add_genre < 0 or add_genre > len(genres):
                print("\nWrong genre number!")

            else:
                add_genre1 = genres[add_genre - 1]
                add_genres.append(add_genre1)

        except ValueError:
            continue
        else: 
            continue
    
    add_country = str(input("Country: "))

    movies.append([add_title, add_year, add_length, add_genres, add_country])

#########################################################################
# Edycja informacji o filmie

def edit_movie():

    clear_screen()

    for i, title in enumerate(movies, start = 1): 
        print(i, title[0])
    print("\n0 - Back")
    
    while True:     # Pętla sprawdzająca żeby długość była liczbą całkowitą
        try:
            movie_to_edit = int(input("\nWhich movie do you want to edit? "))
        except ValueError:
            print("Choose actual movie number...")
            continue
        else:
            if movie_to_edit < 0 or movie_to_edit > len(movies):
                print("Wrong number!")
                continue
            if movie_to_edit == 0:
                clear_screen()
                return
            else:
                break
    print("\nYou are editing:")
    print("\n\tTitle: ", movies[movie_to_edit - 1][0])
    print("\t\t\t", "Year    -", movies[movie_to_edit - 1][1])                     
    print("\t\t\t", "Length  -", movies[movie_to_edit - 1][2], "min")              
    print("\t\t\t", "Genre   - ", end = "") 

    if len(movies[movie_to_edit - 1][3][0]) > 1:         # Jeśli film ma więcej niż 1 gatunek:
        print(*movies[movie_to_edit - 1][3], sep = ", ") # to drukuj w jednej linii, gatunki z zagnieżdżonej listy oddzielone ,
    else:                                                # Jeśli film ma tylko jeden gatunek:
        print(*movies[movie_to_edit -1][3], sep = "")    # to drukuj ten gatunek bez seraparorów (żeby uniknąć 'h o r r o r')

    print("\t\t\t", "Country -", movies[movie_to_edit -1][4])        

    edit_title = str(input("\nEdited Title: ")).title()  # title z modułu string zmienia wielkość pierwszych liter z tytułu na wielkie
    
    while True:
        try:
            edit_year = int(input("\nEdited Year: "))

        except ValueError:
            print("Wrong year!")
            continue
        
        if edit_year < 1895 or edit_year > current_year:
            print("\nWrong year!")

        else: 
            break   # jeśli nie ma błędu formatu roku to wyjdź z pętli while True
    
    while True: # Pętla sprawdzająca żeby długość była liczbą całkowitą
        try:
            edit_length = int(input("\nEdited Length: "))
        except ValueError:
            print("\nWrong length format!")
            continue
        else:
            break

    genres.sort()
    print("\nAvailable genres:")

    for i, genre in enumerate(genres, start=1):
        print(i, genre)

    # Dodawanie jednego lub kilku gatunków do filmu
    edit_genres = []
    edit_genre = -1
    while True:
        try:
            edit_genre = int(input("\nMovie genre? (0 - Stop adding genres): "))

            if edit_genre == 0:
                break

            elif edit_genre < 0 or edit_genre > len(genres):
                print("\nWrong genre number!")

            else:
                edit_genre1 = genres[edit_genre - 1]
                edit_genres.append(edit_genre1)

        except ValueError:
            continue
        else: 
            continue
   
    edit_country = str(input("\nEdited Country: "))

    movies[movie_to_edit - 1][0] = edit_title
    movies[movie_to_edit - 1][1] = edit_year
    movies[movie_to_edit - 1][2] = edit_length
    movies[movie_to_edit - 1][3] = edit_genres
    movies[movie_to_edit - 1][4] = edit_country

#########################################################################
# Usuwanie filmu z bazy

def delete_movie():
    
    clear_screen()

    show_titles_only()

    while True:     # Pętla sprawdzająca żeby długość była liczbą całkowitą
        try:
            movie_to_delete = int(input("\nMovie to delete: "))
        except ValueError:
            print("\nChoose actual movie number...")
            continue
        else:
            if movie_to_delete < 1 or movie_to_delete > len(movies):
                print("\nWrong movie number!")
                continue
            else:
                break

    movies.pop(movie_to_delete - 1)
    print("\nMovie deleted...")
    return

#########################################################################
# Dodawanie gatunku

def add_genre():

    genres.sort()
    clear_screen()

    print("Available genres:\n")
        
    for i, genre in enumerate(genres, start = 1):
        print(i, genre)
    
    print("\n0 - Back\n")
        
    add_genre = str(input("\nWhat is the new genre: ")).capitalize()
    while add_genre != "0":
        genres.append(add_genre)
        clear_screen()
        return

#########################################################################
# Usuwanie gatunku

def delete_genre():

    genres.sort()
    clear_screen()

    print("\nAvailable genres:")
    
    for i, genre in enumerate(genres, start = 1):
        print(i, genre)
    
    print("\n0 - Back\n")

    while True:     # Pętla sprawdzająca żeby długość była liczbą całkowitą
        try:
            genre_to_delete = int(input("\nNumber of genre to delete: "))
        except ValueError:
            print("\nChoose actual genre number...")
            continue
        else:
            if genre_to_delete != 0:
                if genre_to_delete > len(genres):
                    print("\nWrong genre number!")
                    continue
                else:
                    del genres[genre_to_delete - 1]
        return

#########################################################################
# Zapisanie filmów do pliku

def save_list_to_file():

    with open("movies.json", "w") as file:
        json.dump(movies, file, indent = 4)
      
    with open("genres.json", "w") as file:
        json.dump(genres, file, indent = 4)

#########################################################################
# Wyjście z programu z zapisaniem zmian do pliku

def exit_program():

    while True:

        print(          "------------------------------------")
        confirm = input("Do you want to save changes? (Y/N): ")
        if "y" in confirm.lower():
            save_list_to_file()
            print("\nDatabase saved successfully.")
            print("\nGoodbye...\n\n")
            quit()
        elif "n" in confirm.lower():
            print("\nDatabase not saved!\n")
            print("Goodbye...\n\n")
            quit()
        else:
            print("Wrong answer.\n\n")
            continue

#########################################################################
# Główne menu

def main_screen():

    clear_screen()

    choice = -1

    while True: 
        if choice == '1':
            clear_screen()
            show_titles_only()
        if choice == '2':
            clear_screen()
            full_database()
        if choice == '3':
            clear_screen()
            details_by_letter()
        if choice == '4':
            clear_screen()
            search_movie()
        if choice == '9':
            show_options()
        if choice == "0":
            clear_screen()
            exit_program()

        movies.sort()
        clear_screen()
        print("\n\n1 - Movies list.")
        print("2 - Full info.")
        print("3 - Movie details by letter.")
        print("4 - Search for a movie.")
        print("9 - Options.\n")
        print("0 - EXIT.\n")

        choice = input("What's your choice: ")
        print("\n\n")


#########################################################################
## START ##

with open("movies.json") as file:
    movies = json.load(file)        # Wczytanie listy filmów

with open("genres.json") as file:
    genres = json.load(file)        # Wczytanie listy gatunków

main_screen()