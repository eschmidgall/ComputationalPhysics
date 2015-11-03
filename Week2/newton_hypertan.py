import sys
import math

def nextStep(val):
    nextVal = val - function(val)/derev(val)
    return nextVal

def function(val):
    return float(math.tanh(val))

def derev(val):
    return (1-float(math.tanh(val))*float(math.tanh(val)))

def main(val,thresh):
    done = False
    while not done: 
        oldVal = val
        try: 
            val = nextStep(val)
            print(val)
            if abs(val-oldVal)<thresh:
                done = True
        except ZeroDivisionError:
            print("Previous value: "+str(val))
            print("ZeroDivisionError")
            done = True
 

if __name__=="__main__":
    val = float(sys.argv[1])
    thresh = float(sys.argv[2])
    main(val,thresh)
    
