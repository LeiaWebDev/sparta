import requests
from bs4 import BeautifulSoup

# Read the URL and get the HTML,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
}

# You will be scraping the data from this page
url = 'https://www.billboard.com/charts/hot-100'

# Use the requests library to get the HTML code at the url above
data = requests.get(url=url, headers=headers)

# The BeautifulSoup library makes it easy to parse HTML code
soup = BeautifulSoup(data.text, 'html.parser')

# Using select
songs = soup.select('.o-chart-results-list-row')

# Looping through the songs
for song in songs:
    # First, let's get the title of the song
    song_title = song.select_one('#title-of-a-story').text.strip()
    # Next, let's get the singer that movie was released
    singer = song.select_one('.lrv-u-width-100p>ul>li>span').text.strip()
    # Finally, let's get the rating for each movie
    ranking = song.select_one('.o-chart-results-list__item>span').text.strip()
    # ...and print everything out side by side!
    print(ranking,'/',song_title, '/', singer )
