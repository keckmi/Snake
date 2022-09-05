import pygame
import time
import random


def gitter_erstellen():
    global fields
    block = 20
    i = 0
    # Höhe
    for x in range(0, 1000, block):
        # Breite
        for y in range(0, 800, block):
            rect = pygame.Rect(x, y, block, block)
            pygame.draw.rect(SCREEN, (0, 0, 0), rect, 1)
            fields[i] = (x, y)
            i += 1


def generate_snake(pos, empty):
    block = 20
    for snake_block in pos:
        rect = pygame.Rect(snake_block[0], snake_block[1], block, block)
        pygame.draw.rect(SCREEN, (0, 0, 0), rect)
    if empty:
        empty_rect = pygame.Rect(empty[0] + 1, empty[1] + 1, block - 2, block - 2)
        pygame.draw.rect(SCREEN, (200, 200, 200), empty_rect)


def spawn_food():
    global fields
    global food
    block = 20
    field = random.randint(0, len(fields))
    food_rect = pygame.Rect(fields[field][0] + 1, fields[field][1] + 1, block - 2, block - 2)
    pygame.draw.rect(SCREEN, (0, 255, 0), food_rect)
    food.append(fields[field])


def delete_food():
    global food
    block = 20
    old_food = food.pop(0)
    food_rect = pygame.Rect(old_food[0] + 1, old_food[1] + 1, block - 2, block - 2)
    pygame.draw.rect(SCREEN, (200, 200, 200), food_rect)


background_colour = (200, 200, 200)
SCREEN = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('Snake')
SCREEN.fill(background_colour)

pygame.display.flip()

running = True
pos = [(460, 300), (480, 300), (500, 300)]
direction = "right"
fields = {}
gitter_erstellen()
counter = 0
food = []
sleeping_time = 1

while running:
    if len(food) < 10:
        if counter % 3 == 0:
            spawn_food()
    if counter % 7 == 0 and food:
        delete_food()
    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction == "right":
                    continue
                else:
                    direction = "left"
            if event.key == pygame.K_RIGHT:
                if direction == "left":
                    continue
                else:
                    direction = "right"
            if event.key == pygame.K_UP:
                if direction == "down":
                    continue
                else:
                    direction = "up"
            if event.key == pygame.K_DOWN:
                if direction == "up":
                    continue
                else:
                    direction = "down"

        if event.type == pygame.QUIT:
            running = False

    if direction == "right":
        current_pos = (pos[-1][0] + 20, pos[-1][1])
        if current_pos in pos:
            running = False
        else:
            pos.append(current_pos)
    elif direction == "up":
        current_pos = (pos[-1][0], pos[-1][1] - 20)
        if current_pos in pos:
            running = False
        else:
            pos.append(current_pos)
    elif direction == "down":
        current_pos = (pos[-1][0], pos[-1][1] + 20)
        if current_pos in pos:
            running = False
        else:
            pos.append(current_pos)
    elif direction == "left":
        current_pos = (pos[-1][0] - 20, pos[-1][1])
        if current_pos in pos:
            running = False
        else:
            pos.append(current_pos)

    if pos[-1] in food:
        sleeping_time *= 0.95
    else:
        empty = pos.pop(0)

    if 1000 <= pos[-1][0] or pos[-1][0] <= 0 or 800 <= pos[-1][1] or pos[-1][1] <= 0:
        running = False
    generate_snake(pos, empty)
    time.sleep(sleeping_time)

    counter += 1
    pygame.display.flip()
