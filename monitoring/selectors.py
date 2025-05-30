import datetime
import re

import requests
from bs4 import BeautifulSoup


def get_soup_from_tour_kassa() -> BeautifulSoup:
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'sec-ch-ua': '"Chromium";v="136", "Google Chrome";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36'
    }

    r = requests.get(
        'https://tour-kassa.ru/%D0%BA%D1%83%D1%80%D1%81%D1%8B-%D0%B2%D0%B0%D0%BB%D1%8E%D1%82-%D1%82%D1%83%D1%80%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%82%D0%BE%D1%80%D0%BE%D0%B2',
        headers=headers,
    )

    return BeautifulSoup(r.content.decode(), features='html.parser')


def get_table_soups_by_date_from_tour_kassa():
    soup = get_soup_from_tour_kassa()
    course_tables = soup.find_all('table', attrs={'class': 'mod_rate_day'})
    course_tables += soup.find_all('table', attrs={'class': 'mod_rate_today'})
    result = {}
    for table in course_tables:
        table_header = table.find(lambda x: x.name == 'i' and 'Курсы валют туроператоров' in x.text)
        object_with_date = table_header.find_next(string=re.compile(r'\d\d\.\d\d\.\d\d'))
        table_date = datetime.datetime.strptime(object_with_date.text[-8:], '%d.%m.%y').date()
        result[table_date] = table

    return result


def get_anex_euro_course_by_dates() -> dict[datetime.date, float]:
    result = {}
    for date, table in get_table_soups_by_date_from_tour_kassa().items():
        anex_elem = table.find(lambda x: x.attrs.get('class') == ['mod_rate_oper'] and 'Анекс' in x.text)
        price_today = float(anex_elem.find_next('td').text)
        result[date] = price_today

    return result


def get_anex_euro_course():
    soup = get_soup_from_tour_kassa()
    anex_elem = soup.find(lambda x: x.attrs.get('class') == ['mod_rate_oper'] and 'Анекс' in x.text)
    price_today = float(anex_elem.find_next('td').text)
    return price_today
