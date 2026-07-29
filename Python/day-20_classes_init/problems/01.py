class Book:
    def __init__(self, title, author, pages):
        self.title =title
        self.author = author
        self.pages = pages

book = Book("Atomic Habits", "James Clear", 320)
print(f"{book.title}\n{book.author}\n{book.pages}")