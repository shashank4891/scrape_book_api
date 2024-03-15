
# Book Scraper API

This is a Python script for scraping book data from the website http://books.toscrape.com and storing it in a MySQL database.


## Features

- Scrapes book attributes like name, price, availability, and ratings from all 50 pages of the website.

- Stores the scraped data in a MySQL database.


## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- requests library
- beautifulsoup4 library
- pymysql library
- python-dotenv library (optional for loading environment variables from a .env file)
## Installation

* Clone the repository:

```bash
 git clone -
```
* Install the required Python packages:
```bash
 pip install beautifulsoup4 pymysql requests python-dotenv
```
* Set up environment variables:

Create a `.env` file in the root directory and add the following environment variables:

```bash
DB_HOST=your_database_host
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_DATABASE=your_database_name
```

## Usage/Routes

- Run the main.py script:

```bash
python main.py
```

## Contributing

Contributions are always welcome!

Feel free to open a pull request or submit an issue for any bugs or feature requests.

