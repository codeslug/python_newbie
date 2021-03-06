'''
Created on Jan 23, 2014

@author: codeslug

Created as a coding challenge for Codefellows Python Bootcamp.

Intructions: Use object-oriented Python to model a public library (w/ three classes: Library, Shelf, & Book). 
* The library should be aware of a number of shelves. Each shelf should know what books it contains. 
Make the book object have "enshelf" and "unshelf" methods that control what shelf the book is sitting on. 
The library should have a method to report all books it contains. 

Note: this should *not* be a Django (or any other) app - just a single file with three classes (plus commands 
at the bottom showing it works) is all that is needed. In addition to pushing this python file to your Github 
account, please also setup a http://repl.it/languages/Python(so it runs there) and enter the saved URL here.
'''

class Library(object):
    shelves = [] # maintains list of all shelves
        
    def addShelf (self, shelf):
        self.shelves.append(shelf) # adds shelf instance to library's shelves list
    
    def listBooks(self):
        print "Welcome to Library! Today we have in stock the following titles:"
        for shelf in self.shelves: # iterates through the library's master list of shelves
            print "\n".join(shelf.items_on_shelf) # fetches list of books from Shelf instance, formats & prints to newline
    
    def addBook(self, title, shelf):
        shelf.items_on_shelf.append(title) # adds book to a specified shelf instance
        shelf.items_on_shelf.sort() # re-alphabetizes list
        print str("'"+title+"'"), "has been added to the Library."
    
    def removeBook(self, title, shelf):
        shelf.items_on_shelf.remove(title) # removes Book instance from specified Shelf instance
        print str("'"+title+"'"), "has been removed from the Library."


class Shelf(object):
    def __init__(self, genre):
        self.genre = genre
        self.items_on_shelf = []    # keeps list of book titles for each shelf instance
        
    def listBooks(self):
        print self.genre, "Shelf:", ", ".join(self.items_on_shelf) # formats and prints list for shelf instance
    
    def countBooks(self):
        print self.genre, "Shelf contains", str(len(self.items_on_shelf)), "books."


class Book(object):
    def __init__(self, title):
        self.title = title
        
    def addBook(self, shelf):
        my_library.addBook(self.title, shelf) # contacts the library to add the book
    
    def removeBook (self, shelf):
        my_library.removeBook(self.title, shelf)   # contacts the library to remove the book


# CREATE SOME OBJECTS
my_library = Library()

programming = Shelf("Programming")
biology = Shelf("Biology")
fiction = Shelf("Fiction")

book1 = Book("Crime and Punishment")
book2 = Book("Secret World of Slugs and Snails")
book3 = Book("Watership Down")
book4 = Book("How to Learn Python the Hard Way")
book5 = Book("Pride & Prejudice")

# REGISTER THE SHELVES WITH THE LIBRARY
my_library.addShelf(programming)
my_library.addShelf(biology)
my_library.addShelf(fiction)

# ADD BOOKS TO THE LIBRARY
book1.addBook(fiction)
book2.addBook(biology)
book3.addBook(fiction)
book4.addBook(programming)
book5.addBook(fiction)
print "\n" # formatting

# PRINT SHELF CONTENTS

biology.listBooks()
fiction.listBooks()
programming.listBooks()
print "\n"
fiction.countBooks()

# REMOVE BOOKS FROM LIBRARY
print "\n"
book4.removeBook(programming)

# PRINT LIBRARY CONTENTS
print "\n"
my_library.listBooks()

print "\n \n \n"
print "end of program" # i like to congratulate myself for not crashing the program