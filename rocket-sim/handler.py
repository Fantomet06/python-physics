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

        self.Rocket_Cd = 0
        self.Rocket_A = 0

        self.Parachute_Cd = 0
        self.Parachute_A = 0
        self.Parachute_Active = False

        self.printed = False
        self.printed2 = False
        self.vel = []

    def draw(self, win):
        FONT = pygame.font.SysFont("comicsans", 16)

        if self.Parachute_Active == True:
            image = pygame.image.load("./rocket-sim/parachute-man.png")
            win.blit(image, (self.x-100, self.y-200))
        else:
            pygame.draw.rect(win, self.color, (self.x-10, self.y-50, 20, 50))
        #pygame.draw.circle(win, self.color, (self.x, self.y), 10)

        # -- Text --
        distance_text = FONT.render(f"{round(((1000-self.y)/10),2)} m", 1, (255, 255, 255))
        win.blit(distance_text, (self.x + 10, self.y))

    def add_parachute(self, Cd, A):
        self.Parachute_Cd = Cd
        self.Parachute_A = A

    def add_rocket_drag(self, Cd, A):
        self.Rocket_Cd = Cd
        self.Rocket_A = A
        
    def calculate_trajectory(self):  
        print(self.Rocket_Cd, self.Parachute_Cd, self.mass, self.Rocket_A, self.Parachute_A)  
        vel = drag.trajectory(self.Rocket_Cd, self.Parachute_Cd, self.mass, self.Rocket_A, self.Parachute_A, 8.7, 2, 2.9)
        self.vel = vel
        print(self.vel)
        print("calculated trajectory")

    def update_pos(self, frame):

        """
        if self.printed == False:
            if vel > 5:
                print(f"\n({colored('X', 'blue')}) Current velocity: {colored(round(vel,2),'red')} m/s \n")
            else:
                print(f"\n({colored('X', 'blue')}) Current velocity: {colored(round(vel,2),'green')} m/s \n")
            self.printed = True
        """
        vel = self.vel
        #print(vel[frame])
        if vel[frame] < vel[frame-1]:
            self.Parachute_Active = True
        self.y = 1000 - vel[frame] * 10

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