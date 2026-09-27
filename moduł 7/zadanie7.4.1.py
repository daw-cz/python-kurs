import random

class Video:
    def __init__(self, title, year, genre, views=0):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views

    def play(self):
        self.views += 1

    def __repr__(self):
        return self.__str__()

class Movie(Video):
    def __str__(self):
        return f"{self.title} ({self.year})"

class Series(Video):
    def __init__(self, episode_number, season_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.season_number = season_number

    def __str__(self):
        return f"{self.title} S{self.season_number:02d}E{self.episode_number:02d}"

def get_movies(library):
    movies = [item for item in library if isinstance(item, Movie)]
    return sorted(movies, key=lambda x: x.title)


def get_series(library):
    series = [item for item in library if isinstance(item, Series)]
    return sorted(series, key=lambda x: x.title)

def search(library, title):
    for x in library:
        if x.title.lower() == title.lower():
            return x


def generate_views(library):
    if not library:
        return
    random_item = random.choice(library)
    random_views = random.randint(1, 100)
    random_item.views += random_views

def generate_views_10_times(library):
    for _ in range(10):
        generate_views(library)


def top_titles(library, limit=3, content_type=None):
    filtered_library = library
    
    if content_type == "movies":
        filtered_library = [item for item in library if isinstance(item, Movie)]
    elif content_type == "series":
        filtered_library = [item for item in library if isinstance(item, Series)]
        
    sorted_library = sorted(filtered_library, key=lambda x: x.views, reverse=True)
    return sorted_library[:limit]


library = [
    Movie(title="Pulp Fiction", year=1994, genre="Crime"),
    Movie(title="Inception", year=2010, genre="Sci-Fi"),
    Movie(title="The Matrix", year=1999, genre="Sci-Fi"),
    Series(title="The Simpsons", year=1989, genre="Animation", season_number=1, episode_number=5),
    Series(title="Breaking Bad", year=2008, genre="Drama", season_number=5, episode_number=14),
    Series(title="Friends", year=1994, genre="Comedy", season_number=2, episode_number=1),
]


print("--- Sortowanie ---")
print("Filmy:", get_movies(library))
print("Seriale:", get_series(library))

print("\n--- Generowanie losowych wyświetleń ---")
generate_views_10_times(library)
for item in library:
    print(f"{item} -> Wyświetleń: {item.views}")

print("\n--- Odtworzenie filmu ---")
film = search(library, "Inception")
film.play()
print(f"Uruchomiono film: {film}")

print("\n--- Wyszukiwanie ---")
found = search(library, "inception")

if found:
    print(f"Znaleziono: {found}")
    print(f"Liczba wyświetleń filmu: {found.views}")

print("\n--- Najpopularniejsze tytuły ---")
print(top_titles(library))

print("\n--- Najpopularniejsze seriale ---")
print(top_titles(library, content_type="series"))
