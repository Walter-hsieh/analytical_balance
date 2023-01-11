import datetime
import time


# 倒數時間/模組
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        a = datetime.datetime.now()
        print(a)
        time.sleep(1)
        t -= 1





countdown(60)
