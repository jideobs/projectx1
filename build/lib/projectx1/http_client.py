import requests
from requests import Response
from requests.exceptions import RequestException


class HTTPClient:
    def __init__(self, base_url: str, session: requests.Session):
        self.base_url = base_url
        self.session = session

    def get_html(self, params: dict, url_path: str = '/') -> str:
        url = f'{self.base_url}/{url_path}'
        try:
            response = self.session.get(url)
            page_html = response.text
        except RequestException as e:
            page_html = ''

        return page_html
