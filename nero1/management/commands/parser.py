import datetime
import urllib.parse
from collections import namedtuple

import bs4
import requests
from django.core.management.base import BaseCommand
from nero1.models import Reviews
from nero1.models import ReviewsZoon


InnerBlock = namedtuple('Block', 'name,review,date,name1,review1,date1')


class Block(InnerBlock):

    def __str__(self):
        return f'{self.name}\t{self.review} {self.date}'


class ReviewParser:

    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.2 Safari/605.1.15',
            'Accept-Language': 'ru',
        }

                                        ##########YANDEX##########
#подключение страницы для парсинга
    def get_page(self, page: int = None):
        url = 'https://yandex.ru/maps/org/moskovskiy_universitet_im_s_yu_vitte_fakultet_upravleniya/1384213316/reviews/?ll=37.655135%2C55.700335&z=8'
        r = self.session.get(url)
        return r.text
#парсинг имени
    def parse_block(self, item):
        name_block = item.select_one('div.business-review-view__author span')
        name = name_block.string.strip()
#парсинг отзыва
        review_block = item.select_one('span.business-review-view__body-text')
        review = review_block.string.strip()
#парсинг даты
        date_block = item.select_one('span.business-review-view__date')
        date = date_block.text.strip()
        p = Reviews(
            name=name,
            review=review,
            date=date,
        ).save()
        print(f'reviews {p}')
        return Block(
            name=name,
            review=review,
            date=date,
        )

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')

        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        container = soup.select('div.business-reviews-card-view__review')
        for item in container:
            block = self.parse_block(item=item)
            print(block)

                                          ##########ZOON##########
#подключение страницы для парсинга
    def get_page(self, page: int = None):
        url = 'https://zoon.ru/msk/education/moskovskij_universitet_im_syu_vitte_vo_2-m_kozhuhovskom_proezde-5380/reviews/'
        r = self.session.get(url)
        return r.text
#парсинг имени
    def parse_block(self, item):
        name1_block = item.select_one('strong.fs16.mg-right-s class')
        name1 = name1_block.text.strip()
#парсинг отзыва
        review1_block = item.select_one('span.js-comment-content')
        review1 = review1_block.string.strip()
#парсинг даты
        date1_block = item.select_one('span.iblock.gray')
        date1 = date1_block.text.strip()
        p = Reviews(
            name1=name1,
            review1=review1,
            date1=date1,
        ).save()
        print(f'reviews {p}')
        return Block(
            name=name,
            review=review,
            date=date,
        )

    def get_blocks(self, page: int = None):
        text = self.get_page(page=page)
        soup = bs4.BeautifulSoup(text, 'lxml')

        # Запрос CSS-селектора, состоящего из множества классов, производится через select
        container = soup.select('div.comment-container-wrapper.js-comment-container-wrapper')
        for item in container:
            block = self.parse_block(item=item)
            print(block)


class Command(BaseCommand):
    help = 'Парсинг Отзывов'

    def handle(self, *args, **options):
        p = ReviewParser()
        p.get_blocks()
