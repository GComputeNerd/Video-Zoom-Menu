import moviepy.editor as mpy
from editor import *
import pygame
import pygame_gui

# clip1 = mpy.ImageClip("hollow knight.png").set_duration(1/24)
# w,h = clip1.size
# croppedSize = (w*0.3, h*0.3)
# zoomIn(clip1, croppedSize).write_videofile("test1.mp4", fps=24)
# zoomOut(clip1, croppedSize).write_videofile("test2.mp4", fps=24)


pygame.init()

pygame.display.set_caption("Test")

is_running = True

window = pygame.display.set_mode((800, 600))
background = pygame.Surface((800,600))
background.fill(pygame.Color("#000000"))

manager = pygame_gui.UIManager((800, 600))
clock = pygame.time.Clock()

image = pygame_gui.elements.UIImage(
    relative_rect=pygame.Rect((100,100),(500,300)),
    image_surface=pygame.image.load('hollow knight.png'),
    manager=manager
)

while is_running:
    time_delta = clock.tick(60)/1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        manager.process_events(event)
    
    manager.update(time_delta)
    
    window.blit(background, (0,0))
    manager.draw_ui(window)

    pygame.display.update()