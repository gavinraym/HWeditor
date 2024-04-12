import os
import sys

INPUT_PATH = "input"
OUTPUT_PATH = "output"

if getattr(sys, 'frozen', False):
    # If the app is running in a PyInstaller bundle
    INPUT_PATH = os.path.join("..", "input")
    OUTPUT_PATH = os.path.join("..", "output")



