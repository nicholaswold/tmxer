def test_init(basic_map):
    tileset = basic_map.tilesets[0]

    assert(tileset.parent == basic_map)
    assert(tileset.firstgid == 1)
    assert(tileset.name == "tileset")
    assert(tileset.tilewidth == 16)
    assert(tileset.tileheight == 16)
    assert(tileset.spacing == 1)
    assert(tileset.margin == 1)
