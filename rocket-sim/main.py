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

def main():
    run = True
    clock = pygame.time.Clock()
    object = handler.Rocket(RED, 1, 400, 100)

    while run:
        clock.tick(60)
        WIN.fill(DARK_GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        object.update_pos()
        object.draw(WIN)

        pygame.display.update()

    pygame.quit()

    
# -- Main --
if __name__ == "__main__":
    main()