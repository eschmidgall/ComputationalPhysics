def enumerateRandWalk(x,N):
	if N==1 and x==0:
		return 0
	if N==1 and x==-1:
		return 1
	if N==1 and x==1:
		return 1
	if abs(x)>N:
		return 0
	else:
		return enumerateRandWalk(x-1,N-1)+enumerateRandWalk(x+1,N-1)

def walkIt(minN, maxN):
    results =[]
    for N in range(minN,maxN+1):
        for x in range(-N, N+1):
            numWalks = enumerateRandWalk(x,N)
            results.append([x,N,numWalks])
    return results

def main():
    results = walkIt(4,8)
    f = open("randomWalks.txt", "w")
    f.write('x,N,num\n')
    for result in results:
        f.write(str(result[0])+","+str(result[1])+","+str(result[2])+"\n")
    f.close()

if __name__=="__main__":
    main()
