import pyautogui
import time
import math
import operator
from functools import reduce

pyautogui.FAILSAFE = True
init_x, init_y = 173, 269
space = 50
number = 5
interval = 2
region = (init_x, init_y, 200, space)

pyautogui.alert(text='start OK?', title='start game', button='OK')

# TEST START
for i in range(0, number):
    pyautogui.moveTo(init_x, init_y + i * space)
    time.sleep(1)
# TEST END

def imageChange(region):
    im1 = pyautogui.screenshot(region=region)
    histogram1 = im1.histogram()
    time.sleep(2)
    im2 = pyautogui.screenshot(region=region)
    histogram2 = im2.histogram()
    differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))
    print(differ)
    if differ < 20:
        print("image no change!")
        return False
    else:
        print("image change")
        time.sleep(interval)
        return True


while True:
    print("start")
    pyautogui.moveTo(init_x, init_y, duration=1)
    pyautogui.scroll(100 * space)
    time.sleep(1)
    pyautogui.click()
    print("0")
    while True:
        if imageChange((region[0], region[1] + 2 * space, region[2] + 250, region[3])) is False:
            break

    for i in range(1, number):
        pyautogui.click(init_x, init_y + i * space)
        print(i)
        while True:
            if imageChange((region[0], region[1] + 2 * space, region[2] + 250, region[3])) is False:
                break

        if i == (number - 1):
            while True:
                # get old pic
                im1 = pyautogui.screenshot(region=region)
                histogram1 = im1.histogram()
                x, y = pyautogui.position()
                pyautogui.dragTo(x, y - space, 1, button='left')
                pyautogui.moveTo(x, y, duration=1)
                time.sleep(1)
                # get new pic, compare
                im2 = pyautogui.screenshot(region=region)
                histogram2 = im2.histogram()
                differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a-b)**2, histogram1, histogram2)))/len(histogram1))
                print(differ)

                if differ < 50:
                    print("match")
                    break
                else:
                    print("not match")
                    pyautogui.click()
                    while True:
                        if imageChange((region[0], region[1] + 2 * space, region[2] + 250, region[3])) is False:
                            break
