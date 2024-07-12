import time
import pyautogui
import random
import keyboard

messages_pre = [
    "",
    "",
    "",
    "hi",
    "hii",
    "heii",
    "haii :D",
    "hihi",
    "",
    "",
    "pls let me win",
    "pls lemme win i have all day",
    "wsg",
    "wassup",
    "pls bro",
    "haelo"
]

messages_post = [
    "lessgoooo",
    "meow",
    "XD",
    "bruhh",
    "GG",
    "ggs",
    "gs",
    "G",
    "",
    "wow",
    "erm what the sigma",
    "ggwp",
    "skib?",
    "skibidi",
    "FINALLYY",
    "XDDD",
    "woww",
    "bro whst",
    "????",
    "bro what",
    "sigma",
    "I am skbidii sigma",
    "i am the alpha wolf",
    "awOOOOO",
    "AWOOOO",
    "grrr",
    "rawrrr",
    "that was actually kinda scarry ",
    "ayay i finaly won!",
    "yay i finally won",
    "balls",
    "pro gambler xd",
    "GIMME DEM ROBUX",
    "ty",
    "good games :DD:D:D:D",
    "I COOKED",
    "holeyyyy",
    "Gg",
    "GGS",
    "gggs"
]

messages_join = [
    "join mh game please",
    "JOIN PLS",
    "pls joinnn",
    "pls join",
    "hi ples join my game",
    "HIII JOIN PLS",
    "join my game i wait so long",
    "PLS JOIN",
    "join my game pls!!!!",
    "lets play my game :D",
    "anyone looking to joiinnn ?",
    "join me!",
    "JOIN ME",
    "join me game!!!"
]

messages_sign = [
    "waiting pls join",
    "waiting pls join!",
    "please join my game im waiting",
    "hii join my game i am waiting",
    "waiting for join my game",
    "waiting for join"
]

messages_mid = [
    "bro",
    "brp im not giving up",
    "im not giving up",
    "im not giving up i gort al day",
    "bro i got all day",
    "..../",
    "got al dayu bro",
    "stop stallin ",
    "r u a bot?",
    "bruh",
    "BROOO",
    "srlsy?",
    "staller",
    "u BOT?",
    "erm",
    "im not even tired",
    "wasting yuor own time",
    "got th e eintire day",
    "got the whole day"
]

def type_message(message):
    pyautogui.write('/')
    time.sleep(0.1) 
        
    pyautogui.write(message)
    time.sleep(0.1) 
        
    keyboard.press_and_release('enter')

def type_message_modified(message):

    pyautogui.write(message)
    time.sleep(0.1) 
        
    keyboard.press_and_release('enter')

def get_message(messagetemp):
    random_index = random.randint(0, len(messagetemp) - 1)
    return messagetemp[random_index]


def do_message():
    type_message(get_message(messages_post))

def do_pre_message():
    type_message(get_message(messages_pre))

def do_join():
    type_message(get_message(messages_join))

def do_sign():
    type_message_modified(get_message(messages_sign))

def do_midgame_message():
    if random.randint(1,9) == 5:
        type_message_modified(get_message(messages_mid))