#!/bin/python3
# -*- coding: utf-8 -*-
import argparse

from extractors.g1_news_extractor import G1NewsExtractor
from extractors.site_dc_news_extractor import SiteDCNewsExtractor

from writers.csv_writer import CSVWriter
from writers.json_writer import JSONWriter
from writers.xml_writer import XMLWriter

site_options = {
    'g1':G1NewsExtractor,
    'site-dc':SiteDCNewsExtractor
}

output_options = {
    'csv':CSVWriter,
    'json':JSONWriter,
    'xml': XMLWriter
}

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sites', help='List of available sites',  nargs='+', choices=site_options.keys(), required=True)
    parser.add_argument('--output-type', help='Output type', choices=output_options.keys(), required=True)
    args = parser.parse_args()
    return args

def main():
    args = parse_args()
    sites = args.sites
    output_type = args.output_type

    writer = output_options[output_type]()

    for site in sites:
        extractor = site_options[site]()
        list_news = extractor.extract_news()
        writer.write_file(site ,list_news)


if __name__ == "__main__":
    main()