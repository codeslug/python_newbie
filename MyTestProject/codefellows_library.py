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
    topics = [] # this doesnt do anything atm
    
    def __init__(self, name):
        self.name = name
        
    def addShelf (self, shelf):
        self.shelves.append(shelf) # adds live shelf to library's shelves list
    
    def listBooks(self):
        for count in self.shelves:
            print "\n".join(count.items_on_shelf)
    
    def addBook(self, title, shelf):
        shelf.items_on_shelf.append(title)
        shelf.items_on_shelf.sort() #re-alphabetizes list
        print str(title), "has been added to the library."
        
    def getGenre(self):
        pass
    
    def removeBook(self, title, shelf):
        shelf.items_on_shelf.remove(title)
        print title, "has been removed from the Library."


class Shelf(object):
    def __init__(self, genre):
        self.genre = genre
        self.items_on_shelf = []    # keeps list of book titles for each shelf


class Book(object):
    def __init__(self, title):
        self.title = title
        # self.author = author
        # self.genre = genre
        
    def addBook(self, shelf):
        my_library.addBook(self.title, shelf)
    
    def removeBook (self, shelf):
        my_library.removeBook(self.title, shelf)   # better to just remove the book flat out without searching for its shelf?


# CREATE SOME OBJECTS
my_library = Library("My Library")

programming = Shelf("Programming Shelf")
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
print "\n"

# PRINT SHELF CONTENTS
print "Biology Shelf:", ", ".join(biology.items_on_shelf)
print "Programming Shelf:", ", ".join(programming.items_on_shelf)
print "Fiction Shelf:", ", ".join(fiction.items_on_shelf)
print programming.genre, "contains this many books:", str(len(programming.items_on_shelf))

# REMOVE BOOKS FROM LIBRARY
print "\n"
book4.removeBook(programming)

# PRINT LIBRARY CONTENTS
print "\n"
print "The library contains ..."
my_library.listBooks()

# WORKING CODE
# print shelf1.genre, "contains this many books:", str(len(shelf1.items_on_shelf))
# book1.removeBook() # working code
# print shelf1.genre, "contains this many books:", str(len(shelf1.items_on_shelf))

print "\n \n \n \n"
print "end of program"