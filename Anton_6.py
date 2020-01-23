import pyscreenshot as ImageGrab
import os
import time
import win32api
import win32con
from PIL import ImageOps
from numpy import *

"""
....just botting about, 'avin a bit o' sushi, innit?....
"""

# globals; for bounding box adjusting purposes.
x_pad = 10
y_pad = 112

# bouding box snapshot device, Arthur.
def screenGrab():
    b1 = (x_pad+0, y_pad+1, x_pad+639, y_pad+480)
    im = ImageGrab.grab(b1)
    #im.save(os.getcwd() + '//full_snap_' + str(int(time.time())) + '.jpg', 'JPEG')
    return im

# returns a b/w img (a) to the main program, is it not?
def grab():
    box = (x_pad+0, y_pad+1, x_pad+639, y_pad+480)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    #im.save(os.getcwd() + '//full_snap_' + str(int(time.time())) + '.jpg', 'JPEG')
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    return a

# me pointy-clickety-mechanism, innit?
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    #print('click detected.')

"""
for later use; when it's time to introduce the sake to customers 4, 5 and 6!

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    print('left down!')

def leftUp():
    win32api.mouse_event(win32con.MOUSEVENTF_LEFTUP, 0 ,0)
    time.sleep(0.1)
    print('left up!')
"""

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def getCords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print(x, y)

# me 'start the bloody game' function:
def startGame():
    mousePos((316, 205))
    time.sleep(0.5)
    leftClick()
    mousePos((322, 395))
    time.sleep(0.5)
    leftClick()
    mousePos((584, 451))
    time.sleep(0.5)
    leftClick()
    mousePos((319, 374))
    time.sleep(0.5)
    leftClick()

def continueGame():
    foodOnHand['rice'] = 10
    foodOnHand['nori'] = 10
    foodOnHand['roe'] = 10
    foodOnHand['salmon'] = 5
    foodOnHand['shrimp'] = 5
    foodOnHand['unagi'] = 5
    mousePos((323, 379))
    leftClick()
    time.sleep(1)
    main()

class Cord():
    """
    Hot Tip:
    Hunt the coordinates and pixel values that you need clicked upon
    screen running the 'getCords()', the 'im = screenGrab()' and the
    'im.getpixel()' cmds in the python shell.
    """
    # get the desktop pixel!
    desktop = (222, 222)

    # food location:
    f_shr = (35, 335)
    f_ric = (95, 335)
    f_nor = (35, 388)
    f_roe = (95, 382)
    f_sal = (35, 443)
    f_una = (95, 443)

    # plate location:
    pl_1 = (79, 208)
    pl_2 = (180, 208)
    pl_3 = (281, 209)
    pl_4 = (382, 208)
    pl_5 = (483, 208)
    pl_6 = (584, 208)

    # phone location:
    phone = (580, 360)

    # phone menu location:
    menu_toppings = (543, 272)
    menu_rice = (544, 294)
    #menu_sake = (545, 300)     #omitted for leisure purpouses (for now...).

    # shopping list location:
    p_shr = (495, 220)
    p_una = (572, 223)
    p_nor = (491, 276)
    p_roe = (575, 276)
    p_sal = (490, 329)
    p_exit_1 = (583, 335)
    p_exit_2 = (594, 335)
    buy_rice = (545, 278)
    delivery_norm = (491, 295)

def clear_tables():
    mousePos((79, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    mousePos((180, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    mousePos((281, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    mousePos((382, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    mousePos((483, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    mousePos((584, 208))
    leftClick()
    time.sleep(0.05)
    leftClick()
    time.sleep(1)

'''
Recipes:
------------------------------
onigiri
    2 rice, 1 nori
cali roll:
    1 rice, 1 nori, 1 roe
gunkan:
    1 rice, 1 nori, 2 roe
salmon roll:
    1 rice, 1 nori, 2 salmon
shrimp roll:
    1 rice, 1 nori, 2 shrimp
unagi roll:
    1 rice, 1 nori, 2 unagi
dragon roll:
    2 rice, 1 nori, 1 roe, 2 unagi
combo sushi:
    2 rice, 1 nori, 1 roe, 1 salmon, 1 shrimp, 2 unagi
'''

def foldMat():
    mousePos((Cord.f_ric[0] + 50, Cord.f_ric[1]))
    leftClick()
    time.sleep(0.1)

def makeFood(food):
    if food == 'onigiri':
        print('making an onigiri. You buy, you go!')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'caliroll':
        print('making a caliroll. Hey! No drink beer in here!')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'gunkan':
        print('making a gunkan. Hurry up and buy!')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 2
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'salmonroll':
        print('making a salmonroll. From the fresh fish this time, ok?!')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['salmon'] -= 2
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_sal)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_sal)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'shrimpsushi':
        print('making a shrimp sushi, ok..? Hurry up and buy!')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['shrimp'] -= 2
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_shr)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_shr)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'unagiroll':
        print('making an unagiroll, ok..? Hurry hurry!')
        foodOnHand['rice'] -= 1
        foodOnHand['nori'] -= 1
        foodOnHand['unagi'] -= 2
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_una)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_una)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'dragonroll':
        print('making an dragonroll. You! You eat too much!')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['unagi'] -= 2
        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_una)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_una)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

    if food == 'combosushi':
        print('making an combo sushi. Far far too much!')
        foodOnHand['rice'] -= 2
        foodOnHand['nori'] -= 1
        foodOnHand['roe'] -= 1
        foodOnHand['unagi'] -= 1
        foodOnHand['salmon'] -= 1
        foodOnHand['shrimp'] -= 1

        print(foodOnHand)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_ric)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_nor)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_roe)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_una)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_sal)
        leftClick()
        time.sleep(0.05)
        mousePos(Cord.f_shr)
        leftClick()
        time.sleep(0.05)
        foldMat()
        time.sleep(1)

##########################
#-------BUY SCRIPT-------#
##########################

def buyFood(food):
    if food == 'rice':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_rice)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            mousePos(Cord.buy_rice)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['rice'] += 10
        else:
            print('rice NOT available, ok? you... you go come back!!')
            mousePos(Cord.p_exit_1)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

    if food == 'nori':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.p_nor) != (33, 30, 11):
            print('nori is available.')
            mousePos(Cord.p_nor)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['nori'] += 10
        else:
            print('nori is NOT available, please come again!')
            mousePos(Cord.p_exit_2)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

    if food == 'roe':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.p_roe) != (127, 61, 0):
            print('roe is available.')
            mousePos(Cord.p_roe)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['roe'] += 10
        else:
            print('roe NOT available. Go away come back!')
            mousePos(Cord.p_exit_2)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

    if food == 'salmon':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.p_sal) != (127, 71, 47):
            print('salmon is available.')
            mousePos(Cord.p_sal)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['salmon'] += 5
        else:
            print('salmon NOT available. No put finger on display, just clean today!')
            mousePos(Cord.p_exit_2)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

    if food == 'shrimp':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.p_shr) != (127, 52, 6):
            print('shrimp is available.')
            mousePos(Cord.p_shr)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['shrimp'] += 5
        else:
            print('shrimp NOT available. You no get, go!')
            mousePos(Cord.p_exit_2)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

    if food == 'unagi':
        mousePos(Cord.phone)
        leftClick()
        time.sleep(0.1)
        mousePos(Cord.menu_toppings)
        leftClick()
        s = screenGrab()
        time.sleep(0.1)

        if s.getpixel(Cord.p_una) != (94, 49, 8):
            print('unagi is available.')
            mousePos(Cord.p_una)
            leftClick()
            time.sleep(0.1)
            mousePos(Cord.delivery_norm)
            leftClick()
            time.sleep(0.5)
            foodOnHand['unagi'] += 5
        else:
            print('unagi NOT available. You no get, go!')
            mousePos(Cord.p_exit_2)
            leftClick()
            time.sleep(1)
            clear_tables()
            buyFood(food)

# Initial Inventory:
foodOnHand = {'rice': 10,
              'nori': 10,
              'roe': 10,
              'shrimp': 5,
              'salmon': 5,
              'unagi': 5
              }

# Need to buy things, eh?
def checkFood():
    for i, j in foodOnHand.items():
        if i == 'nori' or i == 'rice' or i == 'roe' or i == 'salmon' or i == 'shrimp' or i == 'unagi':
            if j < 4:
                print('{0} is running low.'.format(i))
                buyFood(i)
                checkFood() # el cabron! rechecks for inconsistencies (abundant!)

def get_seat_one():
    box = (x_pad + 25, y_pad + 61, x_pad + 25 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_two():
    box = (x_pad + 126, y_pad + 61, x_pad + 126 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_three():
    box = (x_pad + 227, y_pad + 61, x_pad + 227 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_four():
    box = (x_pad + 328, y_pad + 61, x_pad + 328 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_five():
    box = (x_pad + 429, y_pad + 61, x_pad + 429 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_seat_six():
    box = (x_pad + 530, y_pad + 61, x_pad + 530 + 63, y_pad + 61 + 16)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    print(a)
    #im.save(os.getcwd() + '\\snaps\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a

def get_all_seats():
    get_seat_one()
    get_seat_two()
    get_seat_three()
    get_seat_four()
    get_seat_five()
    get_seat_six()

# getting the sum of an array of pixels within a small, grayscaled zone of the game area, well
# it may sound easy, Boris, but I tell ya' it's not, now pass us the milk ya f*ckin' weapon!
sushiTypes = {2677: 'gunkan',
              2670: 'onigiri',
              3143: 'caliroll',
              2474: 'salmonroll',
              2921: 'shrimpsushi',
              2893: 'unagiroll',
              3307: 'dragonroll',
              4159: 'combosushi'
              }

# empty seats: the sum of a grayscale array.
class Blank:
    seat_1 = 8119
    seat_2 = 5986
    seat_3 = 11353
    seat_4 = 10613
    seat_5 = 7286
    seat_6 = 9041

"""
The basic flow will follow this:
Check seats > if customer, make order > check food >
if low, buy food > clear tables > repeat.
"""

def check_bubs():
    checkFood()

    s1 = get_seat_one()
    if s1 != Blank.seat_1:
        if s1 in sushiTypes:
            print('table 1 is occupied and needs {}'.format(sushiTypes[s1]))
            makeFood(sushiTypes[s1])
        else:
            print('sushi not found: {}'.format(s1))
    else:
        print('table 1 unoccupied. No make money!')

    clear_tables()
    checkFood()

    s2 = get_seat_two()
    if s2 != Blank.seat_2:
        if s2 in sushiTypes:
            print('table 2 is occupied and needs {}'.format(sushiTypes[s2]))
            makeFood(sushiTypes[s2])
        else:
            print('sushi not found: {}'.format(s2))
    else:
        print('table 2 unoccupied. AIIII! I so bored!')

    checkFood()

    s3 = get_seat_three()
    if s3 != Blank.seat_3:
        if s3 in sushiTypes:
            print('table 3 is occupied and needs {}'.format(sushiTypes[s3]))
            makeFood(sushiTypes[s3])
        else:
            print('sushi not found: {}'.format(s3))
    else:
        print('table 3 unoccupied. You come, you buy!')

    clear_tables()
    checkFood()

    s4 = get_seat_four()
    if s4 != Blank.seat_4:
        if s4 in sushiTypes:
            print('table 4 is occupied and needs {}'.format(sushiTypes[s4]))
            makeFood(sushiTypes[s4])
        else:
            print('sushi not found: {}'.format(s4))
    else:
        print('table 4 unoccupied. No hurry, please.')

    checkFood()

    s5 = get_seat_five()
    if s5 != Blank.seat_5:
        if s5 in sushiTypes:
            print('table 5 is occupied and needs {}'.format(sushiTypes[s5]))
            makeFood(sushiTypes[s5])
        else:
            print('sushi not found: {}'.format(s5))
    else:
        print('table 5 unoccupied. Where customer?')

    clear_tables()
    checkFood()

    s6 = get_seat_six()
    if s6 != Blank.seat_6:
        if s6 in sushiTypes:
            print('table 6 is occupied and needs {}'.format(sushiTypes[s6]))
            makeFood(sushiTypes[s6])
        else:
            print('sushi not found: {}'.format(s6))
    else:
        print('table 6 unoccupied. Meh. Ey! Customer! You come back!')

def main():
    startGame()
    time_start = time.time()
    #makeFood('onigiri')
    #makeFood('caliroll')
    #makeFood('gunkan')

    while True:
        im = screenGrab()
        if (int(time.time()) - int(time_start)) >= 10 and im.getpixel(Cord.desktop) != (238, 219, 169):
            print('####################')
            print('#    round ends    #')
            print('####################')
            continueGame()
        else:
            check_bubs()
##          if thisKey.isDown(KEY_ESC):
##              break

"""
if __name__ == '__main__':
    main()
"""
