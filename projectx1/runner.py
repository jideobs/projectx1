import json
from bs4 import BeautifulSoup
from collections import namedtuple

from .http_client import HTTPClient
from .models import WebsiteMetadata, DataField


class Runner:
    def __init__(self, 
                website_metadata: WebsiteMetadata,
                http_client: HTTPClient):
        self.website_metadata = website_metadata
        self.http_client = http_client

    def get_page(self) -> str:
        page_query_attr = self.website_metadata.page_query_attr
        start_page = page_query_attr.start_page
        end_page = page_query_attr.end_page
        query_param_name = page_query_attr.query_param_name 
        for page_num in range(start_page, (end_page+1)):
            params = {query_param_name: page_num}
            html = self.http_client.get_html(params=params)
            yield html

    def get_data_from_page(self, html: str) -> dict:
        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find_all('div', class_=self.website_metadata.data_html_attr.row_html_attr)
        for row in rows:
            row_data = {}
            for field in self.website_metadata.data_html_attr.fields:
                field_data = row.find(field.element_name, class_=field.class_name)
                row_data.update(
                    {field.name: field_data.text}
                )

            yield row_data

    def run(self) -> dict:
        for html in self.get_page():
            for r in self.get_data_from_page(html):
                yield r
