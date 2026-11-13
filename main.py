import os
import pygame
import pgzrun  # <--- Pygame Zero

fullscreen_set = False  # Used in the update() function

# --- Required for Pygame Zero ---
WIDTH = 800
HEIGHT = 600


def draw():
    screen.clear()
    screen.draw.text("Welcome to Pygame Zero", (10, 100), fontname="lemon days", fontsize=60, color=(255, 215, 0))
    screen.draw.text("Justin!", (300, 180), fontname="skincake", fontsize=60, color=(255, 0, 0))


# =================================================================================================================
# the following code is to het FULL SCREEN on both Android and Windows.
# =================================================================================================================

def update():
    global fullscreen_set
    if not fullscreen_set:
        # Apply FULLSCREEN | SCALED on both Windows and Android (SDL2)
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        set_android_immersive()
        fullscreen_set = True


def set_android_immersive():
    # Allows SDL2/Pygame to hide screen system bars."""
    if 'ANDROID_ARGUMENT' in os.environ:
        try:
            from jnius import autoclass
            from android.runnable import run_on_ui_thread

            @run_on_ui_thread
            def _apply_flags():
                PythonActivity = autoclass('org.kivy.android.PythonActivity')
                View = autoclass('android.view.View')
                WindowManager = autoclass('android.view.WindowManager$LayoutParams')

                activity = PythonActivity.mActivity
                window = activity.getWindow()

                # Extend into the front camera notch/cutout area (API 28+)
                params = window.getAttributes()
                params.layoutInDisplayCutoutMode = WindowManager.LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES
                window.setAttributes(params)

                # Enforce immersive sticky mode
                decor_view = window.getDecorView()
                flags = (
                    View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                    | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                    | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                    | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                    | View.SYSTEM_UI_FLAG_FULLSCREEN
                    | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY
                )
                decor_view.setSystemUiVisibility(flags)

            _apply_flags()
        except Exception as e:
            print("Immersive mode setup skipped:", e)




# --- Standard Native Pygame Zero Execution ---
pgzrun.go()




