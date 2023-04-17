import pygame
import math
import drag
from termcolor import colored

# -- Classes --
class Rocket:

    def __init__(self, color, timestep, start_x, start_y, mass):
        self.color = color
        self.timestep = timestep
        self.x = start_x
        self.y = start_y
        self.mass = mass

        self.Cd = 0
        self.A = 0

        self.printed = False
        self.printed2 = False


    def draw(self, win):
        FONT = pygame.font.SysFont("comicsans", 16)

        image = pygame.image.load("./rocket-sim/parachute-man.png")
        win.blit(image, (self.x-100, self.y-200))
        #pygame.draw.circle(win, self.color, (self.x, self.y), 10)

        # -- Text --
        distance_text = FONT.render(f"{round((self.y / 10),2)} m", 1, (255, 255, 255))
        win.blit(distance_text, (self.x + 10, self.y))

    def add_parachute(self, Cd, A):
        self.Cd = Cd
        self.A = A

    def update_pos(self):
        W = self.mass #weight of payload in kg
        Cd = self.Cd #drag coefficient of parachute
        r = 1.229 #density of air in kg/m^3
        A = self.A #area of parachute in m^2
        g = 9.81 #acceleration due to gravity in m/s^2

        vel = drag.velocity(W, Cd, r, A)
        if self.printed == False:
            if vel > 5:
                print(f"\n({colored('X', 'blue')}) Current velocity: {colored(round(vel,2),'red')} m/s \n")
            else:
                print(f"\n({colored('X', 'blue')}) Current velocity: {colored(round(vel,2),'green')} m/s \n")
            self.printed = True

        self.y += vel/10 * self.timestep

    def parachute(self):
        W = self.mass #weight of payload in kg
        Cd = self.Cd #drag coefficient of parachute
        A = self.A
        r = 1.229 #density of air in kg/m^3
        g = 9.81 #acceleration due to gravity in m/s^2

        if self.printed2 == False:
            x = round(drag.get_area(W, Cd, r, 5),2)
            print(f"({colored('X', 'blue')}) Safe 5m/s speed = {colored(x, 'green')} m^2 parachute")
            if A < x:
                print(f"({colored('X', 'blue')}) Current size: {colored(A, 'red')} m^2")
            else:
                print(f"({colored('X', 'blue')}) Current size: {colored(A, 'green')} m^2")
            self.printed2 = True