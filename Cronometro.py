#! python3
# Cronometro

import time, subprocess

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft = timeLeft - 1

# Quando concluir, toca
subprocess.Popen(['start','alarm.wav'], shell=True)
