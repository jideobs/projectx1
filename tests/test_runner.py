import pytest
import json
from mockito import mock

from projectx1.models import WebsiteMetadata
from projectx1.runner import Runner
from projectx1.http_client import HTTPClient
    

def test_run(when):
    http_client = mock(HTTPClient)
    with open('./tests/data/test.html') as html_file_handler:
        when(http_client).get_html(...).thenReturn(html_file_handler.read())

    with open('./tests/data/test.json') as json_file_handler:
        website_metadata = WebsiteMetadata.from_json(json_file_handler.read())

    runner = Runner(website_metadata=website_metadata, http_client=http_client)
    for data_field in runner.run():
        assert all(data_field)
