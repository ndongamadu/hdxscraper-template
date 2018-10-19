#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
SCRAPERNAME:
------------

Reads ScraperName JSON and creates datasets.

"""

import logging

from hdx.data.dataset import Dataset
from hdx.data.resource import Resource
from hdx.data.hdxobject import HDXError
from hdx.data.showcase import Showcase
from hdx.utilities.location import Location
from slugify import slugify
import time


logger = logging.getLogger(__name__)


def generate_dataset_and_showcase(country, countryISO3):
    """Parse json of the form:
    {
    },
    """
    title = country.capitalize() + ' Road Network'
    # logger.info('Creating dataset: %s' % title)
    slugified_name = slugify(title).lower()

    dataset = Dataset({
    })
    dataset['name'] = slugified_name
    dataset['title'] = title

    datex = time.strftime("%x")
    dataset.set_dataset_date(datex)
    dataset.set_expected_update_frequency('Every day')

    mainRoadsResource = Resource()
    mainRoadsResource['name'] = country.capitalize() + ' main roads'
    mainRoadsResource['format'] = 'zipped shapefile'
    mainRoadsResource['url_type'] = 'api'
    mainRoadsResource['url'] = 'http://ogcserver.gis.wfp.org/geoserver/ows?format_options=charset:UTF-8&typename=geonode:'+countryISO3.lower()+'_trs_roads_osm&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&hdx=hdx'
    mainRoadsResource['description'] = 'This dataset includes main roads from OpenStreetMap with the WFP data structure.'
    dataset.add_update_resource(mainRoadsResource)

    streetPathsResource = Resource()
    streetPathsResource['name'] = country.capitalize() + ' streets and paths'
    streetPathsResource['format'] = 'zipped shapefile'
    streetPathsResource['url_type'] = 'api'
    streetPathsResource['url'] = 'http://ogcserver.gis.wfp.org/geoserver/ows?format_options=charset:UTF-8&typename=geonode:'+countryISO3.lower()+'_trs_streets_osm&outputFormat=SHAPE-ZIP&version=1.0.0&service=WFS&request=GetFeature&hdx=hdx'
    streetPathsResource['description'] = 'This dataset includes streets and pathways from OpenStreetMap with the WFP data structure.'
    dataset.add_update_resource(streetPathsResource)

    showcase = Showcase({
        'name': '%s-showcase' % slugified_name,
        'title': country.capitalize(),
        'notes': 'WFP Geonode',
        'url': 'https://geonode.wfp.org/layers/ogcserver.gis.wfp.org%3Ageonode%3A'+countryISO3.lower()+'_trs_roads_osm',
        'image_url': 'https://centre.humdata.org/wp-content/uploads/2017/03/wfp-roads.png'
    })
    #showcase.add_tags([])
    print('==== dataset generated ====')
    return dataset, showcase

