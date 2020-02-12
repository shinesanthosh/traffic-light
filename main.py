import serial
import lightcontrol
import time


state = [0,0,0,0]
retime = lightcontrol.control([1,1,1,1])
ways = len(retime)

while True:
    for i in range(0,ways):
        state[i] = 2
        lightcontrol.light(state)
        time.sleep(retime[i])
        state[i] = 1
        lightcontrol.light(state)
        if retime[i] == 0:
            time.sleep(0)
        else:
            time.sleep(5)
        state[i] = 0
        lightcontrol.light(state)
