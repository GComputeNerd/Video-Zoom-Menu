import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize

def zoomFrame(clip, result,cropped, center):
    n_clip = clip.crop(width=cropped[0],
                       height=cropped[1],
                       x_center = center[0],
                       y_center = center[1])
    
    return n_clip.resize(result)

clip1 = mpy.ImageClip("hollow knight.png").set_duration(5)
size = clip1.size

clip2 = zoomFrame(clip1, size, (320, 320), (size[0]/2, size[1]/2))

video = mpy.concatenate_videoclips([clip1, clip2], method="compose")
video.write_videofile('test.mp4', fps=24)