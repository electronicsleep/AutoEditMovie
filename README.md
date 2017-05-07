AutoEditMovie
==========

Learning MoviePy: Mirror, Edit and Concatination

Author: https://github.com/electronicsleep

License: Released under the BSD license

Purpose: Automatic Movie editing with MoviePy a Python CLI Video Editor, curently can mirror a movie clip. Should get you started with the basics of MoviePy.

MoviePy: http://zulko.github.io/moviepy/

![Alt text](screenshot-mirror.jpg?raw=true "Screenshot Mirror")

[Example:] (https://www.youtube.com/watch?v=72_e-N6xUMI)

Usage:
```
Open Terminal
pip install -r requirements.txt
git clone https://github.com/electronicsleep/AutoEditMovie.git
cd AutoEditMovie
mkdir Camera1
# Move movie file to dir location default Camera1
cp moviefile.mp4 Camera1/moviefile.mp4
# Command to create a mirrored video
python autoeditmovie.py -m moviefile.mp4
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
