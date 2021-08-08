from pyautogui import press, typewrite, sleep, keyUp, hotkey
from scripts.csv_reader import CSVReader
from scripts.winclip import ClipboardWatchDog
from sys import stdin

csvReader = None
def callback(clipboardData : str):
    global csvReader
    value = csvReader.find(clipboardData.strip())
    if value is None:
        return

    keyUp('ctrl')
    press(['left', 'left'])
    typewrite(value[0])
    keyUp('ctrl')
    
    #press('esc')
    press(['enter','enter'])
    #press(['right', 'right'])
    
    press('down')

    #press('ctrl')
    #hotkey('ctrl', 'c')

if __name__=="__main__":
    
    print('csv 파일을 넣으세요: ')

    csvReader = CSVReader(stdin.readline().rstrip())
    a = ClipboardWatchDog(callback)
    a.start()
    #sleep(10)
    #a.stop()
    #a.join()