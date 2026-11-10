
[app]

# p4a.branch = develop

# (string) Title of your application
title = Hello Justin

# (string) Package name
package.name = pgzerohellojustin

# (str) Icon of the application
icon.filename = favicon.ico

# (string) Package domain (needed for android packaging)
package.domain = org.justin

# (string) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,wav,mp3,ogg,ttf,otf,ico

# (string) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# KEY FIX: Standard pygame and pgzero included together 
requirements = hostpython3==3.11,python3==3.11,kivy



# (str) Supported orientations (valid options are: landscape, portrait, portrait-reverse, landscape-reverse)
orientation = portrait

# (list) Permissions
# Required if your game uses sound or reads local files
android.permissions = INTERNET, VIBRATE

# (int) Target Android API, should be as high as possible.
android.api = 33
android.minapi = 24
android.ndk = 25c



# (bool) Use architecture-specific builds (True reduces file size if building for one arch)
# For GitHub actions, keeping it False builds a universal APK that works on most phones
android.archs = arm64-v8a


# (list) The Android architectures for which to build
# (str) Android entry point, default is ok for Kivy/Pygame
android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to exclude from the long description
# android.meta_data =

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
