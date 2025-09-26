import pyautogui
import time
 
def keep_awake(interval=30):
    print("Mouse jiggler started. Press Ctrl+C to stop.")
    try:
        while True:
            pyautogui.moveRel(5, 0, duration=0.2)   # move right
            pyautogui.moveRel(-5, 0, duration=0.2)  # move left
            time.sleep(interval)  # wait before next jiggle
    except KeyboardInterrupt:
        print("\nMouse jiggler stopped.")
 
if __name__ == "__main__":
    keep_awake()
