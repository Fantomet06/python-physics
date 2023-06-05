import pygame
from random import randint
pygame.init()
print("\n")

# -- Window --
WIDTH, HEIGHT = 620, 620
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("wee woo")

# -- Colors --
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
DARK_GRAY = (80, 78, 81)
GREEN = (0, 255, 0)

ball = pygame.image.load("./rocket-sim/parachute-man.png")
ball = pygame.transform.scale(ball,(35,35))
WIN.blit(ball, [100, 100])

pos = [74, 34]
speed = [1, 1]

def fill(surface, color):
    """Fill all pixels of the surface with color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            a = surface.get_at((x, y))[3]
            surface.set_at((x, y), pygame.Color(r, g, b, a))

def main():
    color = (255, 0, 0, 255)
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(BLACK)

        pos[0] += speed[0]
        pos[1] += speed[1]

        ball = pygame.image.load("./bounce/dvd-logo.png")
        ball = pygame.transform.scale(ball,(74,34))
        fill(ball, color)
        WIN.blit(ball, tuple(pos))


        if pos[1] <= 0 or pos[1]+34 >= HEIGHT:
           speed[1] = -speed[1]
           color = tuple([randint(0, 255), randint(0, 255), randint(0, 255), 255])
        if pos[0] <= 0 or pos[0]+74 >= WIDTH:
            speed[0] = -speed[0]
            color = tuple([randint(0, 255), randint(0, 255), randint(0, 255), 255])


        pygame.display.update()

    pygame.quit()

    
# -- Main --
if __name__ == "__main__":
    main()