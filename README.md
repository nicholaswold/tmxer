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
pip3 install tmxer
```

```
from tmxer.map import Map
Map.frompath(filepath)
# or
Map(ET.parse(filepath))
```

That's it. tmxer breaks down the TMX file into its own classes, which can then be navigated and accessed in a sane fashion.

```
level = Map.frompath(filepath)

# Let's iterate over our tilesets
for tileset in level.tilesets:
    print(tileset.name)
```

See? Simple.


## How do I learn more?

Documentation will be located in the `/docs` folder, and will later be hosted externally. Until then, the [TMX spec](https://github.com/bjorn/tiled/wiki/TMX-Map-Format) is very helpful, as tmxer is designed to use the same namespace.


## How do I help?

If you find the tmxer is _too_ simple for you, and lacking features, file an issue here. Alternatively, fork it. Please include tests. Benchmarks too if applicable. Utility scripts, helping tmxer play nice with other frameworks, are always welcome.
