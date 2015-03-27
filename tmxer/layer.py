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
