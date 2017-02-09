AutoEditMovie
==========

Learning MoviePy: Mirror, Edit and Concatination

Author: Chris Robertson

License: Released under the BSD license

Purpose: Wrapper script for Movie.py a Python CLI Video Editor, curently can mirror a movie clip.

Usage:
```
Open Terminal
sudo pip install moviepy
sudo pip install Pillow==2.1.0
git clone https://github.com/electronicsleep/AutoEditMovie.git
cd AutoEditMovie
mkdir Camera1
#MOVE MOVIE FILE TO SDIR LOCATION DEFAULT: ./Camera1
cp moviefile.mp4 Camera1/moviefile.mp4
#CREATE A MIRRORED VIDEO
python autoeditmovie.py -m moviefile.mp4
```

Todo/Ideas:
* Verified mirror works on OSX/Linux
* Get edit and concatinate working
* Stitch a bunch of photos together
* Unclear if edit should work on all files
* Need to think though solid workflows
* This is an experiment

Resources:
https://www.python.org/

Resources:
http://zulko.github.io/moviepy/
