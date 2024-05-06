import os
import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

from user import User
from book import Book
from author import Author


def main_library():
    books = []
    users = []
    authors = []
    current_user = None

    while True:
        print(Style.BRIGHT + "\nWelcome to the Library Management System!")
        print("\nMain Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Quit")
        choice = input('\nPlease enter menu option to proceed: ')
            
        if choice == '1':
            os.system('clear')
            current_user = book_ops(books, authors, current_user)
        elif choice == '2':
            current_user = user_ops(users, current_user)
        elif choice == '3':
            os.system('clear')
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '\nThanks for visiting the Library\n')
            return
        else:
            os.system('clear')
            print(Style.BRIGHT + Fore.RED + '\nInvalid input, please use 1 ,2 ,3 ,4')

def book_ops(books, authors, current_user):
    if current_user is None:    #---In order to track users, Book Operations will not run unless there is an active user
        print(Style.BRIGHT + Fore.RED + "No user currently logged in. Please log in via " + Style.BRIGHT + "User Operations.")
        return current_user
    
    while True:
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Display all authors")
        print("7. Return to main menu")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            print(f'\nCurrent user is {Style.BRIGHT + current_user.name.title()}')
            new_book = add_new_book(authors)
            if new_book:
                books.append(new_book)

        elif choice == '2':
            if not books:
                print("No books available in the collection.")
                continue
            print()
            for idx, book in enumerate(books):
                if book.availability:
                    print(f'{idx + 1}.) {book.get_info()}')
            book_num = int(input('\nEnter the NUMBER of the book you want to borrow: ')) 
            book = books[book_num - 1]
            current_user.borrow(book)   #---Calls borrow method in the User class

        elif choice == '3':
            title = input("\nEnter the title of the book to return: ").strip().lower()
            current_user.return_book(title) #---Calls return method in user class
        elif choice == '4':
            search_book(books)
        elif choice == '5':
            if not books:   
                print("No books available in the collection.")
            else:
                os.system('clear')
                print(Style.BRIGHT + "\nAll Books in Collection:")
                for idx, book in enumerate(books):
                    print(f"{idx + 1}. {book.get_info()}")
        elif choice == '6':
            display_authors(authors)
        elif choice == '7':
            os.system('clear')
            break
        else:
            print(Style.BRIGHT+ "\nInvalid choice, please select from 1-6.")
    return current_user

def add_new_book(authors):
    #---Created this in order to be able to add authors to a list with their bio. It's not a good implementation
    #---because I created a redundancy with asking for the authors name twice. It doesnt duplicate books so it still
    #---outputs relatively nicely but in hindsight this was a bad idea
    author_choice = input("Enter 'new' to add a new author, or an existing author's name: ").strip().lower()
    if author_choice == 'new':
        author = add_new_author()   #---Calls the new author function
        authors.append(author)
    else:   #---This iterates throuhg the list of authors and if the author that the user entered already exists in the 
            #--- authors list, it sets the author value in Author class. Again, this was not good implementation because I immediately ask
            #--- the user to enter the author a second time since that time the author value is going into the Book class
        author = None   #---sets a consistent value for 'author' as the for loop executes and checks for a match
        for a in authors:
            if a.name.lower() == author_choice:
                author = a
                break
        if not author:
            print("Author not found. Please add a new author.")
            return
    title = input("Enter the book title: ").strip().lower()
    author = input("Enter the author's name: ").strip().lower()
    genre = input("Enter the genre: ").strip().lower()
    while True: #---Implemented the try and except here to validate ints. COULD have added extra validation
                #--- to keep the length of of the library ID's consistent. Note for next time.
        try:
            publication_year = int(input("Enter the publication year(####): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric year value.")
    book = Book(title, author, genre, publication_year) 
    os.system('clear')
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Book added successfully!")
    return book

def add_new_author():
    name = input("Enter the author's name: ").strip().lower()
    bio = input("Enter the author's biography: ").strip().lower()
    os.system('clear')
    print('''\nNew author added to database!
           
          Continue with confirming and adding book details...''')
    print()
    return Author(name, bio)

def search_book(books):
    os.system('clear')
    if books:
        title = input("\nEnter the title of the book you are searching for: ").strip().lower()
        for book in books:
            if book.title.lower() == title:
                print('Book was found')
                print(book.get_info())
                break
        else:
            print("No books found with that title.")
    else:
        print('No books in library')
            
def display_all_books(books):
        for book in books:
            print(book.get_info())  #---Calls method in Book class

def display_authors(authors):
    os.system('clear')
    if authors:
        print(Style.BRIGHT + "\nList of Authors:")
        for author in authors:
            print(author.get_info())    #---calls method in Author class
    else:
        print("No authors found.")

def user_ops(users, current_user):
    os.system('clear')
    while True:
        print(Style.BRIGHT + "\nUser Operations:")
        print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")
        if choice == '1':
            while True:
                name = input("\nEnter the user's name: ").strip()
                while True: #---Try and Except again just to validate ints
                    try:
                        library_id = int(input("Enter the user's Library ID (####): ").strip())
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid numeric library ID.")
                new_user = User(name, library_id)
                users.append(new_user)
                os.system('clear')
                print(f"\n{Style.BRIGHT + name.title() + Style.RESET_ALL} was added successfully!")
                if not current_user:    #---Sets the newly created user as the current user
                    current_user = new_user
                break
                
        elif choice == '2':
            if not users:
                print(Style.DIM + Fore.LIGHTRED_EX + "\nNo users found. Please add a user first.")
                continue
            print()
            os.system('clear')
            for idx, user in enumerate(users):
                print(f"{idx + 1}). {user.name.title()}")
            user_num = int(input("\nSelect a user by number to view details and make them the current user: "))
            current_user = users[user_num - 1]  #---Effectively allows the user to select whatever user they want to operate under
            os.system('clear')
            print(Style.BRIGHT + "\nUser Details:")
            print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
            print(f"Name: {current_user.name.title()}")
            print(f"Library ID: {current_user.get_library_id()}")
            print(f'\n{current_user.name.title()} is now the current user')

        elif choice == '3':
            if not users:
                print(Style.DIM + Fore.LIGHTRED_EX + "\nNo users found. Please add a user first.")
            else:
                os.system('clear')
                print('\nHere is your list of users')
                print('⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺')
                for user in users:
                    print(f"{Style.BRIGHT + user.name.title()}:")
                    user.borrowed_display() #---calls the method in User class

        elif choice == '4':
            os.system('clear')
            break
        else:
            print("Invalid choice, please select from 1-4.")
    return current_user

main_library()