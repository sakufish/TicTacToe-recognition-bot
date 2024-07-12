import mss
import numpy as np
import cv2
import time
    
def capture_screen(region):
    with mss.mss() as sct:
        screenshot = sct.grab(region)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
        return img
    
def detect_x(cell_img):
    lower_blue = np.array([95, 195, 95], dtype=np.uint8)  # Convert RGB to BGR # decreased by 5
    upper_blue = np.array([255, 255, 155], dtype=np.uint8)  # Convert RGB to BGR # increased by 5 right one only
    mask = cv2.inRange(cell_img, lower_blue, upper_blue)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 50
    return nonzero_pixels > threshold

"""
def detect_o(cell_img):
    lower_red = np.array([150, 90, 150], dtype=np.uint8)
    upper_red = np.array([255, 180, 255], dtype=np.uint8) 
    mask = cv2.inRange(cell_img, lower_red, upper_red)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 50
    return nonzero_pixels > threshold
"""
def detect_o(cell_img):
    lower_red = np.array([152, 151, 255], dtype=np.uint8)  # Lower bound: close to RGB(255,156,157) # decrease left 2 by 5
    upper_red = np.array([166, 165, 255], dtype=np.uint8)  # Upper bound: close to RGB(255,160,161) # increase left 2 by 5
    mask = cv2.inRange(cell_img, lower_red, upper_red)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 50
    return nonzero_pixels > threshold

def process_board(image, region):

    cell_size = region["width"] // 3
    board = [["" for _ in range(3)] for _ in range(3)]
    
    for i in range(3):
        for j in range(3):
            cell_img = image[i * cell_size:(i + 1) * cell_size, j * cell_size:(j + 1) * cell_size]
            if detect_o(cell_img):
                board[i][j] = 'O'
            elif detect_x(cell_img):
                board[i][j] = 'X'
            else:
                board[i][j] = ' '

    return board

time.sleep(1)

screen_region = {
    "top": 0,          # Top-left corner
    "left": 0,
    "width": 1360,     # Width of the region
    "height": 768      # Height of the region
}

board_region = {
    "top": 337,
    "left": 557,
    "width": 808 - 557,
    "height": 589 - 337
}

region_of_interest = {
    "top": 332,
    "left": 622,
    "width": 726 - 622,
    "height": 357 - 332
}

board_cnc4_region = {
    "left": 492,
    "top": 256,
    "width": 384,
    "height": 332
}

def get_board():
    img = capture_screen(board_region)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return process_board(img, board_region)

def detect_blue(cell_img):

    lower_blue_1 = np.array([195, 136, 59], dtype=np.uint8)
    upper_blue_1 = np.array([201, 141, 64], dtype=np.uint8)

    lower_blue_2 = np.array([119, 95, 64], dtype=np.uint8)
    upper_blue_2 = np.array([120, 106, 69], dtype=np.uint8)

    mask1 = cv2.inRange(cell_img, lower_blue_1, upper_blue_1)
    mask2 = cv2.inRange(cell_img, lower_blue_2, upper_blue_2)

    combined_mask = cv2.bitwise_or(mask1, mask2)
    nonzero_pixels = cv2.countNonZero(combined_mask)

    threshold = 50

    return nonzero_pixels > threshold

def wow_process_board(image, region):
    
    condition = True 
    cell_size = region["width"] // 3

    for j in range(3):
        cell_img = image[2 * cell_size:(3) * cell_size, j * cell_size:(j + 1) * cell_size]
        if detect_blue(cell_img) == False:
            condition = False

    return condition

def do_process_board():
    img = capture_screen(board_region)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return wow_process_board(img,board_region)

def detect_pink_pixels(cell_img):
    
    lower_pink = np.array([113, 70, 142], dtype=np.uint8)  # Lower bound: darker pink (BGR) (decreased by 6 )
    upper_pink = np.array([228, 209, 237], dtype=np.uint8)  # Upper bound: lighter pink (BGR)
    mask = cv2.inRange(cell_img, lower_pink, upper_pink)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 1860
    return nonzero_pixels > threshold

def determine_game():
    img = capture_screen(region_of_interest)
    return detect_pink_pixels(img)

def detect_black():
    cell_img = capture_screen(screen_region)
    lower_black = np.array([0, 0, 0], dtype=np.uint8)  # Lower bound: darker black (BGR) (decreased by 6 )
    upper_black = np.array([5, 5, 5], dtype=np.uint8)  # Upper bound: lighter black (BGR)
    mask = cv2.inRange(cell_img, lower_black, upper_black)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 750000
    return nonzero_pixels > threshold

def detect_cnc4_blue(cell_img):
    lower_blue = np.array([95, 195, 95], dtype=np.uint8)  # Convert RGB to BGR # decreased by 5
    upper_blue = np.array([255, 255, 155], dtype=np.uint8)  # Convert RGB to BGR # increased by 5 right one only
    mask = cv2.inRange(cell_img, lower_blue, upper_blue)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 100

    return nonzero_pixels > threshold

def detect_cnc4_red(cell_img):
    lower_red = np.array([152, 151, 255], dtype=np.uint8)  # Lower bound: close to RGB(255,156,157) # decrease left 2 by 5
    upper_red = np.array([166, 165, 255], dtype=np.uint8)  # Upper bound: close to RGB(255,160,161) # increase left 2 by 5
    mask = cv2.inRange(cell_img, lower_red, upper_red)
    nonzero_pixels = cv2.countNonZero(mask)
    threshold = 100
    return nonzero_pixels > threshold

def process_cnc4_board(image, region):
    rows = 6
    cols = 7
    cell_width = region["width"] // cols
    cell_height = region["height"] // rows
    board = [["" for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            cell_img = image[i * cell_height:(i + 1) * cell_height, j * cell_width:(j + 1) * cell_width]
            cv2.imshow(f"Cell {i}, {j}", cell_img)
            cv2.waitKey(0)  # Wait for a key press to move to the next cell image
            if detect_cnc4_blue(cell_img):
                board[i][j] = 'X'
            elif detect_cnc4_red(cell_img):
                board[i][j] = 'O'
            else:
                board[i][j] = ' '
            cv2.destroyAllWindows()


    return board

def get_cnc4_board():
    img = capture_screen(board_cnc4_region)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)
    return process_cnc4_board(img, board_region)