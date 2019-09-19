from pynput import keyboard
from game2048 import Game2048

game = Game2048(4)
game.start_game()


def on_press(key):
    try:
        if key.char == 'w' or key.char == 'W':
            game.up()
        elif key.char == 's' or key.char == 'S':
            game.down()
        elif key.char == 'a' or key.char == 'A':
            game.left()
        elif key.char == 'd' or key.char == 'D':
            game.right()
        elif key.char == 'r' or key.char == 'R':
            game.undo()
        elif key.char == 'p' or key.char == 'P':
            game.new_game()
        elif key.char == 'c' or key.char == 'C':
            game.check()
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
