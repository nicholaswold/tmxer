# tmxer

An abstraction over TMX maps.

Read: Not reliant on any one framework to do the heavy lifting.

tmxer's goals are simple:
  - Be fast
  - Be simple
  - Be useful

tmxer breaks down TMX maps into their base components, allowing you to easily access a wealth of information. Because the TMX spec is not stable, we take only _what we need_. Additionally, we provide some utility classes for commonly-used frameworks like pygame and pyglet that reduce boilerplate.


## How do I work this crazy thing?

```
python setup.py install
```

```
from tmxer.map import Map

level = Map(filepath)
```

That's it. tmxer breaks down the TMX file into its own classes, which can then be navigated and accessed in a sane fashion.

```
level = Map(filepath)

# Let's iterate over our tilesets
for tileset in level.tilesets:
    print(tileset.name)
```

See? Simple.

What if you wanted to work in Pyglet?

```
from tmxer.map import PygletMap

level = PygletMap(filepath)
window = pyglet.window.Window(640, 480)

@window.event
def on_draw():
    window.clear()
    level.draw()
```

You can even extend objectgroups to do physics with something like PyMunk!


## How do I learn more?

Documentation will be located in the `/docs` folder, and will later be hosted externally. Until then, the [TMX spec](https://github.com/bjorn/tiled/wiki/TMX-Map-Format) is very helpful, as tmxer is designed to use the same namespaces.


## How do I help?

If you find the tmxer is _too_ simple for you, and lacking features, file an issue here. Alternatively, fork it. Please include tests. Benchmarks too if applicable. Utility scripts, helping tmxer play nice with other frameworks, are always welcome.
