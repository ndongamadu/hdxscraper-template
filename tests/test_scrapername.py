#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Unit tests for scrapername.

'''
from os.path import join

import pytest
from hdx.hdx_configuration import Configuration
from scrapername import generate_dataset_and_showcase, get_countriesdata


class TestWorldPop:
    countrydata = {...}

    @pytest.fixture(scope='function')
    def configuration(self):
        Configuration._create(hdx_read_only=True,
                             project_config_yaml=join('tests', 'config', 'project_configuration.yml'))

    @pytest.fixture(scope='function')
    def downloader(self):
        class Request:
            def json(self):
                pass

        class Download:
            @staticmethod
            def download(url):
                request = Request()
                if url == 'http://xxx':
                    def fn():
                        return {'key': [TestWorldPop.countrydata]}
                    request.json = fn
                return request
        return Download()

    def test_get_countriesdata(self, downloader):
        countriesdata = get_countriesdata('http://xxx/', downloader)
        assert countriesdata == [TestWorldPop.countrydata]

    def test_generate_dataset_and_showcase(self, configuration, downloader):
        dataset, showcase = generate_dataset_and_showcase(downloader, TestWorldPop.countrydata)
        assert dataset == {...}

        resources = dataset.get_resources()
        assert resources == [...]

        assert showcase == {...}

