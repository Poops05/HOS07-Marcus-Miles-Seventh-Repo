class LibraryCatalog: 
    """Class to manage a collection of books."""
    def __init__(self): 
        self.books = []

    def add_book(self, book):
        """Adds a book object to the catalog.""" 
        self.books.append(book)

    def display_all_books(self):
        """Displays info for all books in the catalog."""
        for book in self.books: 
            book.display_info()
            print()


class Book:
    """Base class representing a physical book."""
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_in_or_out(self):
        """Toggles the check-in/check-out status."""
        self.is_checked_out = not self.is_checked_out
        status = "checked out" if self.is_checked_out else "checked in"
        print(f"The book '{self.title}' by {self.author} is now {status}.")

    def display_info(self):
        """Prints detailed information about the book."""
        info = ( f"Title: {self.title}\n" f"Author: {self.author}\n" f"ISBN: {self.isbn}\n" f"Status: {'Checked out' if self.is_checked_out else 'Available'}" )
        print()
      

class DownloadDetails:
    """Stores download-related information for an eBook."""
    def __init__(self, download_link, file_size):
        self.download_link = download_link
        self.file_size = file_size

    def display_download_info(self):
        print(f"Download Link: {self.download_link}")
        print(f"File Size: {self.file_size} MB")


class EBook(Book):
    """Represents an electronic book with downloadable content."""
    def __init__(self, title, author, isbn, download_link, file_size):
        super().__init__(title, author, isbn)
        self.download_details = DownloadDetails(download_link, file_size)

    def display_info(self):
        """Extends Book display_info with download details."""
        super().display_info()
        self.download_details.display_download_info()


physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
ebook = EBook("1984", "George Orwell", "0987654321", "http://ebooks.example.com/1984", 2)

my_library = LibraryCatalog() 
my_library.add_book(physical_book) 
my_library.add_book(ebook)

print("=== Displaying All Books in the Catalog ===")
my_library.display_all_books()

print("=== Testing Check-In/Check-Out ===")
physical_book.check_in_or_out() 
ebook.check_in_or_out()

print("\n=== Displaying Updated Book Statuses ===")
my_library.display_all_books()
ebook.check_in_or_out()
ebook.display_info() 

    
