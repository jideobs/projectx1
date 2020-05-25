import os
import sys

from mockito import patch

from projectx1.cli import main
from projectx1 import http_client

def test_main__invalid_args():
    try:
        main()
    except SystemExit as e:
        # System exit on invalid args would be error code
        assert str(e) == '2'


def test_main__invalid_metadata():
    sys.argv = ['', '-m=/tmp/invalid.json', '-o=/tmp/output.csv']
    try:
        main()
    except SystemExit as e:
        assert str(e) == '100'


def test_main__successful_run():
    sys.argv = ['', '-m=./tests/data/test.json', '-o=/tmp/output.csv']
    with open('./tests/data/test.html') as f:
        html_doc = f.read()
        with patch(http_client.HTTPClient, 'get_html', lambda params: html_doc):
            main()

            assert os.path.exists('/tmp/output.csv')
