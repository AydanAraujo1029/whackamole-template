import pygame
import random


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))

        mole_x=0
        mole_y=0


        def render_mole(x,y):
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))

        def draw_grid():
            # draw horizontal lines
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    (0,0,0),
                    (0, i * 32),
                    (640, i * 32),
                    1
                )
            # draw vertical lines
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    (0,0,0),
                    (i * 32, 0),
                    (i * 32, 512),
                    1
                )


        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type==pygame.MOUSEBUTTONDOWN:
                    (a,b)=event.pos
                    a=a//32*32
                    b=b//32*32
                    if a==mole_x and b==mole_y:

                        x = random.randrange(0, 20)
                        y = random.randrange(0, 16)
                        mole_x=32*x
                        mole_y=32*y



            screen.fill("light green")
            draw_grid()
            render_mole(mole_x,mole_y)
            pygame.display.flip()
            clock.tick(60)
            pygame.display.update()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
