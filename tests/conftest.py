from tmxer.map import *
import xml.etree.ElementTree as ET
import os
import pytest

@pytest.fixture(scope='session')
def map_path():
    return os.path.join(os.getcwd() + '/../tests/test.tmx')

@pytest.fixture(scope='session')
def basic_map(map_path):
    return Map(map_path)

@pytest.fixture(scope='session')
def pyglet_map(map_path):
    return PygletMap(map_path)
