from playGame import play_game
from board import detect_black
from board import determine_game
from chat import do_message
from playGame import queue_game
from move import hold_keys
from playGame import click_to_focus
from chat import do_pre_message
from chat import do_join
from playGame import do_the_sign
from chat import do_midgame_message
    
import time
import random

first_loop = True   
queued = False
robux_amount = 2    

MIN_INTERVAL_SECONDS = 50  # Minimum interval (1 minutes)w
MAX_INTERVAL_SECONDS = 120  # Maximum interval (2  minutes)

MIN_INTERVAL_ITERATIONS = MIN_INTERVAL_SECONDS * 10
MAX_INTERVAL_ITERATIONS = MAX_INTERVAL_SECONDS * 10

iteration_count = 0
next_message_iteration = random.randint(MIN_INTERVAL_ITERATIONS, MAX_INTERVAL_ITERATIONS)
time.sleep(1)
click_to_focus()

while True:

    round_counter = 0


    if (first_loop):
        do_the_sign()
        first_loop = False

    if (queued == False):
        queue_game(robux_amount)        
        queued = True
    if detect_black():

        iteration_count = 0

        print("--------------")
        print("Game Detected!")
        print("--------------")

        time.sleep(4)
        do_pre_message()
        queued = False  

        while True:


            play_game()
            round_counter += 1

            if (round_counter >= 30):
                do_midgame_message()

            if determine_game():
                do_message()
                time.sleep(14)
                hold_keys(2)
                break
    
    iteration_count += 1

    if iteration_count >= next_message_iteration:
        do_join()
        hold_keys(1)
        iteration_count = 0
        next_message_iteration = random.randint(MIN_INTERVAL_ITERATIONS, MAX_INTERVAL_ITERATIONS)
    
    time.sleep(0.1)
    


