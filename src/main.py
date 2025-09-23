import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spaceship Dodger")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Spaceship properties
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 50, 50
spaceship_img = pygame.Surface((SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
spaceship_img.fill(WHITE)

# Asteroid properties
ASTEROID_WIDTH, ASTEROID_HEIGHT = 40, 40
asteroid_img = pygame.Surface((ASTEROID_WIDTH, ASTEROID_HEIGHT))
asteroid_img.fill(RED)

# Fonts
font = pygame.font.SysFont(None, 36)

def draw_text(text, x, y):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

class Spaceship:
    def __init__(self):
        self.x = WIDTH // 2 - SPACESHIP_WIDTH // 2
        self.y = HEIGHT - SPACESHIP_HEIGHT - 20
        self.speed = 7

    def move(self, dx):
        self.x += dx * self.speed
        self.x = max(0, min(WIDTH - SPACESHIP_WIDTH, self.x))

    def draw(self):
        screen.blit(spaceship_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

class Asteroid:
    def __init__(self, speed):
        self.x = random.randint(0, WIDTH - ASTEROID_WIDTH)
        self.y = -ASTEROID_HEIGHT
        self.speed = speed

    def move(self):
        self.y += self.speed

    def draw(self):
        screen.blit(asteroid_img, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, ASTEROID_WIDTH, ASTEROID_HEIGHT)

def main():
    clock = pygame.time.Clock()
    spaceship = Spaceship()
    asteroids = []
    asteroid_timer = 0
    score = 0
    difficulty = 1
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx = 0
        if keys[pygame.K_LEFT]:
            dx = -1
        if keys[pygame.K_RIGHT]:
            dx = 1
        spaceship.move(dx)

        # Increase difficulty over time
        difficulty = 1 + score // 100
        asteroid_speed = 4 + difficulty
        asteroid_spawn_rate = max(20, 60 - difficulty * 5)

        # Spawn asteroids
        asteroid_timer += 1
        if asteroid_timer >= asteroid_spawn_rate:
            asteroids.append(Asteroid(asteroid_speed))
            asteroid_timer = 0

        # Move and draw asteroids
        for asteroid in asteroids[:]:
            asteroid.move()
            asteroid.draw()
            if asteroid.get_rect().colliderect(spaceship.get_rect()):
                draw_text(f"Game Over! Score: {score}", WIDTH // 2 - 120, HEIGHT // 2)
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False
            if asteroid.y > HEIGHT:
                asteroids.remove(asteroid)
                score += 10

        spaceship.draw()
        draw_text(f"Score: {score}", 10, 10)
        draw_text(f"Difficulty: {difficulty}", 10, 40)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
