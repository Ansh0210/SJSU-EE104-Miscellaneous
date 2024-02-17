import pygame
import random
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Object Identification Game")

# Colors
white = (255, 255, 255)

# Fonts
font = pygame.font.SysFont(None, 48)

# Fruits
fruits = ['apple', 'banana']

# Load fruit images
fruit_images = {}
for fruit in fruits:
    try:
        fruit_images[fruit] = pygame.image.load(f'{fruit}.png')
    except pygame.error as e:
        print(f"Error loading image for {fruit}: {e}")
        pygame.quit()
        exit()

# Function to display a correct and a false fruit
def display_fruits():
    screen.fill(white)

    # Randomly select a correct fruit
    correct_fruit = random.choice(fruits)

    # Randomly select a false fruit (different from the correct fruit)
    false_fruit = random.choice([f for f in fruits if f != correct_fruit])

    # Display the correct and false fruits at fixed positions
    correct_position = (100, 200)
    false_position = (500, 200)

    screen.blit(fruit_images[correct_fruit], correct_position)
    screen.blit(fruit_images[false_fruit], false_position)

    # Speak the name of the correct fruit using os.system
    os.system(f'say "Click on the {correct_fruit}"')

    pygame.display.flip()

    return correct_fruit

# Main game loop
def game_loop():
    running = True

    correct_fruit = display_fruits()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                # Check if the click is within the area of the correct fruit
                correct_position = (100, 200, 100, 100)  # (x, y, width, height)
                correct_rect = pygame.Rect(correct_position)
                if correct_rect.collidepoint(x, y):
                    os.system(f'say "Correct! Well done! This is {correct_fruit}"')
                else:
                    os.system("say 'Oops! Try again.'")

                correct_fruit = display_fruits()

        pygame.display.update()

# Start the game
game_loop()

# Quit Pygame
pygame.quit()
