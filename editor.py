import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize, time_mirror

def zoomFrame(clip, result,cropped, center):
    n_clip = clip.crop(width=cropped[0],
                       height=cropped[1],
                       x_center = center[0],
                       y_center = center[1])
    
    return n_clip.resize(result)

def zoomIn(clip, croppedSize ,center=None, duration=5,
            initial_duration = 3, final_duration = 2):
    ogSize = clip.size
    w = ogSize[0]
    h = ogSize[1]
    fps = 24

    final = clip.set_duration(initial_duration)
    clip = clip.set_duration(1/fps)

    n_iter = duration*fps

    if not center:
        center = (w/2, h/2)

    xSpeed = (w - croppedSize[0])/n_iter
    ySpeed = (h - croppedSize[1])/n_iter
    curr_clip = clip

    for i in range(n_iter):
        w -= xSpeed
        h -= ySpeed
        curr_clip = zoomFrame(
            clip,
            ogSize,
            (w, h),
            center
        )

        final = mpy.concatenate_videoclips([final, curr_clip])
    final = mpy.concatenate_videoclips([final, curr_clip.set_duration(final_duration)])

    return final

def zoomOut(clip, croppedSize, center=None, duration=3
    ,       initial_duration = 2, final_duration = 2):
    total_duration = initial_duration+duration+final_duration

    clip = zoomIn(clip, croppedSize, center=None,
                  initial_duration=final_duration,
                  final_duration=initial_duration+1,
                  duration=duration)
    
    return time_mirror(clip.subclip(0,total_duration))