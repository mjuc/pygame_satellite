import pygame
import thorpy
from satellite import Satelite

ref_flag=False

def set_sat_refresh():
    ref_flag=True

pygame.init()
sat=Satelite()
screen = pygame.display.set_mode([1200, 700])
#menu
slider_x = thorpy.SliderX(100, (10, 60), "X axis distance")
slider_y = thorpy.SliderX(100, (10, 60), "Y axis distance")
slider_r = thorpy.SliderX(50, (1,10), "Planet radius")
slider_rs = thorpy.SliderX(10, (1,5), "Satellite radius")
slider_m = thorpy.SliderX(160, (20,100), "Planet mass")
slider_G = thorpy.SliderX(500, (5,10), "Gravitational acceleration")
sat_refresh_button = thorpy.make_button("Refresh params",func=set_sat_refresh)
quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
box = thorpy.Box(elements=[slider_x,
                           slider_y,
                           slider_r,
                           slider_rs,
                           slider_m,
                           slider_G,
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
    if ref_flag:
        sat.set_x(slider_x.get_value())
        sat.set_y(slider_y.get_value())
        sat.set_R(slider_r.get_value())
        sat.set_Rs(slider_rs.get_value())
        sat.set_GM(slider_m.get_value(),slider_G.get_value())
    menu.react(event)

pygame.quit()
