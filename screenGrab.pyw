import pyscreenshot as ImageGrab
import os
import time

"""
....
"""

# globals
x_pad = 73
y_pad = 100
#x_pad = 365
#y_pad = 179

def screenGrab():
    box = (x_pad+0, y_pad+1, x_pad+639, y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '/full_snap_' + str(int(time.time())) + '.jpg', 'JPEG')

def main():
    screenGrab()
if __name__ == '__main__':
    main()
