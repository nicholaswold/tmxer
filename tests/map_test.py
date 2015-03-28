def test_init(basic_map):
    """Make sure that maps load from xml correctly"""
    assert(basic_map.version == 1.0)
    assert(basic_map.orientation == "orthogonal")
    assert(basic_map.renderorder == "right-down")
    assert(basic_map.width == 40)
    assert(basic_map.height == 24)
    assert(basic_map.tileheight == 16)
    assert(basic_map.tilewidth == 16)

    assert(len(basic_map.tilesets) == 1)
    assert(len(basic_map.layers) == 2)
    #assert(len(basic_map.objectgroups) == 1)
    #assert(len(basic_map.imagelayers) == 0)

def test_pyglet(pyglet_map):
    """Make sure that maps load from xml correctly"""
    assert(pyglet_map.version == 1.0)
    assert(pyglet_map.orientation == "orthogonal")
    assert(pyglet_map.renderorder == "right-down")
    assert(pyglet_map.width == 40)
    assert(pyglet_map.height == 24)
    assert(pyglet_map.tileheight == 16)
    assert(pyglet_map.tilewidth == 16)

    assert(len(pyglet_map.tilesets) == 1)
    assert(len(pyglet_map.layers) == 2)

def test_pyglet_draw(pyglet_map):
    window = pyglet_map.pyglet.window.Window(pyglet_map.width * pyglet_map.tilewidth,
            pyglet_map.height * pyglet_map.tileheight)
    label = pyglet_map.pyglet.text.Label(text="Press ESC to continue...", x=300, y=300, anchor_x='center')

    @window.event
    def on_draw():
        pyglet_map.draw()
        label.draw()

    pyglet_map.pyglet.app.run()
