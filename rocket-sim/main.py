import handler
import pygame
pygame.init()
print("\n")

# 10 pixels = 1 meter

# -- Window --
WIDTH, HEIGHT = 1080, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Rocket Simulator")

# -- Colors --
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_GRAY = (80, 78, 81)
GREEN = (0, 255, 0)

def main():
    run = True
    clock = pygame.time.Clock()
    object = handler.Rocket(RED, 1, 400, 1000, 1)
    object.add_parachute(1.75, 0.5) # drag coefficient, m^2 parachute
    #object.parachute()
    object.add_rocket_drag(0.5, 0.0078) # drag coefficient, m^2 rocket
    #object.update_pos() # Only for testing without graphics
    object.calculate_trajectory()

    frame = 0
    while run:
        clock.tick(100)
        WIN.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        object.update_pos(frame)
        object.draw(WIN)
        pygame.draw.rect(WIN, GREEN, (0, 1000, 1080, 80))

        pygame.display.update()
        frame += 1

    pygame.quit()

    
# -- Main --
if __name__ == "__main__":
    main()