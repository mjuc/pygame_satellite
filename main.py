import pygame
import thorpy
from satellite import Satelite

pygame.init()

screen = pygame.display.set_mode([1000, 700])
#menu
slider_x = thorpy.SliderX(100, (10, 60), "X axis distance")
slider_y = thorpy.SliderX(100, (10, 60), "Y axis distance")
slider_r = thorpy.SliderX(50, (1,10), "Planet radius")
slider_rs = thorpy.SliderX(10, (1,5), "Satellite radius")
slider_m = thorpy.SliderX(160, (20,100), "Planet mass")
sat_refresh_button = thorpy.make_button("Refresh params")#uttery useless
quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
box = thorpy.Box(elements=[slider_x,
                           slider_y,
                           slider_r,
                           slider_rs,
                           slider_m,
                           sat_refresh_button,
                           quit_button])
menu = thorpy.Menu(box)

for element in menu.get_population():
    element.surface = screen

box.set_topleft((0,0))
box.blit()
box.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    menu.react(event)
    print(slider_x.get_value())
pygame.quit()
