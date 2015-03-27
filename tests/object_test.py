def test_init(basic_map):
    group = basic_map.objectgroups[0]
    assert(group.parent == basic_map)
    assert(group.name == "Collisions")
    assert(len(group.objects) == 7)
    o = group.objects[0]
    assert(o.id == 5)
    assert(o.x == 448)
    assert(o.y == 176)
    assert(o.width == 128)
    assert(o.height == 16)
