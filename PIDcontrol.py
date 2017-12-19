import random as r
import time as t

'''
This project's purpose is to perform simple testing of PID controller
in a "simulated" environment (i.e. no external features to correct).
'''

target = int(input('Enter target: '))
it_time = int(input('Enter it_time: '))

kp = 0.6
ki = 0.6
kd = 0.6

i_base_out = 0
errorPrior_default = 0

randomStart = r.randint(1, target)

def compP(_kp, targetValue, currentValue):
    error = targetValue - currentValue
    p_output = _kp * error
    return p_output

def compI(_ki, targetValue, currentValue, integOut):
    error = targetValue - currentValue
    i_output = integOut + (_ki * error)
    return i_output

def compD(_kd, targetValue, currentValue, _errorPrior):
    error = targetValue - currentValue
    d_output = (error - _errorPrior) / it_time
    return d_output

newPOut = compP(kp, target, randomStart)
newIOut = compI(ki, target, randomStart, i_base_out)
newDOut = compD(kd, target, randomStart, errorPrior_default)

#ENTER 1, 2, 3, OR 4 FOR CORRESPONDING MODES
choice = input('Enter choice: ')

if(choice == 1):
    newVal = randomStart + newPOut
elif(choice == 2):
    newVal = randomStart + newPOut + newIOut
elif(choice == 3):
    newVal = randomStart + newPOut + newDOut
else:
    newVal = randomStart + newPOut + newIOut + newDOut

newError = target - newVal

if (target != newVal):
    while(target != newVal):
        t.sleep(0.01)
        newPOut = compP(kp, target, newVal)
        newIOut = compI(kp, target, newVal, newIOut)
        newDOut = compD(kd, target, randomStart, newError)
        newVal = newVal + newPOut + newIOut + newDOut
        print(newVal)
        
