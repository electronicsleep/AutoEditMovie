AutoEditMovie
==========

MoviePy: Mirror, Edit

Author: https://github.com/electronicsleep

License: Released under the BSD license

Purpose: Automatic Movie editing with MoviePy a Python CLI Video Editor, curently can mirror a movie clip. Should get you started with the basics of MoviePy.

![Alt text](screenshot.jpg?raw=true "Screenshot")

[Example:] (https://www.youtube.com/watch?v=72_e-N6xUMI)

Usage:
```
Open Terminal
git clone https://github.com/electronicsleep/AutoEditMovie.git
cd AutoEditMovie
pip install -r requirements.txt
mkdir Camera1
# Move movie file to dir location default Camera1
cp moviefile.mp4 Camera1/moviefile.mp4
# Command to create a mirrored video

# Running:
# Usage: python autoeditmovie.py -m moviefile.mp4
# Future: python autoeditmovie.py [-m] [-e] [-c]

# Set source and destination
# sdir = "Camera1/"
# ddir = "Camera1/MoviePyOutput/"

# Create dir and process video files

# Make dir if they are not present
```

Todo/Ideas:
* Verified mirror works on OSX/Linux
* Get edit and concatinate working
* Stitch a series of photos together
* Multiple camera workflow
* Different effects
* This is an experiment

``` 
# Modules Tested
pip install moviepy==0.2.3.2
pip install Pillow==2.1.0
```

Resources:
https://www.python.org/

Resources:
http://zulko.github.io/moviepy/
