#This challenge aims to determine the number of pairs of matching socks.
from collections import Counter
def matchingSocks(number, arr):
    socks = 0
    for element in Counter(arr).values():
        socks+=element//2
    return socks
