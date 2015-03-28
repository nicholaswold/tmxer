# Getting Started

tmxer is a lightweight python engine, so if you want to just grab tmxer and go, open a terminal and do this:

```
pip3 install -e git+https://github.com/nicholaswold/tmxer#egg=tmxer
```

If you're trying to embed this library in a package, open up your requirements.txt file and paste `-e git+https://github.com/nicholaswold/tmxer#egg=tmxer` into it. Then run `pip3 install -r requirements.txt` and you're good to go.

Now open up a python interpreter, and get an example tiled map or something.

```
from tmxer.map import Map
filename = TILEDMAPHERE
level = Map(filename)
```

That should give you the barebones Map object. From here, you can write functions to use the map data in this object. Or, you could skip that step and write a class to extend Map so that all the functionality you want is right there. If you want examples, go check out `map.py` for the other types of maps we have.

*WIP*
