def test_init(basic_map):
    image = basic_map.tilesets[0].image

    assert(image.parent == basic_map.tilesets[0])
    assert(image.source == 'tileset.gif')
    assert(image.width == 154)
    assert(image.height == 69)
    assert(image.margin == image.parent.margin)
