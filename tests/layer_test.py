def test_init(basic_map):
    layer = basic_map.layers[0]

    assert(layer.name == "Background")
    assert(layer.width == 40)
    assert(layer.height == 24)
    assert(len(layer.data) == 40*24)
    assert(layer.data[0] == 10)
    assert(len(set(layer.data)) == 1)
