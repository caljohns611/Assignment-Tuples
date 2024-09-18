#question 2 task 2
def add_book(library):
    new_book = input("Enter the title of the book you want to add: ")
    author = input("Enter the author of the book you want to add: ")
    
    new_book_tuple = (new_book, author)
    
    if new_book_tuple in library:
        print("This book is already in your library.")
    else:
        library.append(new_book_tuple)
        print("Book added to the library.")

    return library 

def display_library(library):
    if not library:
        print("The library is empty.")
    else:
        print("Current Library:")
        for title, author in library:
            print(f'Title: "{title}", Author: {author}')

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

display_library(library)

library = add_book(library)

display_library(library)
