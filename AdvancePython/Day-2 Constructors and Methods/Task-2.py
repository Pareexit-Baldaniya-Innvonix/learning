# Task 2: parameterized constructure
class Movie:
    def __init__(self, name, type, cinema):
        self.name = name
        self.type = type
        self.cinema = cinema


movie = Movie("Avatar: Fire and Ash", "Action", "Hollywood")
print(movie.name)
print(movie.type)
print(movie.cinema)
