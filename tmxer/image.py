class Image:
    def __init__(self, parent, rootnode):
        self.root = rootnode
        self.parent = parent

        self.source = self.root.attrib['source']
        self.width = int(self.root.attrib['width'])
        self.height = int(self.root.attrib['height'])
        self.margin = parent.margin
