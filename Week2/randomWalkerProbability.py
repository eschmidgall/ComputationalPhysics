import math
import random
import sys
import pylab
import ast

class Walker1D(object):
    '''
    A random walker in 1D
    '''
    def __init__(self,pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def move(self):
        pos = self.pos
        moveStep = random.choice([1,-1])
        self.pos = pos+moveStep
        return self.pos

def initializeWalkers(num_walkers,initial_positions):
    walkers = []
    for i in range(num_walkers):
        walker = Walker1D(initial_positions[i])
        walkers.append(walker)
    return walkers

def runStep(walkers):
    walkerPos = []
    for walker in walkers:
        position = walker.move()
        walkerPos.append(position)
    return walkerPos

def runOneSimulation(num_walkers, initial_positions, num_steps):
    if not initial_positions:
        initial_positions = [random.randint(-num_steps,num_steps) for a in range(num_walkers)]
    walkers = initializeWalkers(num_walkers, initial_positions)
    for i in range(1,num_steps):
        stepPosition = runStep(walkers)
    return stepPosition

def plotResults(displaceVec, num_steps):
    numBins = len(range(-num_steps, num_steps+1))
    n,bins,patches = pylab.hist(displaceVec,numBins, normed = 1, histtype = 'stepfilled')
    pylab.show()
    
def main(num_sims,num_walkers, num_steps, initial_positions):
    netDisplace = []
    for n in range(num_sims): 
        finalPosition = runOneSimulation(num_walkers, initial_positions, num_steps)
        netDisplace.append(finalPosition)
    displaceVec = [item for sublist in netDisplace for item in sublist]
    plotResults(displaceVec, num_steps)

if __name__=="__main__":
    num_sims = int(sys.argv[1])
    num_walkers = int(sys.argv[2])
    num_steps = int(sys.argv[3])
    initial_positions = sys.argv[4]
    if initial_positions =='None':
        initial_positions = None
    else:
        initial_positions = ast.literal_eval(initial_positions)
    main(num_sims, num_walkers, num_steps, initial_positions)
        
