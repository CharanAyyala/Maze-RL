import pygame
import time
import random
import numpy as np

# Maze Layout
maze = [
    ["S", ".", "#", ".", ".", ".", "#", ".", "G"],
    [".", "#", ".", "#", "#", ".", "#", ".", "#"],
    [".", ".", ".", "#", ".", ".", ".", ".", "."],
    ["#", ".", "#", "#", ".", "#", "#", ".", "#"],
    [".", ".", ".", ".", ".", ".", "#", ".", "."],
    [".", "#", "#", "#", "#", ".", "#", "#", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."]
]

# Initialize Pygame
pygame.init()
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Reinforcement Learning Maze")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Cell size
CELL_SIZE = 60
player_pos = [0, 0]
attempts = []
current_attempt = []
ai_mode = False

# Move directions
directions = {
    pygame.K_UP: (-1, 0),
    pygame.K_DOWN: (1, 0),
    pygame.K_LEFT: (0, -1),
    pygame.K_RIGHT: (0, 1)
}

def draw_maze():
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            color = WHITE if cell == "." else BLACK if cell == "#" else RED if cell == "G" else GREEN
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (player_pos[1] * CELL_SIZE, player_pos[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def move_player(dx, dy):
    global player_pos, current_attempt
    x, y = player_pos
    new_x, new_y = x + dx, y + dy
    if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] != "#":
        player_pos = [new_x, new_y]
        current_attempt.append(tuple(player_pos))
        if maze[new_x][new_y] == "G":
            attempts.append(current_attempt[:])
            current_attempt.clear()
            reset_player()

def reset_player():
    global player_pos
    player_pos = [0, 0]

def ai_play():
    if len(attempts) >= 2:
        for step in attempts[0]:
            time.sleep(0.5)
            pygame.event.pump()
            player_pos[0], player_pos[1] = step
            draw_maze()
            pygame.display.flip()

def main():
    global ai_mode
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(WHITE)
        draw_maze()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in directions:
                    move_player(*directions[event.key])
                elif event.key == pygame.K_SPACE:
                    ai_play()
        clock.tick(10)
    pygame.quit()

main()
