import os
import pygame
import pgzrun

# --- Required for Pygame Zero ---
WIDTH = 800
HEIGHT = 600

# Global variables
fullscreen_set = False
current_fps = 60.0  # Start near 60 so smoothing ramps cleanly
fps_timer = 0.0
fps_display_text = "FPS: 60"


# =================================================================================================================
# My Pygame ZERO code
# =================================================================================================================
def draw():
    screen.clear()

    # Draw main welcome text
    screen.draw.text("Welcome to Pygame Zero", (10, 100), fontname="lemon days", fontsize=60, color=(255, 215, 0))
    screen.draw.text("Justin!", (300, 180), fontname="skincake", fontsize=60, color=(255, 0, 0))

    # Draw the smoothed FPS counter
    screen.draw.text(fps_display_text, topleft=(10, 10), fontsize=65, color=((0,0,205)))


# =================================================================================================================
# Standard Code to get FULL Screen on both Android and Windows
# =================================================================================================================

def set_android_immersive():
    """Allows SDL2/Pygame to hide screen system bars on Android."""
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


def update(dt):
    global fullscreen_set, current_fps, fps_timer, fps_display_text

    # 1. Set fullscreen on Windows and Android once on the first frame
    if not fullscreen_set:
        screen.surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN | pygame.SCALED)
        set_android_immersive()
        fullscreen_set = True

    # 2. Calculate and smooth FPS
    if dt > 0:
        instant_fps = 1.0 / dt
        current_fps = (current_fps * 0.9) + (instant_fps * 0.1)

    # 3. Update the display string 4 times per second
    fps_timer += dt
    if fps_timer > 0.25:
        fps_display_text = f"FPS: {round(current_fps)}"
        fps_timer = 0.0

#
#=====================================================================================================================
#
# --- Standard Native Pygame Zero Execution ---
pgzrun.go()


