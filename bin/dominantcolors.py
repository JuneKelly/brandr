#! /usr/bin/env python
import colorthief
import sys
import json


def main():
    image_path = sys.argv[1]
    thief = colorthief.ColorThief(image_path)
    palette = thief.get_palette(quality=5)
    result = {
        'path': image_path,
        'palette': palette
    }
    print json.dumps(result, indent=2)

    pass


if __name__ == '__main__':
    main()
