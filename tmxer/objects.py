class ObjectGroup:
    def __init__(self, parent, rootnode):
        self.parent = parent
        self.root = rootnode
        self.name = self.root.attrib['name']
        self.objects = []
        for o in self.root.findall('object'):
            self.objects.append(Object(self, o))

class Object:
    def __init__(self, parent, rootnode):
        self.parent = parent
        self.root = rootnode
        self.id = int(self.root.attrib['id'])
        self.x = float(self.root.attrib['x'])
        self.y = float(self.root.attrib['y'])
        self.width = float(self.root.attrib['width'])
        self.height = float(self.root.attrib['height'])
