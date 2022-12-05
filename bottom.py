import os
import time
import sys
import threading

cols, lines = os.get_terminal_size()

# Save the positionat the bottom of the page
sys.stdout.write("\n")

# Move cursor to bottom left, second last line
sys.stdout.write(f"\033[0;{lines-1}r")

# Return cursor to top
sys.stdout.write("\0338")

# flush buffer
sys.stdout.flush()


def set_bottom(text: str):
    # Return cursor to area it was saved above
    sys.stdout.write("\0337")
    
    # Go to the far left
    sys.stdout.write(f"\033[{lines};0f")

    # write the text
    sys.stdout.write(text)

    # Save the cursor area
    sys.stdout.write("\0338")
    sys.stdout.write("\n")
     
    # go up one line
    sys.stdout.write("\033[1A")
    sys.stdout.flush()
