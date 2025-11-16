import cv2
import numpy as np
import mss
import pyautogui
import time

# Disable the pyautogui fail-safe to avoid unwanted exceptions when the cursor
# reaches a corner during rapid movements.
pyautogui.FAILSAFE = False

def get_mouse_position():
    return pyautogui.position()

def capture_screen(region=None):
    with mss.mss() as sct:
        screenshot = sct.grab(region) if region else sct.grab(sct.monitors[1])
        return np.array(screenshot)

def main():
    print("Press 'CTRL c' to quit.")
    
    while True:
        # Capture the screen
        screen = capture_screen()
        
        # Get mouse position
        mouse_x, mouse_y = get_mouse_position()
        
        # Check if mouse is within the screen boundaries
        if (0 <= mouse_x < screen.shape[1]) and (0 <= mouse_y < screen.shape[0]):
            # Display the coordinate of the pixel under the mouse
            pixel_color = screen[mouse_y, mouse_x]
            color_bgr = (int(pixel_color[0]), int(pixel_color[1]), int(pixel_color[2]))
            print(f"Mouse Position: ({mouse_x}, {mouse_y}) - Color (BGR): {color_bgr}", end='\r')

        # Slow the loop slightly so macOS accessibility services keep up
        time.sleep(0.01)
        
        # Display the screen
        #cv2.imshow("Screen", screen)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
