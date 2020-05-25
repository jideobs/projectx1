import sys
import os
import csv
import json
import time
import argparse

import requests

from .models import WebsiteMetadata
from .http_client import HTTPClient
from .runner import Runner


def get_args(args):
    parser = argparse.ArgumentParser(description='Scrape the data.')
    parser.add_argument('-m', type=str, nargs=1, dest='metadata_filename',
                    help='metadata holding info on how to get data from html', required=True)
    parser.add_argument('-o', nargs=1, type=str, dest='output_filename',
                    help='path where output should be stored', required=True)

    return parser.parse_args(args)


def check_if_filename_exists(filename):
    if not os.path.exists(filename):
        print('Cannot find metadata file: {filename}')
        sys.exit(100)


def main():
    print('Starting')
    args = get_args(sys.argv[1:])
    metadata_filename = args.metadata_filename[0]
    output_filename = args.output_filename[0]

    check_if_filename_exists(metadata_filename)

    with open(metadata_filename) as metadata_file:
        metadata_file_raw = metadata_file.read()
        metadata_file_dict = json.loads(metadata_file_raw)
        website_metadata = WebsiteMetadata.from_json(metadata_file_raw)
        with requests.Session() as session:
            with open(output_filename, 'w', newline='') as csvfile:
                fieldnames = [field['name'] for field in metadata_file_dict['data_html_attr']['fields']]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                http_client = HTTPClient(
                    base_url=website_metadata.url,
                    session=session)
                runner = Runner(
                    website_metadata=website_metadata,
                    http_client=http_client
                )
                for row in runner.run():
                    writer.writerow(row)


def main2():
    start = time.time()
    main()
    end = time.time()
    print(f'Total time taken: {end - start}')
