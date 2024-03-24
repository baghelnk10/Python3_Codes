import os
import time

# Number of times to beep
total_beeps = 32

# Interval between beeps in seconds
interval = 15

for i in range(total_beeps):
    # Make the system emit a beep sound by calling a system command
    os.system(f'say "Lap {i+1}"')  # Use the 'say' command to produce a beep
    print("Beep", i+1, "of", total_beeps)
    if i < total_beeps - 1:
        time.sleep(interval)
