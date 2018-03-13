"""
file: config.py
This file holds configuration options common to gamev1 and botv1
"""

import tkinter as tk

# CONFIGURATION OPTIONS RELATED TO GAME_V1
# DISPLAY OPTIONS
SQUARE_SIZE = 10
WIDTH = 60      # in square
HEIGHT = 60     # in square
MARGE = 2       # affects the way gems are displayed

# GAME OPTIONS
NBR_GEMS = 100              # number of gems to set on the board for every generation
NBR_BOT = 20                # number of bots per generation
DEFAULT_SPEED = 0          # default speed of time
MAX_STRENGTH = 80           # maximum strength of a bot
NB_SELECT_BOT = 10
NB_TURN_GENERATION = 300     # number of turns to pass after a new generation is created
                            # (used when auto_gen is ON)
MUTATION = 1		# put to 1 to activate mutation
