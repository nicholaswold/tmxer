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
    #assert(len(basic_map.layers) == 2)
    #assert(len(basic_map.objectgroups) == 1)
    #assert(len(basic_map.imagelayers) == 0)

def test_fromfile(basic_map_file):
    """Make sure that maps can load a file themselves"""
    assert(basic_map_file.version == 1.0)
    assert(basic_map_file.orientation == "orthogonal")
    assert(basic_map_file.renderorder == "right-down")
    assert(basic_map_file.width == 40)
    assert(basic_map_file.height == 24)
    assert(basic_map_file.tileheight == 16)
    assert(basic_map_file.tilewidth == 16)
