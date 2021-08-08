import threading 
from pyautogui import sleep
from pywintypes import error as pywin_error
import win32clipboard

class ClipboardWatchDog(threading.Thread):
    _clipboard_data = None
    _stop_flag = False
    _callback_func = None
    def __init__(self, callback : callable):
        super().__init__()
        if callback is None:
            raise Exception('`callback` is none')
        self._callback_func = callback

    def run(self):
        print('실행 중 입니다.')
        while not self._stop_flag:
            try:
                win32clipboard.OpenClipboard()
                clipboard_data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                
                if self._clipboard_data is not None and clipboard_data != self._clipboard_data:
                    print(f'/old: {self._clipboard_data} /new: {clipboard_data}')
                    self._callback_func(clipboard_data)
                self._clipboard_data = clipboard_data
                sleep(0.1)
            except pywin_error as e:
                if '5' in str(e) and 'OpenClipboard' in str(e): # = OpenClipboard Access Denined
                    continue
                print(f'warning, failed watch clipboard. cause, {type(e)}:{e}')
            except Exception as e:
                print(f'warning, failed watch clipboard. cause, {type(e)}:{e}')
                

    def stop(self):
        self._stop_flag = True

    
# test
if __name__ == '__main__':
    def printData(str):
        print(str)
    a = ClipboardWatchDog(printData)
    a.start()
    sleep(10)
    a.stop()

    a.join()
