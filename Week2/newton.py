import sys

def nextStep(val):
    nextVal = val - function(val)/derev(val)
    return nextVal

def function(val):
    return float(val**2-5)

def derev(val):
    return float(2*val)

def main(val, thresh):
    done = False
    while not done:
        oldVal = val; 
        val = nextStep(val)
        print(val)
        if abs((oldVal-val)/(oldVal))<thresh:
            print("Done")
            done = True

if __name__=="__main__":
    val = float(sys.argv[1])
    thresh = float(sys.argv[2])/100
    main(val, thresh)
    
