def enumerateRandWalk(x,N):
        global randWalks
        if N==1 and x==0:
                return 0
        if N==1 and x==-1:
                return 1
        if N==1 and x==1:
                return 1
        if abs(x)>N:
                return 0
        if str(N) in randWalks and str(x) in randWalks[str(N)]:
                return randWalks[str(N)][str(x)]
        else:
                numWalks = enumerateRandWalk(x-1,N-1)+enumerateRandWalk(x+1,N-1)
                if str(N) not in randWalks:
                        randWalks[str(N)]= dict()
                randWalks[str(N)][str(x)]= numWalks        
                return numWalks
                
def walkIt(minN, maxN):
        global randWalks
        results =[]
        randWalks = dict()
        for N in range(minN,maxN+1):
                print("Now doing N="+str(N))
                for x in range(-N, N+1):
                        numWalks = enumerateRandWalk(x,N)
                        results.append([x,N,numWalks])
        return results

def main():
        results = walkIt(1,500)
        f = open("randomWalks.txt", "w")
        f.write('x,N,num\n')
        for result in results:
                f.write(str(result[0])+","+str(result[1])+","+str(result[2])+"\n")
        f.close()

if __name__=="__main__":
        main()
