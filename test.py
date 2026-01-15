import pygame
import sys
import random

# test.py - simple Snake game using pygame
# Run: pip install pygame
# Then: python test.py


# Config
CELL_SIZE = 20
GRID_W = 30
GRID_H = 20
WIDTH = CELL_SIZE * GRID_W
HEIGHT = CELL_SIZE * GRID_H
FPS_BASE = 8
FPS_INC_EVERY = 5  # increase speed every N points
BG_COLOR = (18, 18, 18)
SNAKE_COLOR = (0, 200, 0)
FOOD_COLOR = (200, 50, 50)
GRID_COLOR = (30, 30, 30)
TEXT_COLOR = (200, 200, 200)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def random_food_pos(snake):
    while True:
        pos = (random.randrange(GRID_W), random.randrange(GRID_H))
        if pos not in snake:
            return pos

def draw_grid(surface):
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y))

def draw_rect(surface, pos, color):
    r = pygame.Rect(pos[0]*CELL_SIZE, pos[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)
    pygame.draw.rect(surface, color, r)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)
    big_font = pygame.font.SysFont(None, 48)

    def reset():
        start_x = GRID_W // 2
        start_y = GRID_H // 2
        snake = [(start_x, start_y), (start_x-1, start_y), (start_x-2, start_y)]
        direction = RIGHT
        food = random_food_pos(snake)
        score = 0
        return snake, direction, food, score

    snake, direction, food, score = reset()
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_w, pygame.K_UP):
                    if direction != DOWN:
                        direction = UP
                elif event.key in (pygame.K_s, pygame.K_DOWN):
                    if direction != UP:
                        direction = DOWN
                elif event.key in (pygame.K_a, pygame.K_LEFT):
                    if direction != RIGHT:
                        direction = LEFT
                elif event.key in (pygame.K_d, pygame.K_RIGHT):
                    if direction != LEFT:
                        direction = RIGHT
                elif event.key == pygame.K_r and game_over:
                    snake, direction, food, score = reset()
                    game_over = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        if not game_over:
            # Move snake
            head = snake[0]
            new_head = ((head[0] + direction[0]) % GRID_W, (head[1] + direction[1]) % GRID_H)
            # Check collision with self
            if new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 1
                    food = random_food_pos(snake)
                else:
                    snake.pop()

        # Draw
        screen.fill(BG_COLOR)
        draw_grid(screen)
        # Draw food
        draw_rect(screen, food, FOOD_COLOR)
        # Draw snake
        for i, p in enumerate(snake):
            # slightly different shade for head
            c = (255, 220, 0) if i == 0 else SNAKE_COLOR
            draw_rect(screen, p, c)

        score_surf = font.render(f"Score: {score}", True, TEXT_COLOR)
        screen.blit(score_surf, (8, 8))

        if game_over:
            over_surf = big_font.render("GAME OVER", True, (220, 60, 60))
            over_rect = over_surf.get_rect(center=(WIDTH//2, HEIGHT//2 - 20))
            screen.blit(over_surf, over_rect)
            instr_surf = font.render("Press R to restart or Q to quit", True, TEXT_COLOR)
            instr_rect = instr_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
            screen.blit(instr_surf, instr_rect)

        pygame.display.flip()

        # Adjust FPS by score for difficulty
        fps = FPS_BASE + (score // FPS_INC_EVERY)
        clock.tick(fps)

if __name__ == "__main__":
    main()