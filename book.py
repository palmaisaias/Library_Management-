import colorama
from colorama import Back, Fore, Style
colorama.init
colorama.init(autoreset=True)

class Book:

    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.availability = True

    def get_info(self):
        return (f"Title: {self.title.title()}, Author: {self.author.title()}, "
                f"Genre: {self.genre.title()}, Available: {'Yes' if self.availability else 'No'}")
    
    def borrow(self):   #---this method is called by the borrow method in the user class. Checks if book
                        #--- is available. If it is, it then sets the availability to false to indicate
                        #---that the book has now been borrowed.
        if self.availability:
            self.availability = False 
            return True
        else:
            return False
