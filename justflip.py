import sys
from random import getrandbits

iterations = int(sys.argv[1]) if len(sys.argv) > 1 else 100
heads = 0
tails = 0

for x in range(iterations):
    heads += getrandbits(1)

tails = iterations - heads

print("flips: " + str(iterations))
print("heads: " + str(heads))
print("tails: " + str(tails))