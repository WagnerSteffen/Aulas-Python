import time
import pywhatkit
import pyautogui


phone = '+5555999009007'
messege = ['Mensagem 1', 'Mensagem 2', 'Mensagem 3', 'Mensagem 4', 'Mensagem 5']
hms = time.strftime('%X')
hms = [int(i) for i in hms.split(":")]
print(hms)
for i in range(len(messege)):
    pywhatkit.sendwhatmsg(phone, messege[i], hms[0], hms[1]+(i+1), 15, True, 20)
    pyautogui.click(840, 980)
    time.sleep(3)
