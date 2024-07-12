import easyocr
from PIL import Image
import pyautogui
import io   
import time

reader = easyocr.Reader(['en'])

def extract_text_from_screen_region(region):
    
    result = reader.readtext(pyautogui.screenshot(region=region))
    
    text = ' '.join([item[1] for item in result])
    
    return text

region = (596, 308, 171, 33)

def get_text():
    return extract_text_from_screen_region(region)


time.sleep(1)
print(get_text())
