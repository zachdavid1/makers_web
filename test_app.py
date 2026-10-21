import os
import sys
from playwright.sync_api import Page, expect
import sys
import os
from db_connection import DatabaseConnection
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app


def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200



def test_get_authors():
    client = app.test_client()
    response = client.get('/authors')
    assert response.json == [
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
    assert response.status_code == 200

def test_books_page(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    books = page.locator("#book-list")
    expect(books).to_contain_text(['Minecraft Redstone Handbook'])

def test_book_creation(page: Page):
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder('title').fill("Minecraft Redstone Handbook")
    page.get_by_placeholder('author').fill("Notch")
    page.get_by_role("button", name="Add book").click()

    expect(page.locator("#book-list")).to_contain_text('Minecraft Redstone Handbook, by Notch')

def test_film_creation(page: Page):
    page.goto("http://127.0.0.1:5001/films")
    page.get_by_placeholder('title').fill("The Lego Movie")
    page.get_by_placeholder('year').fill('2016')
    page.get_by_role("button", name = "Add film").click()

    expect(page.locator("#film-list")).to_contain_text('Film: The Lego Movie, 2016')


# test_create_user.py



def test_create_user_is_saved_to_database():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()

   # send the request
    response = client.post('/users', data={
        'username': 'testuser',
        'password': 'password123'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # read from the DB
    result = connection.execute("SELECT * FROM users WHERE username = 'testuser'")

    # assert that the user was created
    assert len(result) == 1
    assert result[0]['username'] == 'testuser'


    