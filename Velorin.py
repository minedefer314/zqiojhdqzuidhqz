import pyautogui
import time
import keyboard
import win32gui
import numpy as np



def get_active_window_size():
    hwnd = win32gui.GetForegroundWindow()
    if hwnd == 0:
        print('No active window detected.')
        return (None, None)

    rect = win32gui.GetWindowRect(hwnd)
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    return (width, height)

def pixel_search(color, region, tolerance=20, stride=3):
    screenshot = pyautogui.screenshot(region=region)
    img_array = np.array(screenshot)
    for y in range(0, img_array.shape[0], stride):
        for x in range(0, img_array.shape[1], stride):
            pixel = img_array[y, x, :3]
            if np.all(np.abs(pixel - color) <= tolerance):
                return True
    return False

def get_mouse_color():
    x, y = pyautogui.position()
    screenshot = pyautogui.screenshot()
    return screenshot.getpixel((x, y))

def main():
    color_to_find = None
    region = None
    while True:
        if keyboard.is_pressed('ctrl'):
            color_to_find = get_mouse_color()
            win_width, win_height = get_active_window_size()
            mid_x = win_width // 2
            mid_y = win_height // 2
            region = (mid_x-5, mid_y-5, 10, 10)

        elif keyboard.is_pressed('e') and region is not None and pixel_search(color_to_find, region):
            pyautogui.click()
            time.sleep(0.4)
        elif keyboard.is_pressed('f2'):
            break
        else:
            time.sleep(0.01)
if __name__ == '__main__':
    main()