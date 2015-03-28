class Layer:
    def __init__(self, parent, rootnode):
        self.root = rootnode
        self.parent = parent

        self.name = self.root.attrib['name']
        self.width = int(self.root.attrib['width'])
        self.height = int(self.root.attrib['height'])
        self.data = []
        for tile in self.root.findall('./data/tile'):
            self.data.append(int(tile.attrib['gid']))

class ImageLayer:
    # TODO: Put an imagelayer in test.tmx
    # TODO: Implement the rest of ImageLayer
    # TODO: Write tests for ImageLayer
    def __init__(self, parent, rootnode):
        self.parent = parent
        self.root = rootnode

class PygletLayer(Layer):
    """An extended layer that handles all the tile -> window stuff through Pyglet"""

    @property
    def pyglet(self):
        # Just a nice shorthand
        return self.parent.pyglet

    def __init__(self, parent, rootnode):
        Layer.__init__(self, parent, rootnode)

        self.sprites = []
        self.batch = self.pyglet.graphics.Batch()

        for i, v in enumerate(self.data):
            rows_completed = (i // self.width) + 1
            if v > 0:
                self.sprites.append(self.pyglet.sprite.Sprite(self.parent.get_tile(v),
                    (i % self.width) * self.parent.tilewidth, 
                    (self.height * self.parent.tileheight) - (rows_completed * self.parent.tileheight),
                    batch=self.batch))
