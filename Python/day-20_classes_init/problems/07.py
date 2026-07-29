class Movie:
    industry = "Hollywood"
    def __init__(self,title, director, release_year, rating):
        self.title= title
        self.director = director
        self.release_year = release_year
        self.rating= rating

movie1 = Movie("Inception", "Christopher Nolan", 2010, 8.8)
movie2 = Movie("Interstellar", "Christopher Nolan", 2014, 8.7)
movie2.rating = 9.0

print(f"{movie1.title}\n{movie1.director}\n{movie1.release_year}\n{movie1.rating}\n{movie1.industry}")
print(f"\n{movie2.title}\n{movie2.director}\n{movie2.release_year}\n{movie2.rating}\n{movie2.industry}")