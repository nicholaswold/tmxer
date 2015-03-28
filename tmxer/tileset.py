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
        self.image = self.parent._Image(self, self.root.find('image'))
        self.columns = (self.image.width + self.spacing) // (self.tilewidth + self.spacing)
        self.rows = (self.image.height + self.spacing) // (self.tileheight + self.spacing)

class PygletTileset(Tileset):
    def __init__(self, parent, rootnode):
        Tileset.__init__(self, parent, rootnode)
        self.textures = self.pyglet.image.ImageGrid(self.image.trim(), self.rows, self.columns,
                self.tilewidth, self.tileheight, self.spacing, self.spacing)

    @property
    def pyglet(self):
        return self.parent.pyglet

    def transform(self, i):
        """
        Transforms an index anchored at the top left of an image (TMX-style) to an index
        that is anchored on the bottom left.
        """
        oldRow = i // self.columns
        newRow = (self.rows - 1) - oldRow
        shift = (newRow - oldRow) * self.columns
        if i > self.rows * self.columns:
            shift = -shift
        return i + shift - self.firstgid

    def get(self, i):
        return self.textures[self.transform(i)]
