import requests
from bs4 import BeautifulSoup


def track_lister(date):
    response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{date}')
    response.raise_for_status()

    source_raw = response.text

    scrape = BeautifulSoup(source_raw, 'html.parser')

    track_list = []

    song_rank = scrape.find_all(name='span', class_='chart-element__rank__number')
    song_title = scrape.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
    artist_by = scrape.find_all(name='span',
                                class_='chart-element__information__artist text--truncate color--secondary')

    for x in range(100):
        template = {
            'rank': f'{song_rank[x].getText()}',
            'track': f'{song_title[x].getText()}',
            'artist': f'{artist_by[x].getText()}'
        }
        track_list.append(template)

    return track_list
