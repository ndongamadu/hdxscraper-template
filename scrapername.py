#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
SCRAPERNAME:
------------

Reads ScraperName JSON and creates datasets.

"""

import logging

from hdx.data.dataset import Dataset
from hdx.data.hdxobject import HDXError
from hdx.data.showcase import Showcase
from hdx.utilities.location import Location
from slugify import slugify

logger = logging.getLogger(__name__)


def get_countriesdata(base_url, downloader):
    response = downloader.download('%sfolder/folder/xxx.xxx' % base_url)
    jsonresponse = response.json()
    return jsonresponse['countries_key']


def generate_dataset_and_showcase(base_url, downloader, countrydata):
    """Parse json of the form:
    {
    },
    """
    title = countrydata['title']
    logger.info('Creating dataset: %s' % title)
    slugified_name = slugify(title).lower()
    ...
    dataset = Dataset({
        'name': slugified_name,
        'title': title,
        ...
    })
    dataset.set_maintainer()
    dataset.set_organization()
    dataset.set_dataset_date()
    dataset.set_expected_update_frequency()
    dataset.add_country_location()
    dataset.add_tags([])

    resource = {
        'name': title,
        'format': ,
        'url': ,
        'description':
    }
    dataset.add_update_resource(resource)

    showcase = Showcase({
        'name': '%s-showcase' % slugified_name,
        'title':
        'notes':
        'url':
        'image_url':
    })
    showcase.add_tags([])
    return dataset, showcase
