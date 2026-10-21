from film import Film
class FilmRepo():
    def __init__(self, conn):
        self.conn = conn
    def get_all(self):
        rows = self.conn.execute("SELECT * from films")
        films = []
        for film in rows:
            films.append(Film(film['title'], film['year']))
        return films
    def add_film(self, film_info):
        self.conn.execute(f"INSERT INTO films (title, year) VALUES (%s, %s)",
                          [film_info['title'], int(film_info['year'])])
