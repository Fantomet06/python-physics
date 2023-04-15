import pygame
import math
import drag



# -- Classes --
class Rocket:

    def __init__(self, color, timestep, start_x, start_y, mass):
        self.color = color
        self.timestep = timestep
        self.x = start_x
        self.y = start_y
        self.mass = mass


    def draw(self, win):
        FONT = pygame.font.SysFont("comicsans", 16)

        image = pygame.image.load("./rocket-sim/parachute-man.png")
        win.blit(image, (self.x-100, self.y-200))
        #pygame.draw.circle(win, self.color, (self.x, self.y), 10)

        # -- Text --
        distance_text = FONT.render(f"{self.y:.2f} x", 1, (255, 255, 255))
        win.blit(distance_text, (self.x + 10, self.y))

    def update_pos(self):
        W = self.mass #weight of payload in kg
        Cd = 1.75 #drag coefficient of parachute
        r = 1.229 #density of air in kg/m^3
        A = 0.5 #area of parachute in m^2
        g = 9.81 #acceleration due to gravity in m/s^2

        vel = drag.velocity(W, Cd, r, A)

        self.y += vel * self.timestep