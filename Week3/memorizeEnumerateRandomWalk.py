'''Playing with Python Decorators for Memorization, available documentation:
https://wiki.python.org/moin/PythonDecoratorLibrary
This works like the dictionary in fastEnumerateRandomWalk.py but it's done
automatically as part of the memoized class. This is just a fun exercise. '''

import collections
import functools

class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

@memoized
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
        print(N)
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
