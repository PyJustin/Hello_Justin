import pgzrun   # <--- Pygame Zero
import os
import pygame   # using pygame for its FULLSCREEN Function (in UPDATE below)

fullscreen_set = False # this is used in the UPATE Functiom.

# --- Required for Pygame Zero ---
WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    screen.draw.text("Welcome to Pygame Zero", (10, 100), fontname="lemon days", fontsize=60, color=(255,215,0))
    screen.draw.text("Justin!", (300, 180), fontname="skincake", fontsize=60, color=(255,0,0))


# code to get Full Screen when running on Windows - not applicable on Androiid as that is set in Buildozer.spec file
def update():  # Pygame Zero requires an Update Function even if it just contains 'pass'
    global fullscreen_set
    if not fullscreen_set and 'ANDROID_ARGUMENT' not in os.environ:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        fullscreen_set = True


# --- Standard Native Execution ---
pgzrun.go()


