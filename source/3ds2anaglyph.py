#!/usr/bin/env python
import sys, os
from PIL import Image
from PIL import MpoImagePlugin

from PIL.ImageOps import grayscale as greyscale
from PIL.ImageOps import colorize as colourise

def conv(files):
    for file in files:
        name, ext = os.path.splitext(file)
        im = Image.open(file)
        im.seek(0)
        l = im.copy()
        im.seek(1)
        r = im.copy()

        l = greyscale(l)
        l = colourise(l, (0,0,0),(255,0,0))

        r = greyscale(r)
        r = colourise(r, (0,0,0),(0,255,255))

        o = Image.blend(l,r,0.5)
        o.save(name + ".jpg", "JPEG")

if __name__ == "__main__":
    if len(sys.argv) == 1:
       print("""Usage: python 3ds2anaglyph.py file1 file2 ...
or drag & drop files onto the .exe""")
       input("Press Enter to continue...")
       exit()
    conv(sys.argv[1:])
    exit()
