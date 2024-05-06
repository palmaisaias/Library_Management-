import os
import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

class User:
    def __init__(self, name, library_id):
        self.name = name
        self.__library_id = library_id
        self.borrowed_books = []  
    #---I incorporated the get and set here since I made the library ID private but ultimately I dont 
    #--- like the execution. I didnt include an option to modify the library ID which i think is the 
    #---whole point of setting something as private, to validate and control the editing and accessing 
    #---of that information.
    def get_library_id(self):
        return self.__library_id
    
    def set_library_id(self, new_library_id):
        self.__library_id = new_library_id
        print("Library ID has been updated.")

    def borrow(self, book):
        if book.borrow():   #---calls the method in Book class and works with the returned bool value
            self.borrowed_books.append(book)    #---adds the book to the users borrowed list.
            os.system('clear')
            print(f'\n{Style.BRIGHT + self.name.title()} has borrowed the book')
        else:
            print(f'not available for borrowing')
    
    def borrowed_display(self): #---I liked this because under 'Display all users' I give the user visibility
                                #---of not only the list of users but any books they have currently borrowed
        print(f"{self.name.title()}'s Borrowed Books:")
        if self.borrowed_books:
            for book in self.borrowed_books:
                print(book.title.title())
                print()
        else:
            print("No books currently borrowed\n")

    def return_book(self, title):   #---This method allows a user to return a book using its title
        for b, borrowed_book in enumerate(self.borrowed_books): #---loops through the index and the borrowed book object
            if borrowed_book.title.lower() == title.lower():
                self.borrowed_books.pop(b)  #---used pop to remove the book from the borrowed books list
                print(f"{Style.BRIGHT + borrowed_book.title.title()} has been returned.")
                borrowed_book.availability = True   #---makes book available again
                return
        print(Style.BRIGHT + Fore.RED + "\nBook not found in borrowed list.")