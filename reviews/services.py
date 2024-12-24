from typing import Any
import requests
from requests.adapters import Retry, HTTPAdapter
from .models import Review 
from .exceptions import UpdateReviewError, EmptyReviewList
from bs4 import BeautifulSoup
from datetime import datetime, timezone


def get_2gis_reviews_data(api_key_2gis: str, organization_id: str, reviews_limit: int = 10) -> tuple[dict[str, Any], float, int]:
    """
    Получаем информацию об отзывах определенной организации
    :param api_key_2gis: 2GIS API KEY
    :param reviews_limit: Количество отзывов в ответе (default: 10);
    :param url: Ссылка на организацию 2 gis (пример: https://2gis.ru/vladivostok/firm/70000001021276207/tab/reviews);
    :return: Словарь с данными об отзывах организации, среднмй рейтинг компании и количество отзывов
    """
    fetched_reviews = _fetch_reviews(organization_id, api_key_2gis)
    result = _get_needed_data_format(fetched_reviews, reviews_limit)
    average_rating = fetched_reviews['meta']['branch_rating']
    count_review = fetched_reviews['meta']['branch_reviews_count']
    return result, average_rating, count_review


def _fetch_reviews(organization_id: str, api_key_2gis: str) -> dict[str, dict]:
    """
    Использую публичное API 2gis, получаем полную информацию об отзывах организации.
    :param api_key_2gis: 2GIS API KEY
    :param organization_id: ID организации 2gis
    :return: Словарь ответа 2gis API
    """

    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    try:
        return session.get(
            f"https://public-api.reviews.2gis.com/2.0/branches/{organization_id}/reviews?"
            f"limit=50&is_advertiser=false&fields=meta.branch_rating,meta.branch_reviews_count&sort_by=date_edited&"
            f"key={api_key_2gis}&locale=ru_RU"
        ).json()
    except Exception:
        raise UpdateReviewError("Ошибка при запросе к 2gis API")


def _get_needed_data_format(
    fetched_data: dict[str, dict], reviews_limit: int = 10
) -> dict[str, Any]:
    """
    Фильтрация ненужных данных ответа и преобразование нужных в необходимый формат.
    :param fetched_data: Данные ответа от API 2gis;
    :param reviews_limit: Количество отзывов в ответе (default: 10);
    :return: Словарь с данными об отзывах организации
    """

    MIN_RATING = 4

    if len(fetched_data["reviews"]) == 0:
        raise EmptyReviewList("Список отзывов пуст")
    
    return {
        "reviews": [
            {
                "stars": review["rating"],
                "created_at": review["date_edited"] or review["date_created"],
                "text": review["text"],
                "author": review["user"]["name"],
                "author_avatar": review["user"]["photo_preview_urls"]["640x"],
                "photos": [
                    photo["preview_urls"]["640x"]
                    for photo in review["photos"]
                    if photo.get("preview_urls")
                ],
            }
            for review in fetched_data["reviews"]
            if review["rating"] >= MIN_RATING
        ][:reviews_limit],
    }


def get_vl_reviews_data() -> tuple[dict[str, Any], float, int]:
    url = "https://www.vl.ru/commentsgate/ajax/thread/company/naparili-dv/embedded"

    params = {
        "theme": "company",
        "appVersion": "2024101514104",
        "_dc": "0.32945840348689304",
        "pastafarian": "0fb682602c07c4ae9bdb8969e7c43add3b898f4e7b14548c8c2287a29032d6b1",
        "location": "https://www.vl.ru/naparili-dv#comments",
        "moderatorMode": "1"
    }

    headers = {
        "Host": "www.vl.ru",
        "Sec-Ch-Ua-Platform": "\"macOS\"",
        "X-Requested-With": "XMLHttpRequest",
        "Accept-Language": "ru-RU,ru;q=0.9",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://www.vl.ru/autocenter",
        "Accept-Encoding": "gzip, deflate, br",
        "Priority": "u=1, i"
    }

    cookies = {
        "PHPSESSID": "rhjcp9pkfg82bvcda7tve2a9m0",
        "city": "4",
        "region": "103",
        "visitor": "ad5f2acbb35cd457a9dc57c692437d9261e1d5606ea33280caabd64f0fa3d0d6",
        "ring": "980791ab6a297547f26234387e1a5012",
        "analytics_user": "980791ab6a297547f26234387e1a5012",
        "spravochnik_windowSessionID": "ad061bf1730033306880",
        "_ym_uid": "1730033307709177970",
        "_ym_d": "1730033307",
        "sprRecentlyWatchedCompanyIds": "460034",
        "_ym_isad": "2",
        "_gid": "GA1.2.1877505797.1730033311",
        "_ga": "GA1.3.1517315620.1730033307",
        "_ga_3XHX5WMXEB": "GS1.2.1730033312.1.0.1730033312.60.0.0",
        "_ga_D3RZ9TRN3Y": "GS1.3.1730033312.1.0.1730033312.60.0.0",
        "_ga_1XW1PCV9KF": "GS1.2.1730033312.1.1.1730034975.8.0.0",
        "_ym_visorc": "w",
        "spravochnik_windowSessionTS": "1730035316115",
        "_ga_3X07YH0D78": "GS1.1.1730035314.2.1.1730035316.0.0.0",
        "_gat": "1",
        "_gat_allProjects": "1",
        "_gat_glCommonTracker": "1",
        "_gat_commentsvlru": "1",
    }

    response = requests.get(url, headers=headers, params=params, cookies=cookies)

    if response.status_code == 200:
        res = response.json()['data']['content']
        soup = BeautifulSoup(res, 'html.parser')
        review_elements = soup.find_all('li', {'data-type': 'review'})
        reviews = []

        for review in review_elements:
            star_rating = review.find('div', class_='star-rating')
            if star_rating:
                star_rating = int(float(star_rating.find('div', class_='active')['data-value']) * 5)

            user_avatar = review.find('div', class_='user-avatar').find('img')
            if user_avatar:
                user_avatar = user_avatar['src']

            user_name_tag = review.find('span', class_='user-name')
            user_name = user_name_tag.text.strip() if user_name_tag else 'N/A'

            review_text_tag = review.find('div', class_='cmt-content').find('p', class_='comment-text')
            if review_text_tag and "Комментарий:" in review_text_tag.text:
                review_text = review_text_tag.text.strip().split("Комментарий:", 1)[1].strip()
            else:
                continue

            time_tag = review.find('span', class_='time')
            time_text = time_tag.text 
            created_at = convert_to_datetime(time_text)

            if star_rating >= 4:
                reviews.append({
                    'author': user_name,
                    'text': review_text,
                    'author_avatar': user_avatar,
                    'stars': star_rating, 
                    'created_at': created_at,
                })

        reviews_count_block = soup.find('div', class_='cmt-thread-subscription')
        reviews_count = reviews_count_block.find('span',class_='count').text

        api_review_avg = 'https://www.vl.ru/ajax/company-history-votes?companyId=444287'
        response = requests.get(api_review_avg, headers=headers)

        data = response.json()
        average_rating_history: dict = data["history"]
        average_rating = list(average_rating_history.values())[0]

        return reviews, average_rating, reviews_count
    else:
        print(f"Ошибка: {response.status_code}")


def get_yandex_reviews_data() -> tuple[dict[str, Any], float, int]:
    url = 'https://yandex.ru/maps/org/naparili_dv/68956168702/reviews/?ll=131.926107%2C43.156871&z=17'
    
    headers = {
        'Host': 'yandex.ru',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://www.google.com/',
        'Connection': 'keep-alive',
        'Cookie': 'maps_los=0; spravka=dD0xNzI2ODEwMTY3O2k9ODYuMTAyLjEzLjc0O0Q9RUY3MDRCMEVFNzU0MTg1N0YzNTZENDg2RjlGMjNFNDMzNTY2NDdDRUQxQzlFQzE3NTFEQThDREFGMjA4MTNFNENFMUFFNkQyRTNCOTBGRTc3NENEOEJFQTExNUVFNjQwRUQwOEIwNDQ2QjI0NUYyRkVBQkEwMzNEMzQxM0JFNzA1MEQ0MzMyOTlGRkY1M0I4MUJERDt1PTE3MjY4MTAxNjc2NTgyNzE1ODA7aD01YmYzMGNlNTBmYTY4ODljZWI0ZmM5NjcyOTI4MGJmOQ==; _yasc=r3AyN1rNx3P7SuIwvwYQHGPC7jhpypevF0XoRv0aqOsiu8Q5dsPbKyhN0qIj9ZEhnAHqypxgYP8=; i=USTWwFikzzttv4Ewt+JjX6guEjI7ryOi3U8d1d0obMvWdQLf6l3nC4o08OxIR2X5+xwqxB4bIfVflox4XzmFHzUvDKI=; yandexuid=1948173161726810137; yashr=8704804031726810137; receive-cookie-deprecation=1; yuidss=1948173161726810137; ymex=2042170139.yrts.1726810139; _ym_uid=1726810140413132111; _ym_d=1726810140; is_gdpr=0; is_gdpr_b=CLmcHRCIlAIoAg==; yp=2042170169.pcs.1#1729488569.hdrc.0#1727414969.szm.0_8:2400x1350:2400x1194; bh=YNvqsLgGahfcyuH/CJLYobEDn8/14QyChPKOA4vBAg==; yabs-vdrf=A0; gdpr=0',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Priority': 'u=0, i',
    }

    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, "html.parser")
    meta_block = soup.find('div', class_='business-summary-rating-badge-view')

    rating_raw = meta_block.find('div', class_='business-summary-rating-badge-view__rating').text
    average_rating = float(rating_raw.split('\xa0')[1].replace(',', '.'))

    reviews_count_raw = meta_block.find('span', class_='business-rating-amount-view').text 
    reviews_count = int(reviews_count_raw.split()[0])

    review_blocks = soup.findAll('div', class_='business-reviews-card-view__review')
    reviews = []
    for review_block in review_blocks: 
        author = review_block.find('div', class_='business-review-view__author-name').find('span').text 
        text = review_block.find('span', class_='business-review-view__body-text').text
        stars = len(review_block.find('div', class_='business-rating-badge-view__stars').findAll('span'))

        created_at_str = review_block.find('span', class_='business-review-view__date').find('span').text 
        created_at = convert_to_datetime(created_at_str)

        author_avatar = review_block.find('div', class_='user-icon-view__icon').get('style')
        if author_avatar: 
            author_avatar = author_avatar.split('url(')[1][:-1]

        photos_blocks = review_block.findAll('img', class_='business-review-media__item-img')
        photos = [photo_block.get('src') for photo_block in photos_blocks]

        reviews.append({
            'author': author,
            'text': text,
            'author_avatar': author_avatar,
            'stars': stars, 
            'created_at': created_at,
            'photos': photos,
        })

    return reviews, average_rating, reviews_count


def convert_to_datetime(datetime_str: str) -> datetime: 
    months_mapper = {
        'января': 1,
        'февраля': 2,
        'марта': 3,
        'апреля': 4,
        'мая': 5,
        'июня': 6,
        'июля': 7,
        'августа': 8,
        'сентября': 9,
        'октября': 10,
        'ноября': 11,
        'декабря': 12
    }

    if len(datetime_str.split()) == 2: 
        datetime_parts = datetime_str.split()
        day = datetime_parts[0] 
        year = datetime.now().year
    else: 
        datetime_parts = datetime_str.split()
        year = datetime_parts[2]
        day = datetime_parts[0]
        month_text = datetime_parts[1]

    month_text = datetime_parts[1]
    month = months_mapper.get(datetime_parts[1])

    if not month: 
        raise KeyError(f'Месяца "{month_text}" не существует')
        
    datetime_obj = datetime(
        year=int(year), 
        month=int(month), 
        day=int(day)
    ).replace(tzinfo=timezone.utc) 
    return datetime_obj