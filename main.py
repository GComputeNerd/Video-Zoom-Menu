import moviepy.editor as mpy
from moviepy.video.fx.all import crop, resize

def zoomFrame(clip, result,cropped, center):
    n_clip = clip.crop(width=cropped[0],
                       height=cropped[1],
                       x_center = center[0],
                       y_center = center[1])
    
    return n_clip.resize(result)

clip1 = mpy.ImageClip("hollow knight.png").set_duration(2)
size = clip1.size

clip2 = zoomFrame(clip1, size, (320, 320), (size[0]/2, size[1]/2))

ogSize = clip1.size
croppedSize = (320, 320)
center = (ogSize[0]/2, ogSize[1]/2)
clips = [clip1]
n_iter = 5
xSpeed = (ogSize[0] - croppedSize[0])/n_iter
ySpeed = (ogSize[1] - croppedSize[1])/n_iter
for i in range(5):
    clips.append(
        zoomFrame(
            clips[-1],
            ogSize,
            (ogSize[0] - i*xSpeed, ogSize[1] - i*ySpeed),
            center
        )
    )

video = mpy.concatenate_videoclips(clips, method="compose")
video.write_videofile('test.mp4', fps=24)