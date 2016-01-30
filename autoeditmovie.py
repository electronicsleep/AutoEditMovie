#!/usr/bin/python

# Author: Chris Robertson <electronicsleep@gmail.com>
# Date: 01/30/2016
# Purpose: Learning MoviePy: Mirror, Edit and Concatination
# Released under the MIT license

# Running:
# Usage: python autoeditmovie.py -m moviefile.mp4

# Future: python autoeditmovie.py [-m] [-e] [-c]

# WRAPPER SCRIPT FOR THE MOVIEPY PYTHON LIBRARY

# SET SOURCE AND DESINATIONS OF MOVIE FILES
sdir = "Camera1/"
ddir = "Camera1/MoviePyOutput/"

# CREATE DIRS AND PROCESS VIDEO FILES

import errno    
import sys
import os
from moviepy.editor import *

# MAKE DIRS IF THEY ARE NOT PRESENT

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

mkdir_p(sdir)
mkdir_p(ddir)

# CHECK FOR ARGS AND GIVE USAGE

total = len(sys.argv)
cmdargs = str(sys.argv)

#print ("The total numbers of args passed to the script: %d " % total)
#print ("Args list: %s " % cmdargs)

try:
  sys.argv[2]
except IndexError: 
  print "Usage: autoeditmovie.py -m moviefile.mp4"
  sys.exit(0)
else:
  print "Checking movie file"

for arg in sys.argv: 
 print ("Argument: %s" % str(arg))

videofile = sys.argv[2]

print ("Videofile %s" % str(videofile))

### START MIRROR EFFECT

if sys.argv[1] == '-m':

 from moviepy.editor import VideoFileClip, clips_array, vfx
 clip1 = VideoFileClip(sdir + videofile).margin(10) # add 10px contour
 clip2 = clip1.fx( vfx.mirror_x)
 clip3 = clip1.fx( vfx.mirror_y)
 clip4 = clip1.fx( vfx.mirror_y)
 clip4 = clip4.fx( vfx.mirror_x)
 #clip4 = clip1.resize(0.60) # downsize 60%
 final_clip = clips_array([[clip1, clip2],
                          [clip3, clip4]])
 final_clip.resize(width=1280).write_videofile(ddir + "mirror.mp4")


### END MIRROR EFFECT


### START EDIT MOVIE EDITS ALL IN ONE DIR CURRENTLY

if sys.argv[1] == '-e':

 os.listdir(sdir)

 from os import listdir
 from os.path import isfile, join
 onlyfiles = [ f for f in listdir(sdir) if isfile(join(sdir,f)) ]


 mp4files = []
 print "FILES"
 for file in onlyfiles:
  #print file
  if file.endswith("MP4"):
   print file
   mp4files.append(file)

 print "MP4 FILES"

 for file in mp4files:
  print file

  # Load mp4 and select the subclip 
  clip = VideoFileClip(sdir + file).subclip(00,10)
 
  # Reduce the audio volume (volume x 0.8)
  #clip = clip.fx( afx.volumex, 0.8)

  # Add logo to movie
  #clip = ImageClip(ddir + "logo.jpg")
  #clip = ImageClip(100 100) # a (height x width x 3) RGB numpy array
  #clip = video.to_ImageClip(t='00:00:00') # frame at t=1 hour.
  #clip = video.to_ImageClip(t='01:00:00') # frame at t=1 hour.

  #clip = ImageClip(ddir + "logo.jpg", transparent=False) # True is the default
  #clip.mask # the alpha layer of the picture.
 
  # Generate a text clip. You can customize the font, color, etc.
  txt_clip = TextClip("MEMORY ECHO",fontsize=200,color='black')
 
  # Say that you want it to appear 10s at the center of the screen
  txt_clip = txt_clip.set_pos('bottom').set_duration(10)
 
  # Overlay the text clip on the first video clip
  video = CompositeVideoClip([clip, txt_clip])
 
  # Write the result to a file
  video.to_videofile(ddir + file ,fps=24, codec='mpeg4', audio=False)

### END EDIT MOVIE


### START CONCATITNATE CLIPS EFFECT

if sys.argv[1] == '-c':

 print "### CONCAT CLIPS ###"
 onlyfiles = [ f for f in listdir(ddir) if isfile(join(ddir,f)) ]

 mp4files = []
 print "OUTPUT FILES"
 for file in onlyfiles:
  if file.endswith("MP4"):
   print file
   mp4files.append(file)

 num=0
 for file in mp4files:
  print "CONCAT FILE" + file
  num = num + 1

 #from moviepy.editor import VideoFileClip, concatenate_videoclips
 #clip1 = VideoFileClip(ddir + "videoexample.MP4")
 #clip2 = VideoFileClip(ddir + "videoexample.MP4")
 #clip3 = VideoFileClip(ddir + "videoexample.MP4")

 #BUILD ALL
 final_clip = concatenate_videoclips([clip1,clip2,clip3])
 final_clip.write_videofile(ddir + "concatenation.mp4")

### END CONCATITNATE CLIPS EFFECT

sys.exit(0)
