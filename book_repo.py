from book import Book
class BookRepo():
    def __init__(self, conn):
        self.conn = conn

    def get_all(self):
        rows = self.conn.execute("SELECT * FROM books")
        books = []
        for book in rows:
            books.append(Book(book['id'], book['title'], book['author']))
        return books

    def create_book(self, book_details):
        self.conn.execute("INSERT INTO books (title, author) VALUES (%s, %s)",[book_details['title'], book_details['author']])
