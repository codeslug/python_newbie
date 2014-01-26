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
        print "shelves = ", self.shelves
        # print "shelf names are: ", self.shelves[self.genre]
        for count in self.shelves:
            print count.items_on_shelf
    
    def addBook(self, title):
        shelf1.items_on_shelf.append(title)
        shelf1.items_on_shelf.sort() #re-alphabetizes list
        print str(title), "has been added to the library."
        
    def getGenre(self):
        pass
    
    def removeBook(self, title):
        shelf1.items_on_shelf.remove(title)
        print title, " has been removed from the Library."
        


class Shelf(object):
    items_on_shelf = [] #keeps list of book titles for each shelf
    def __init__(self, genre):
        self.genre = genre
    
#    def add_book (self, title):
#        self.items_on_shelf.append(title)
#        self.items_on_shelf.sort() #re-alphabetizes list
#        print str(title), "has been added to the shelf."
# maybe add this code back -- if library passes books to empty shelves??
    
    def listBooks(self):
        print "This shelf contains: " + ", ".join(self.items_on_shelf)
    
#    def removeBooks (self, title):
#        self.items_on_shelf.remove(title)

class Book(object):
    def __init__(self, title):
        self.title = title
        # self.author = author
        # self.genre = genre
    
    def unshelf(self):
        library1.unshelf(self.title)
        
    def addBook(self):
        my_library.addBook(self.title)
    
    def removeBook (self):
        my_library.removeBook(self.title)

# CREATE SOME OBJECTS
my_library = Library("My Library")

book1 = Book("Crime and Punishment")
book2 = Book("Secret World of Slugs and Snails")

shelf1 = Shelf("Programming Shelf")
shelf2 = Shelf("Biology")
shelf3 = Shelf("Fiction")

# REGISTER THE SHELVES WITH THE LIBRARY
my_library.addShelf(shelf1)
my_library.addShelf(shelf2)
my_library.addShelf(shelf3)


# book1.printTitle() # debugging


# shelf1.add_book(book1.title)
# shelf1.list_books()
# print shelf1.genre, "contains this many books:", str(len(shelf1.items_on_shelf))

book1.addBook()
book2.addBook()
my_library.listBooks()

# WORKING CODE
# print shelf1.genre, "contains this many books:", str(len(shelf1.items_on_shelf))
# book1.removeBook() # working code
# print shelf1.genre, "contains this many books:", str(len(shelf1.items_on_shelf))

print
print
my_library.listBooks()


print "Shelf 1:", shelf1.items_on_shelf
print "Shelf 2:", shelf2.items_on_shelf
print "Shelf 3", shelf3.items_on_shelf

# BUGGED print "Library list", my_library.shelves.genre




print
print
print "not bugged... yet"