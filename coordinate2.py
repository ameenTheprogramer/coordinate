import subprocess
import re

def get_mouse_click_coordinates():
    # Start the xev process
    xev_process = subprocess.Popen(['xev'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

    # Pattern to match mouse click events
    click_pattern = re.compile(r"ButtonPress event,.*button (\d+),.*root:.*\[(\d+),(\d+)\]")

    # Process xev output line by line
    for line in iter(xev_process.stdout.readline, ''):
        match = click_pattern.search(line)
        if match:
            button = match.group(1)
            x = match.group(2)
            y = match.group(3)
            print(f"Mouse clicked at: x={x}, y={y} (Button {button})")

if __name__ == "__main__":
    get_mouse_click_coordinates()
