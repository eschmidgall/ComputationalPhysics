import sys
import ast

def nextStep(val1,val2):
    nextVal = float(val2*function(val1)-val1*function(val2))/float(function(val1)-function(val2))
    return nextVal

def function(val):
    return float(val**2-5)

def main(vals, thresh):
    done = False
    x1 = vals[0]
    x2 = vals[1]
    print(thresh)
    while not done:
        x0 = nextStep(x1,x2)
        if abs((x0-x1)/(x1))<thresh:
            done = True
            print("The root is: "+str(x0))
        else:
            x2 = x1
            x1 = x0
            print("Current step: ["+str(x1)+","+str(x2)+"]")

if __name__=="__main__":
    vals = ast.literal_eval(sys.argv[1])
    thresh = float(sys.argv[2])/100
    main(vals, thresh)
    
