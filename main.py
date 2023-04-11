import pygame 

# -- Global Constants --
width = 800
height = 800
background_colour = (255,255,255)

running = True

def main(running):
    #draw the screen
    draw()

    while running:
        ev = pygame.event.get()

        for event in ev:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    break
        
        draw_circle()

# -- Functions --
def draw():
    global screen

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("My Game")
    screen.fill(background_colour)
    pygame.display.update()

def draw_circle():
    pygame.draw.circle(screen, (0,0,0), (400,400), 50)
    pygame.display.update()

# -- Main Program --
if __name__ == "__main__":
    main(running)