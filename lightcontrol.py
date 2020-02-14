import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

lightstate = [[1,0,0],[1,0,0],[1,0,0],[1,0,0]]
pin = [[2,3,4],[5,6,7],[8,9,10],[11,12,13]]

def control(veh):
    maxlim = 120
    minlim = 0
    avgtime = 6
    lanes = 2
    ways = len(veh) #no of lanes
    times = []
    for i in range(0,ways):
        time = (veh[i]*avgtime)/lanes
        print time
        if time>maxlim: 
            allotime = maxlim
        elif time<minlim:
            allotime=minlim
        else:
            allotime=time
        times.append(allotime)
    return times

def setlight(listate,pino):
    for i in range(0,len(pino)):
        for j in range(0,3):
            if listate[i][j] == 1:
                GPIO.output(pino[i][j], GPIO.HIGH)
            else:
                GPIO.output(pino[i][j], GPIO.LOW)
                


def setlight(listate,pino):
    for i in range(0,len(pino)):
        for j in range(0,3):
            


def light(state):
    
    for i in range(0,len(state)):
        if state[i] == 2:
            lightstate[i] = [0,0,1]
        elif state[i] == 1:
            lightstate[i] = [0,1,0]
        else:
            lightstate[i] = [1,0,0]
        print lightstate
        setlight(lightstate,pin)
