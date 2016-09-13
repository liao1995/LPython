import webbrowser
import time

total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open("http://github.com/liao1995")
    break_count = break_count + 1
