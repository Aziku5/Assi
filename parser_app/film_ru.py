from bs4 import BeautifulSoup as BS
import requests
from django.views.decorators.csrf import csrf_exempt

URL = "https://www.film.ru/compilation/luchshie-multfilmy-disney"

HEADERS = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
}


# TODO START PARSING
@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


# TODO GET DATA
@csrf_exempt
def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all("div", class_="redesign_afisha_movie")
    disney_cartoon = []

    for item in items:
        disney_cartoon.append(
            {
                "title_name": item.find("div", class_="redesign_afisha_movie_main_title").get_text(),
                "title_url": URL + item.find("a").get("href"),
                "description": item.ind("div", class_="wrapper_movies_text").get_text(),
                "image": URL + item.find("div", class_="redesign_afisha_movie").find("img alt").get("src"),
            }
        )
    return disney_cartoon


# TODO ENDPARSER

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        all_cartoon = []
        for page in range(0, 1):
            html = get_html(f'https://www.film.ru/compilation/luchshie-multfilmy-disney', params=page)
            all_cartoon.extend(get_data(html.text))
            # print(all_cartoon)
            return all_cartoon

    else:
        raise Exception('Error in parsing')

# parser()
