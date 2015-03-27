from tmxer.map import Map
import xml.etree.ElementTree as ET
import os
import pytest

@pytest.fixture(scope='session')
def map_path():
    return os.path.join(os.getcwd() + '/../tests/test.tmx')

@pytest.fixture(scope='session')
def basic_map_file(map_path):
    """Returns a file object that we can pass to create a Map"""
    return Map.frompath(map_path)

@pytest.fixture(scope='session')
def basic_map(map_path):
    """Helper function for my convenience"""
    return Map(ET.parse(map_path))
