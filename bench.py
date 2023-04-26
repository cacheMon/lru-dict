
import time
import resource

# s = sys.argv[1].split('.')
# lru = __import__(s[0]).__dict__[s[1]]
from lru import LRU as lru

m = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
t = time.time()

cache = lru(1000000)
for i in range(1100000):
  cache[i] = i

print("Time : {} s, Memory : {} Kb".format(time.time()-t,
      resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - m))


# python bench.py pylru.lrucache
# python bench.py lru.LRU
