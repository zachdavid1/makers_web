from flask import Flask, render_template, request, redirect
from book_repo import BookRepo
from film_repo import FilmRepo
from db_connection import DatabaseConnection
from user_repo import UserRepo
# instantiate a Flask app object
app = Flask(__name__)


@app.route('/hello', methods = ['GET'])
def hello():
    return "Hello world"

@app.route('/books', methods = ['GET'])
def get_books():
    conn = DatabaseConnection()
    conn.connect()
    book_repo = BookRepo(conn)
    books = book_repo.get_all()
    for book in books:
        print(book)
    return render_template('books.html', books = books)

@app.route('/authors', methods = ['GET'])
def get_authors():
    return [
  {
    "name": "Julia Donaldson",
    "dob": "1948-09-16"
  },
  {
    "name": "Andrea Beaty",
    "dob": "1961-10-08"
  },
  {
    "name": "Kelly Barnhill",
    "dob": "1973-01-01"
  },
  {
    "name": "Zetta Elliott",
    "dob": "1979-11-11"
  }
]

@app.route('/', methods = ['GET'])
def index():
    return render_template("index.html")

@app.route('/books', methods = ['POST'])
def create_book():
    conn = DatabaseConnection()
    conn.connect()
    book_repo = BookRepo(conn) 
    book_details = request.form
    book_repo.create_book(book_details)
    return redirect("/books")
    
@app.route('/films', methods = ['GET'])
def see_films():
    conn = DatabaseConnection()
    conn.connect()
    film_repo = FilmRepo(conn)
    films = film_repo.get_all()
    return render_template('films.html', films = films)

@app.route('/films', methods = ['POST'])
def add_film():
    conn = DatabaseConnection()
    conn.connect()
    film_repo = FilmRepo(conn)
    film_details = request.form
    film_repo.add_film(film_details)
    return redirect("/films")

@app.route('/users', methods = ['GET'])
def get_signup():
    return render_template("signup_form.html")

@app.route('/users', methods = ['POST'])
def create_user():
    conn = DatabaseConnection()
    conn.connect()
    user_repo = UserRepo(conn)
    user_details = request.form
    user_repo.create(user_details)
    return redirect('/users')
# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5001, debug=True)


