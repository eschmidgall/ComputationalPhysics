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

def runSimulation(num_walkers, initial_positions, num_steps):
    if not initial_positions:
        initial_positions = [random.randint(-num_steps,num_steps) for a in range(num_walkers)]
    walkers = initializeWalkers(num_walkers, initial_positions)
    positions = [initial_positions]
    for i in range(1,num_steps):
        stepPosition = runStep(walkers)
        positions.append(stepPosition)
    return positions

def plotResults(num_walkers, num_steps, positions):
    steps = range(num_steps)
    for i in range(num_walkers):
        walkerPos = [position[i] for position in positions]
        pylab.plot(steps,walkerPos)
    pylab.title('Random Walk Simulation')
    pylab.xlabel('Time (Steps)')
    pylab.ylabel('Position')
    pylab.show()

def main(num_walkers, num_steps, initial_positions):
    positions = runSimulation(num_walkers, initial_positions, num_steps)
    plotResults(num_walkers, num_steps, positions)

if __name__=="__main__":
    num_walkers = int(sys.argv[1])
    num_steps = int(sys.argv[2])
    initial_positions = sys.argv[3]
    if initial_positions =='None':
        initial_positions = None
    else:
        initial_positions = ast.literal_eval(initial_positions)
    main(num_walkers, num_steps, initial_positions)
        
