import pyautogui
from urllib import parse
import time
import webbrowser as web

phone = ['+5555999009007']
text = parse.quote('Isso é um teste')
web.open(f'https://web.whatsapp.com/send?phone={phone}&text={text}')
time.sleep(15)
pyautogui.click(840, 980)
pyautogui.press('enter')
time.sleep(5)
