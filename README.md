3ds to anaglyphic photo converter
=================================

Batch convert 3DS photos to red-cyan anaglyphic images with Python 3 &amp; ~~PIL~~ Pillow. 

Converts 3DS photos to anaglyphic images, for viewing on devices without 3d screens using your (my) 2 coloured 80s nerd glasses.

Requirements: A version of Pillow from after 25 Jul 2014 which is when MPO format support was added.

Use:
```bat
python 3ds2anaglyph.py file1.mpo file2.mpo ....etc
```

Creates .jpgs alongside the .MPO files you feed it, so if the SD card is full it'll fail unless you copy the .MPO files to another folder first.

Windows .exe file included for people who can't/won't install Python. Just drag & drop a bunch of .MPO files onto the .exe file.

Currently only produces images for red (left-eye) / cyan (right eye) glasses.