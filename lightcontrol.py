import serial

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

def light(state):
    output = []
    for i in range(0,len(state)):
        if state[i] == 2:
            output.append('g')
        elif state[i] == 1:
            output.append('y')
        else:
            output.append('r')
    print output