#!/usr/bin/python3
for x in range(ord('z'), ord('a') - 1, -1):
    if x % 2 == 0:
        res = 0
    else:
        res = 32
    print('{}'.format(chr(x - res)), end="")
