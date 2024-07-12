from ticTacToeAI import return_best_move
from board import get_board
from board import do_process_board
from pywinauto import mouse
from board import determine_game
from chat import do_sign

import time
import pyautogui
import keyboard

# button coords
# 1 - 2 - 3 -
# 4 - 5 - 6 - 
# 7 - 8 - 9 - 

rounds = 0

button_coords = {
    (0, 0): (595, 542),
    (0, 1): (677, 542),
    (0, 2): (760, 542),
    (1, 0): (595, 629),
    (1, 1): (677, 629),
    (1, 2): (760, 629),
    (2, 0): (595, 709),
    (2, 1): (677, 709),
    (2, 2): (760, 709)
}
def detect_turn():
    past_boards = []

    while True:
        if determine_game():
            return False

        if keyboard.is_pressed('ctrl+shift+q'):  # Shortcut to stop the script
            print("Stopping script...")
            exit()

        past_boards.append(get_board())

        if do_process_board():
            print("-------------")

            if len(past_boards) >= 3:
                for row in past_boards[-3]:
                    print(row)
                return past_boards[-3]
            elif len(past_boards) == 2:
                for row in past_boards[-2]:
                    print(row)
                return past_boards[-2]
            else:
                for row in past_boards[-1]:
                    print(row)
                return past_boards[-1]
        
        time.sleep(0.04)

def do_choice(choice):
    if choice in button_coords:
        x, y = button_coords[choice]
        pyautogui.moveTo(x, y, duration=0.3)

        time.sleep(0.7)
        mouse.click(coords=(x, y))  


def play_game():
    board = detect_turn()
    if (board == False):
        return
    else:
        choice = return_best_move(board)
        do_choice(choice)


"""
while True:
    for row in get_board():
        print(row)
    print("------------------------")
    time.sleep(1)
"""

play_button_coords = (679, 709)
host_game_coords = (679, 553)
ttt_game_coords = (587, 345)
create_room_coords = (679,552)
robux_selection = (680, 451)
popup_coords = (821, 306)
sign_coords = (71, 415)
sign_text_coords = (183, 478)
hold_sign_coords = (236, 506)

rbx_coords = [
    (572, 417),
    (677, 417),
    (777, 417),
    (572, 503),
    (677, 503),
    (777, 503)
]


def click_button(coords):
    time.sleep(0.1)
    pyautogui.moveTo(coords[0], coords[1], duration=0.1)
    time.sleep(0.3)
    mouse.click(coords=(coords[0],coords[1]))

def queue_game(robux_amount):
    click_button(play_button_coords)
    click_button(host_game_coords)
    click_button(ttt_game_coords)
    click_button(rbx_coords[robux_amount])
    if (robux_amount == 0):
        click_button(create_room_coords)
    else:
        click_button(robux_selection)

def click_to_focus():
    click_button((500,500))

def close_popup():
    click_button(popup_coords)

def do_the_sign():
    click_button(sign_coords)
    click_button(sign_text_coords)
    do_sign()
    click_button(hold_sign_coords)
    click_to_focus()