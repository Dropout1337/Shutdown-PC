import os
import time

os.system('cls & title [SHUTDOWN] By Dropout ^| Main Menu')

print(
    '\n[\u001b[31m1\u001b[37m]  Shutdown Your PC',
    '\n[\u001b[31m2\u001b[37m]  Restart Your PC'
)
choice = input('\n\u001b[31m>\u001b[37m Choice\u001b[31m:\u001b[37m ')
if "1" in choice:
    os.system('title [SHUTDOWN] By Dropout ^| Shutting Down In 3 Seconds')
    print('\u001b[31m>\u001b[37m Shutting Down...')
    time.sleep(3)
    os.system('shutdown.exe /s /t 00')
elif "2" in choice:
    os.system('title [SHUTDOWN] By Dropout ^| Restarting In 3 Seconds')
    print('\u001b[31m>\u001b[37m Restarting...')
    time.sleep(3)
    os.system('shutdown.exe /r /t 00')    
else:
    print('\n[\u001b[31m!\u001b[37m] Invalid Option')
    os.system('pause >NUL')
    os._exit(0)    
