import os

class Image:
    def __init__(self, parent, rootnode):
        self.root = rootnode
        self.parent = parent

        self.source = self.root.attrib['source']
        self.width = int(self.root.attrib['width'])
        self.height = int(self.root.attrib['height'])
        self.margin = parent.margin
        self.filename = os.path.join(os.path.dirname(self.parent.parent.filepath), self.source)

class PygletImage(Image):
    def __init__(self, parent, rootnode):
        Image.__init__(self, parent, rootnode)
        self.image = self.pyglet.image.load(self.filename)

    @property
    def pyglet(self):
        return self.parent.pyglet

    def trim(self):
        return self.image.get_region(self.margin, self.margin, self.width - (self.margin * 2),
                self.height - (self.margin * 2))
