import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize


clip1 = mpy.ImageClip("hollow knight.png").set_duration(5)
(w,h) = clip1.size

clip2 = crop(clip1,width = w*0.3, height = h*0.3, x_center=w/2, y_center=h/2)
clip2 = clip2.resize(width = w)

video = mpy.concatenate_videoclips([clip1, clip2], method="compose")
video.write_videofile('test.mp4', fps=24)