# Website to execute the code is reeborg.ca
# Credits to github reeborg_en.py

# Important: Multiline docstrings should have their text start
# on the second line. This results in nicer formatting when
# using help().

# When generating documentation using sphinx, these modules are both
# unavailable and not needed
try:
    from browser import window
    RUR = window.RUR
except ImportError:
    from collections import defaultdict
    window = defaultdict(str)
    print("\n --> Skipping importing from browser for sphinx.\n")


def turn_left():  #py:turn_left
    """Reeborg turns to its left."""
    RUR._turn_left_()


def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move(self):  #py:UR.move
        """Move forward, by one grid position."""
        RUR._UR.move_(self.body)

# hurdle
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

for step in range(6):
     jump()