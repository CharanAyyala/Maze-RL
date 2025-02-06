import pygame

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

# Constants
TILE_SIZE = 50
WIDTH, HEIGHT = len(maze[0]) * TILE_SIZE, len(maze) * TILE_SIZE
PLAYER_COLOR = (0, 255, 0)
WALL_COLOR = (50, 50, 50)
GOAL_COLOR = (255, 215, 0)
BACKGROUND_COLOR = (200, 200, 200)

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RL Maze Game")

# Player Position
player_pos = [0, 0]


def draw_maze():
    screen.fill(BACKGROUND_COLOR)
    for row in range(len(maze)):
        for col in range(len(maze[row])):
            x, y = col * TILE_SIZE, row * TILE_SIZE
            if maze[row][col] == "#":
                pygame.draw.rect(screen, WALL_COLOR, (x, y, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == "G":
                pygame.draw.rect(screen, GOAL_COLOR, (x, y, TILE_SIZE, TILE_SIZE))

    # Draw Player
    px, py = player_pos[1] * TILE_SIZE, player_pos[0] * TILE_SIZE
    pygame.draw.rect(screen, PLAYER_COLOR, (px, py, TILE_SIZE, TILE_SIZE))
    pygame.display.flip()


running = True
while running:
    draw_maze()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            dx, dy = 0, 0
            if event.key == pygame.K_UP:
                dx, dy = -1, 0
            elif event.key == pygame.K_DOWN:
                dx, dy = 1, 0
            elif event.key == pygame.K_LEFT:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT:
                dx, dy = 0, 1

            new_x = max(0, min(player_pos[0] + dx, len(maze) - 1))
            new_y = max(0, min(player_pos[1] + dy, len(maze[0]) - 1))

            if maze[new_x][new_y] != "#":
                player_pos = [new_x, new_y]

            if maze[new_x][new_y] == "G":
                print("You reached the goal! 🎉")
                running = False

pygame.quit()
