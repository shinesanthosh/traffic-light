def control(veh):
    ways = len(veh) #no of lanes
    maxi = 0
    maxv = 0
    for num in range(0,ways):
        if(veh[num] > maxv):
           maxv = veh[num]
           maxi = num
    print(num," ",veh[num],"green")