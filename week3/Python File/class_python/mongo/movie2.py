import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import certifi 

client = MongoClient('mongodb+srv://test:sparta@cluster0.u7yzppb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
# client = MongoClient('mongodb+srv://test:<sparta>@cluster0.u7yzppb.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=certifi.where())
db = client.dbsparta


# Read the URL and get the HTML,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# You will be scraping the data from this page
url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

# Use the requests library to get the HTML code at the url above
data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to
# parse HTML code
soup = BeautifulSoup(data.text, 'html.parser')

# Using select
movies = soup.select('.lister > table > tbody > tr')

# Looping through the movies
for movie in movies:
    # First, let's get the title of the movie
    movie_title = movie.select_one('.titleColumn > a').text
    # Next, let's get the year that movie was released
    year = movie.select_one('.titleColumn > .secondaryInfo').text
    # Let's also clean up the value for the year 
    # by removing special characters
    year = year.replace('(', '')
    year = year.replace(')', '')
    # Finally, let's get the rating for each movie
    rating = movie.select_one('.ratingColumn > strong').text
    # ...and print everything out side by side!
    print(movie_title, '/', year, '/', rating)

    doc = {
        'movie' : movie_title,
        'year' : year,
        'rating' : rating
    }
    db.movies.insert_one(doc)

target_movie = db.movies.find_one({'movie': 'Aladdin'})
print(target_movie['rating'])

target_rating = target_movie['rating']

movies = list(db.movies.find({'rating': target_rating}))

# boucle car on a un tableau avec variable et on veux trouver les bons films
for movie in movies:
    print(movie['movie'])


    db.movies.update_one(
    {'movie':'Aladdin'},
    {'$set': {'rating':'0'}}
    )