#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Top level script. Calls other functions that generate datasets that this script then creates in HDX.

"""
import logging
import csv

from wfp import generate_dataset_and_showcase
from os.path import join

from hdx.facades.hdx_scraperwiki import facade
# from hdx.Configuration import Configuration

logger = logging.getLogger(__name__)


def main():
    """Generate dataset and create it in HDX"""
    with open('countries.csv', 'r') as countriesList:
        reader = csv.reader(countriesList)
        for row in reader:
            pays = row[0]
            iso = row[1]
            if (iso == 'CIV'):
                pays = 'Ivory Coast'
            dataset, showcase = generate_dataset_and_showcase(pays, iso)
            dataset.update_from_yaml()
            dataset.add_country_location(iso)

            dataset.add_tags([pays, 'OPENSTREETMAP', 'ROADS', 'UNSDIT'])
            showcase.add_tags([pays, 'OPENSTREETMAP', 'ROADS', 'UNSDIT'])

            dataset.create_in_hdx()
            showcase.create_in_hdx()
            showcase.add_dataset(dataset)

            print('==== %s dataset added ====' % pays)


if __name__ == '__main__':
    facade(main, hdx_site='test', user_agent='HDXINTERNAL unhabitat scraper',
           project_config_yaml=join('config', 'project_configuration.yml'))
