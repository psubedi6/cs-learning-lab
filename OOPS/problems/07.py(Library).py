class Book:
    library = "Toronto Public Library"
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def read(self, pages_read):
        if pages_read > self.pages:
            print("You cannot read more page then the book have")
        else:
            self.pages = self.pages - pages_read

    @staticmethod
    def is_long_book(total_pages):
        if total_pages>= 300:
            return True
        else:
            return False
    
    def display(self):
        print(f"Library: {Book.library}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages Remaining: {self.pages}")

book1 = Book("Harry Potter", "J. K. Rowling", 458)

book1.read(500)
book1.is_long_book(500)
book1.display()