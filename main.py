#!/bin/python3
# -*- coding: utf-8 -*-
import argparse

from extractors import G1NewsExtractor, SiteDCNewsExtractor
from writers import CSVWriter

site_options = {
    'g1':G1NewsExtractor,
    'site-dc':SiteDCNewsExtractor
}

output_options = {
    'csv':CSVWriter
}

parser = argparse.ArgumentParser()
parser.add_argument('--sites', help='List of available sites',  nargs='+', choices=site_options.keys())
parser.add_argument('--output-type', help='Output type', choices=output_options.keys())
args = parser.parse_args()
sites = args.sites


for site in sites:
    extractor = site_options[site]()
    list_news = extractor.extract_news()
    for news in list_news:
        print(site,news.url)