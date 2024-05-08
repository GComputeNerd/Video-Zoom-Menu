from moviepy.editor import *

clip = ImageClip("hollow knight.png").set_duration(5)

video = concatenate_videoclips([clip], method="compose")
video.write_videofile('test.mp4', fps=24)