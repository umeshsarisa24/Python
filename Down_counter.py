import time
import sys

def countdown_with_animation(seconds):
    animation = "|/-\\"
    for remaining in range(seconds, 0, -1):
        for frame in animation:
            sys.stdout.write(f"\r{remaining} seconds remaining... {frame}")
            sys.stdout.flush()
            time.sleep(0.25)  # Animation speed

    print("\rCountdown complete!            ")

# Input countdown time in seconds
countdown_time = int(input("Enter countdown time in seconds: "))
countdown_with_animation(countdown_time)
