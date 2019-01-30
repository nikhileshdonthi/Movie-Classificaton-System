movies=[]


def menu():
    user_input = input("Enter 'a' to add a movie,'l' to see movies,'f' to find a movie, and 'q' to quit: ")
    while user_input!='q':

        if user_input == 'a':
            add_movie()
        elif user_input == 'l':
            show_movies()
        elif user_input == 'f':
            find_movie()
        else:
            print("Not a correct option. Please try again")
        user_input = input("Enter 'a' to add a movie,'l' to see movies,'f' to find a movie, and 'q' to quit: ")
    print("Thank you for using the Programs")

def add_movie():
    """
    movie={
        'name':...(str),
        'year':...(int),
        'director':...(str)
    }
    """
    name = input("Enter movie name : ")
    year =input("Enter year : ")
    director = input("Enter director : ")

    movies.append({
        'name': name,
        'year': year,
        'director': director
    })

def show_movies():


    for i in movies:
        show_movies_orders(i)

def show_movies_orders(i):
        print(f"The movie name is {i['name']}, released in {i['year']} and director is {i['director']}\n")

def find_movie():
    find_by= input("Pleas press 'name' to find by name,'year' to find by year and 'director' to find by director")
    looking_for=input("Please enter the attribues")
    ml=[]
    for i in movies:
        if i[find_by]==looking_for:
            ml.append(i)
    for i in ml:
        show_movies_orders(i)


menu()





