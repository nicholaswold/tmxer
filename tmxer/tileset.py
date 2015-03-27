from tmxer.image import Image

class Tileset:
    def __init__(self, parent, rootnode):
        """Abstract a tileset into an object"""
        self.parent = parent
        self.root = rootnode
        self.firstgid = int(self.root.attrib['firstgid'])
        self.name = self.root.attrib['name']
        self.tilewidth = int(self.root.attrib['tilewidth'])
        self.tileheight = int(self.root.attrib['tileheight'])
        self.spacing = int(self.root.attrib['spacing'])
        self.margin = int(self.root.attrib['margin'])
        self.image = Image(self, self.root.find('image'))
