import xml.etree.ElementTree as ET
from tmxer.tileset import *
from tmxer.image import *
from tmxer.layer import *
from tmxer.objects import ObjectGroup

class Map:
    def __init__(self, filepath, _Tileset=Tileset, _Layer=Layer, _Image=Image,
            _ObjectGroup=ObjectGroup, _ImageLayer=ImageLayer):
        self._Tileset = _Tileset
        self._Layer = _Layer
        self._Image = _Image
        self._ObjectGroup = _ObjectGroup
        self._ImageLayer = _ImageLayer

        self.filepath = filepath
        self.root = ET.parse(filepath).getroot()
        self.version = float(self.root.attrib['version'])
        self.orientation = self.root.attrib['orientation']
        self.renderorder = self.root.attrib['renderorder']
        self.width = int(self.root.attrib['width'])
        self.height = int(self.root.attrib['height'])
        self.tilewidth = int(self.root.attrib['tilewidth'])
        self.tileheight = int(self.root.attrib['tileheight'])

        self.tilesets = [_Tileset(self, i) for i in self.root.findall('tileset')]
        self.layers = [_Layer(self, i) for i in self.root.findall('layer')]
        self.objectgroups = [_ObjectGroup(self, i) for i in self.root.findall('objectgroup')]
        self.imagelayers = [_ImageLayer(self, i) for i in self.root.findall('imagelayer')]

    def get_tile(self, i):
        """Traverse tilesets and return an Image object for that particular tile"""
        for tileset in self.tilesets:
            firstgid = tileset.firstgid
            lastgid = (tileset.columns * tileset.rows) + firstgid
            if firstgid <= i <= lastgid:
                return tileset.get(i)

class PygletMap(Map):
    """An extended map that provides functionality for image manipulation via Pyglet"""
    pyglet = __import__('pyglet')

    def __init__(self, filepath):
        Map.__init__(self, filepath, _Layer=PygletLayer, _Image=PygletImage, _Tileset=PygletTileset)

    def draw(self):
        for layer in self.layers:
            layer.batch.draw()
