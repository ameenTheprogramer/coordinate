import subprocess
import re

def get_mouse_click_coordinates():
    while True:
        # Get mouse click event using xev
        result = subprocess.run(['xev', '-event', 'button_press'], capture_output=True, text=True)

        # Extract x and y coordinates from the output
        match = re.search(r'x:\s*(\d+)\s*y:\s*(\d+)', result.stdout)
        
        if match:
            x = int(match.group(1))
            y = int(match.group(2))
            
            # Print the coordinates
            print(f"Mouse clicked at: x={x}, y={y}")

if __name__ == "__main__":
    get_mouse_click_coordinates()
