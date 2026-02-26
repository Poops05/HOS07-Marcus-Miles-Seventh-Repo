class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False

    def check_in_or_out(self):
        self.is_checked_out = not self.is_checked_out
        status = "checked out" if self.is_checked_out else "checked in"
        print(f"The book '{self.title}' by {self.author} is now {status}.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Status: {'Checked out' if self.is_checked_out else 'Available'}")


class EBook(Book):
    def __init__(self, title, author, isbn, download_link, file_size):
        super().__init__(title, author, isbn)
        self.download_link = download_link
        self.file_size = file_size

    def display_info(self):
        super().display_info()
        print(f"Download Link: {self.download_link}")
        print(f"File Size: {self.file_size} MB")


physical_book = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
ebook = EBook( "1984", "George Orwell", "0987654321", "http://ebooks.example.com/1984", 2 )

print("Testing Book class:")
physical_book.display_info()
physical_book.check_in_or_out()
physical_book.check_in_or_out()

print("\nTesting EBook class:")
ebook.display_info()
ebook.check_in_or_out()
ebook.display_info() 

    