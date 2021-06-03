import pygame
from pygame.constants import USEREVENT
import thorpy
from satellite import Satelite
import numpy as np

RUN_SIM = 1

#defines for colours used by simulation
WHITE = (255, 255, 255)
BLUE = (  0,   0, 255)
GREEN = (  0, 255,   0)
RED = (255,   0,   0)

#instance of model
sat=Satelite()

#custom pygame event responsible for starting simulation
run_sim_event = pygame.event.Event(pygame.USEREVENT+1)

#update model params
def set_sat_refresh():
    print("Refresh values")
    sat.set_R(slider_r.get_value())
    sat.set_Rs(slider_rs.get_value())
    sat.set_GM(slider_m.get_value(),slider_G.get_value())
    sat.set_x(slider_x.get_value())
    sat.set_y(slider_y.get_value()) 

#initialize simulation
def run_sim():
    print("Running simulation")
    pygame.event.post(run_sim_event)
    
pygame.init()
pygame.display.set_caption("Satellite sim")
screen = pygame.display.set_mode([1200, 700])
screen.fill(WHITE)

#menu
#sliders regulating model params
slider_x = thorpy.SliderX(100, (10, 60), "X axis distance")
slider_y = thorpy.SliderX(100, (10, 60), "Y axis distance")
slider_r = thorpy.SliderX(50, (1,10), "Planet radius")
slider_rs = thorpy.SliderX(10, (1,5), "Satellite radius")
slider_m = thorpy.SliderX(160, (20,100), "Planet mass")
slider_G = thorpy.SliderX(500, (5,10), "Gravitational acceleration")
#buttons
sat_refresh_button = thorpy.make_button("Refresh params",func=set_sat_refresh)
run_sim_button = thorpy.make_button("Run simulation",func=run_sim)
quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
box = thorpy.Box(elements=[slider_x,
                           slider_y,
                           slider_r,
                           slider_rs,
                           slider_m,
                           slider_G,
                           sat_refresh_button,
                           run_sim_button,
                           quit_button])
menu = thorpy.Menu(box)

for element in menu.get_population():
    element.surface = screen

box.set_topleft((0,0))
box.blit()
box.update()
pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.USEREVENT+1:
            radius=sat.get_R()
            dist_x=sat.get_x()
            dist_y=sat.get_y()
            sat_radius=sat.get_Rs()
            screen.fill(WHITE)
            box.blit()
            box.update()
            pygame.draw.circle(screen,BLUE,(600,350),radius)
            pygame.draw.circle(screen,
                               GREEN,
                               (600+dist_x+radius+sat_radius,350+dist_y+radius+sat_radius)
                               ,sat_radius)
            pygame.display.update()
            time=np.arange(0,1000,0.01)
            X=sat.calculateX(time)
            Y=sat.calculateY(time)
            radius=sat.get_R()
            sat_radius=sat.get_Rs()
            print(len(X))
            for i in range(0,len(X)):
                screen.fill(WHITE)
                box.blit()
                box.update()
                pygame.draw.circle(screen,BLUE,(600,350),radius)
                pygame.draw.circle(screen,GREEN,(600+int(X[i])+radius+sat_radius,350+int(Y[i])+radius+sat_radius),sat_radius)
                pygame.display.update()                              
        
        menu.react(event)
        pygame.display.update()

pygame.quit()
