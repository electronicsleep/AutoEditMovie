#!/usr/bin/python

# Author: https://github.com/electronicsleep
# Date: 01/30/2016
# Purpose: Learning MoviePy: Mirror, Edit and Concatination
# Released under the BSD license

import errno
import sys
import os
import argparse
from moviepy.editor import *

# Running:
# Usage: python autoeditmovie.py -m moviefile.mp4
# Future: python autoeditmovie.py [-m] [-e] [-c]

# Set source and destination
sdir = "Camera1/"
ddir = "Camera1/MoviePyOutput/"

# Create dir and process video files

# Make dir if they are not present


def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


def main():

    if args.verbose:
        print("Verbose ON")

    mkdir_p(sdir)
    mkdir_p(ddir)

    try:
        sys.argv[2]
    except IndexError:
        print("Usage: autoeditmovie.py -m moviefile.mp4")
        sys.exit(0)
    else:
        print("Checking movie file")

    for arg in sys.argv:
        print("Argument: %s" % str(arg))

    videofile = sys.argv[2]

    print("Videofile %s" % str(videofile))

    # Start mirror effect

    if sys.argv[1] == '-m':
        from moviepy.editor import VideoFileClip, clips_array, vfx
        # add 10px contour
        clip1 = VideoFileClip(sdir + videofile).margin(10)
        clip2 = clip1.fx(vfx.mirror_x)
        clip3 = clip1.fx(vfx.mirror_y)
        clip4 = clip1.fx(vfx.mirror_y)
        clip4 = clip4.fx(vfx.mirror_x)
        # clip4 = clip1.resize(0.60) # downsize 60%
        final_clip = clips_array([[clip1, clip2],
                            [clip3, clip4]])
        final_clip.resize(width=1280).write_videofile(ddir + "mirror.mp4")

    # End mirror effect

    # Start edit movie edits all in one dir currently

    if sys.argv[1] == '-e':

        os.listdir(sdir)
        from os import listdir
        from os.path import isfile, join
        onlyfiles = [f for f in listdir(sdir) if isfile(join(sdir, f))]

        mp4files = []
        print("FILES")
        for file in onlyfiles:
            if file.endswith("MP4"):
                print(file)
                mp4files.append(file)
                print("MP4 FILES")

            for file in mp4files:
                print(file)

        # Load mp4 and select the subclip
        clip = VideoFileClip(sdir + file).subclip(00,10)

        # Reduce the audio volume (volume x 0.8)
        # clip = clip.fx( afx.volumex, 0.8)

        # Add logo to movie
        # clip = ImageClip(ddir + "logo.jpg")
        # clip = ImageClip(100 100) # a (height x width x 3) RGB numpy array
        # clip = video.to_ImageClip(t='00:00:00') # frame at t=1 hour.
        # clip = video.to_ImageClip(t='01:00:00') # frame at t=1 hour.

        # clip = ImageClip(ddir + "logo.jpg", transparent=False) # True is the default
        # clip.mask # the alpha layer of the picture.

        # Generate a text clip. You can customize the font, color, etc.
        txt_clip = TextClip("MEMORY ECHO",fontsize=200,color='black')

        # Say that you want it to appear 10s at the center of the screen
        txt_clip = txt_clip.set_pos('bottom').set_duration(10)

        # Overlay the text clip on the first video clip
        video = CompositeVideoClip([clip, txt_clip])

        # Write the result to a file
        video.to_videofile(ddir + file, fps=24, codec='mpeg4', audio=False)

    # End edit move

    # Start concatenate clips effect

    if sys.argv[1] == '-c':

        print("### CONCAT CLIPS ###")
        onlyfiles = [f for f in listdir(ddir) if isfile(join(ddir, f))]

        mp4files = []
        print("OUTPUT FILES")
        for file in onlyfiles:
            if file.endswith("MP4"):
                print(file)
                mp4files.append(file)

        num = 0
        for file in mp4files:
            print("CONCAT FILE" + file)
            num = num + 1
            print(file)

        # from moviepy.editor import VideoFileClip, concatenate_videoclips
        # clip1 = VideoFileClip(ddir + "videoexample.MP4")
        # clip2 = VideoFileClip(ddir + "videoexample.MP4")
        # clip3 = VideoFileClip(ddir + "videoexample.MP4")

        # Build All
        final_clip = concatenate_videoclips([clip1,clip2,clip3])
        final_clip.write_videofile(ddir + "concatenation.mp4")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mirror', '-m', help='Mirror movie clip')
    parser.add_argument('--verbose', '-v', help='Verbose', default=True)
    args = parser.parse_args()
    main()
