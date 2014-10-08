# RLE EXAMPLE: works only with letters
from itertools import groupby

def runLengthEncode (plainText):
    res = []

    for k,i in groupby(plainText):
        run = list(i)
        if(len(run) > 4):
            res.append("/{:02}{}".format(len(run), k))
        else:
            res.extend(run)

    return "".join(res)
# /RLE EXAMPLE

# Playground
import random


def gen(qty):
    return ''.join(random.choice('0123456789ABCDEF') for i in range(qty))
