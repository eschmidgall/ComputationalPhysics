#trapParallel_1.py
#example to run: mpiexec -n 4 python trapParallel_1.py 0.0 1.0 10000
import numpy
import sys
import random
import pylab as plb
from mpi4py import MPI
from mpi4py.MPI import ANY_SOURCE

class NotMod(Exception):
    def __init__(self, num_walkers, size):
        self.num_walkers = num_walkers
        self.size = size
    def __str__(self):
        return "Number of walkers: "+str(num_walkers)+" not divisible by "+str(size)
        
    
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#Variables are num_walkers and num_steps
num_walkers = int(sys.argv[1])
num_steps = int(sys.argv[2])

def randomWalk(num_steps, pos):
    for i in range(num_steps):
        step = random.choice([-1,1])
        pos = pos+step
    return pos
        

if num_walkers % size:
    raise NotMod(num_walkers, size) 
    
local_numWalkers = num_walkers/size; 

walkLengths = numpy.zeros(local_numWalkers)
recv_buffer = numpy.zeros(local_numWalkers)

for n in range(local_numWalkers):
    walkLengths[n] = randomWalk(num_steps,0) 

if rank == 0:
        total = walkLengths
        for i in range(1, size):
            comm.Recv(recv_buffer, ANY_SOURCE)
            total = numpy.append(total, recv_buffer)
else:
        comm.Send(walkLengths, dest =0)

if comm.rank == 0:
        n, bins, patchs = plb.hist(total, 2*num_steps+1, normed = False, histtype = 'stepfilled')
        plb.xlabel('Number of Steps')
        plb.ylabel('Number of Walks')
        plb.title('Distribution for '+str(num_walkers)+' walks of '+str(num_steps)+' steps, Parallel on '+str(size)+' Processes')
        plb.show()

        fname = 'numWalks_'+str(num_walkers)+'_numSteps_'+str(num_steps)+'.txt'
        numpy.savetxt(fname,total, fmt = '%i')
        
