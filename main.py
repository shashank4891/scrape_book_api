import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
import pymysql

# Load environment variables from .env file
load_dotenv()

# Function to scrape book data from a given URL
def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = []
    for book in soup.find_all('article', class_='product_pod'):
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        rating = book.find('p', class_='star-rating')['class'][1]
        books.append({'title': title, 'price': price, 'availability': availability, 'rating': rating})
    return books

# Function to connect to MySQL database
def connect_to_database():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        charset='utf8mb4'
    )

# Function to create books table if it doesn't exist
def create_books_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        price VARCHAR(20),
        availability VARCHAR(50),
        rating VARCHAR(10)
    )
    """)

# Function to insert books into the database
def insert_books_into_database(books, cursor, conn):
    for book in books:
        cursor.execute("INSERT INTO books (title, price, availability, rating) VALUES (%s, %s, %s, %s)", (book['title'], book['price'], book['availability'], book['rating']))
    conn.commit()

# Main function
def main():
    base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
    conn = connect_to_database()
    with conn.cursor() as cursor:
        create_books_table(cursor)
        for page in range(1, 51):  # Scraping all 50 pages
            url = base_url.format(page)
            books = scrape_books(url)
            insert_books_into_database(books, cursor, conn)
    conn.close()

if __name__ == "__main__":
    main()