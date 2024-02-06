from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse clicked at (x={x}, y={y})")

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
