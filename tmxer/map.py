import xml.etree.ElementTree as ET
from tmxer.tileset import Tileset
from tmxer.layer import Layer
from tmxer.layer import ImageLayer
from tmxer.objects import ObjectGroup

class Map:
    def __init__(self, xml):
        self.root = xml.getroot()
        self.version = float(self.root.attrib['version'])
        self.orientation = self.root.attrib['orientation']
        self.renderorder = self.root.attrib['renderorder']
        self.width = int(self.root.attrib['width'])
        self.height = int(self.root.attrib['height'])
        self.tilewidth = int(self.root.attrib['tilewidth'])
        self.tileheight = int(self.root.attrib['tileheight'])

        self.tilesets = [Tileset(self, i) for i in self.root.findall('tileset')]
        self.layers = [Layer(self, i) for i in self.root.findall('layer')]
        self.objectgroups = [ObjectGroup(self, i) for i in self.root.findall('objectgroup')]
        self.imagelayers = [ImageLayer(self, i) for i in self.root.findall('imagelayer')]

    @classmethod
    def frompath(cls, filepath):
        return cls(ET.parse(filepath))
