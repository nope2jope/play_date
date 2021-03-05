import requests
from bs4 import BeautifulSoup

travel_to = '2010-05-11'#input("To what date would you like to travel? Enter in YYYY-MM-DD: ")

response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{travel_to}')
response.raise_for_status()

source_raw = response.text

source = BeautifulSoup(source_raw, 'html.parser')

track_list = []

song_rank = source.find_all(name='span', class_='chart-element__rank__number')
song_title = source.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
artist_by = source.find_all(name='span', class_='chart-element__information__artist text--truncate color--secondary')

for x in range(100):
    template = {
        'rank': f'{song_rank[x].getText()}',
        'track': f'{song_title[x].getText()}',
        'artist': f'{artist_by[x].getText()}'
    }
    track_list.append(template)

