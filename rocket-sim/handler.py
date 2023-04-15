import pygame
import math
import drag

# -- Classes --
class Rocket:

    def __init__(self, color, timestep, start_x, start_y):
        self.color = color
        self.timestep = timestep
        self.x = start_x
        self.y = start_y


    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), 10)

    def update_pos(self):
        W = 1 #weight of payload in kg
        Cd = 1.75 #drag coefficient of parachute
        r = 1.229 #density of air in kg/m^3
        A = 0.5 #area of parachute in m^2
        g = 9.81 #acceleration due to gravity in m/s^2

        vel = drag.velocity(W, Cd, r, A)

        self.y += vel * self.timestep