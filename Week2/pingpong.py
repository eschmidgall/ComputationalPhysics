import numpy
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
count = numpy.zeros(1)

while count<10:
    if rank==0:
        count = count+1
        comm.Send(count,dest=1)
        print('Ping! Count = '+str(count))
        comm.Recv(count, source = 1)
    if rank==1:
        comm.Recv(count, source = 0)
        count=count+1
        print('Pong! Count='+str(count))
        comm.Send(count, dest=0)
        
if comm.rank==1:        
    print("Total messages sent: "+str(count))

        
