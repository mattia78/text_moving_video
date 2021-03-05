# Import everything needed to edit video clips
from moviepy.editor import *

import random

import gizeh

# RESOLUTION
W = 1280
H = 720
duration = 5
max_distance = 1200

text_string = ["primo", "secondo", "terzo"]

def make_frame(t):
    surface = gizeh.Surface(W,H)
    current_text = text_string[int((t*len(text_string))//5)]
    text = gizeh.text(current_text, fontsize = 80, fontfamily="Impact", fill=(1,1,1), xy=(W/2, min(340,-340+max_distance*((t*len(text_string)/duration)%1))))
    text.draw(surface)
    return surface.get_npimage()

clip2 = VideoClip(make_frame, duration=duration)

clip2.write_videofile("my_video.mp4",fps=12)
