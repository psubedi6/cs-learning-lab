class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    @property
    def reading_time(self):
        return (self.pages/2)

time = Book("Harry Potter",20)

print(f"{time.reading_time}minutes")