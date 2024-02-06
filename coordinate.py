import subprocess
import re
import time

def get_mouse_coordinates():
    while True:
        # Get mouse position using xdotool
        result = subprocess.run(['xdotool', 'getmouselocation', '--shell'], capture_output=True, text=True)
        output = result.stdout

        # Extract x and y coordinates
        x_match = re.search(r'X:(\d+)', output)
        y_match = re.search(r'Y:(\d+)', output)

        if x_match and y_match:
            x = int(x_match.group(1))
            y = int(y_match.group(1))

            # Output coordinates
            print(f"Mouse coordinates: x={x}, y={y}")

        # Optional: Add a delay to control the refresh rate
        time.sleep(0.5)

if __name__ == "__main__":
    get_mouse_coordinates()
