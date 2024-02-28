import pyautogui as py
import time

time.sleep(5)

for i in range(100):
    py.write(f"Hello message {i}")
    py.press("enter")
    time.sleep(1)


print("Done")
