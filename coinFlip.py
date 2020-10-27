from random import getrandbits
from time import sleep

bal = 100
deposit = 100
deposits = 0
winnings = 0
wins = 0
losses = 0
loss = 0

for x in range(1000):
    if bal < 2:
        deposits += 1
        bal += deposit
        print("deposited: " + str(deposit))
        print("total deposits: " + str(deposits))

    half = int(round((bal/2)))
    if getrandbits(1):
        print("Win " + str(half))
        bal += half
        wins += 1
        winnings += half
    else:
        print("loss " + str(half))
        bal -= half
        losses += 1
        loss += half
    print("balance: " + str(bal))

print("wins: " + str(wins))
print("winnings: " + str(winnings))
print("losses: " + str(losses))
print("lost: " + str(loss))
print("deposits: " + str(deposits))
print("balance: " + str(bal))