import pytest
import requests
from mockito import mock
from requests import Response
from io import BytesIO as BufferIO

from projectx1.http_client import HTTPClient


@pytest.fixture
def session_factory(when):
    def factory(return_value):
        session = mock(requests.Session)
        if isinstance(return_value, requests.exceptions.RequestException):
            when(session).get(...).thenRaise(return_value)
        else:
            when(session).get(...).thenReturn(return_value)
        
        return session

    return factory


def test_http_client_get_html_successful_connection_to_server(session_factory):
    expected_page_html = '<html>website</html>'
    
    expected_response = Response()
    expected_response.status_code = 200
    expected_response.encoding = 'utf-8'
    expected_response.raw = BufferIO(expected_page_html.encode('utf-8'))

    session = session_factory(return_value=expected_response)
    http_client = HTTPClient(base_url='https://www.example.com', session=session)
    page_html = http_client.get_html(params={'page': 0})
    
    assert expected_page_html == page_html


def test_http_client_get_html_request_exception_occurred(session_factory):
    expected_page_html = ''

    session = session_factory(return_value=requests.exceptions.ConnectionError())
    http_client = HTTPClient(base_url='https://www.example.com', session=session)
    page_html = http_client.get_html(params={'page': 0})

    assert expected_page_html == page_html
