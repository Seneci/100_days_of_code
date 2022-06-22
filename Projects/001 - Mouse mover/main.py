# This Python script will use the PyAutoGUI library in order to control the mouse: pip install PyAutoGUI
# You can use the following link to uninstall a python library:
# https://servicedesk.mtu.edu/TDClient/1801/Portal/KB/ArticleDet?ID=66715

##############################
#Terminate pressing Ctrl + F2#
##############################

import pyautogui

def print_screensize():
    try:
        while True:
            pyautogui.moveTo(300, 200, 1)
            pyautogui.moveTo(310, 210, 1)
            pyautogui.moveTo(290, 210, 1)
            pyautogui.moveTo(300, 200, 1)

    except:
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_screensize()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
