# Shawn Anderson October 12 2019
# Inspired by https://github.com/corbanworks/fng-sin-tools/blob/master/fngsin.class.php

import random
from math import floor
def generateSIN():
        validPrefix = [1,2,3,4,5,6,7,9]
        sin = [random.choice(validPrefix)]
        length = 9
        while(len(sin) < (length - 1)):
                sin.append(random.choice(range(0,9)))
        sum = 0
        pos = 0
        reversedSIN = list(reversed( sin ))
        while(pos < length - 1):
                odd = reversedSIN[ pos ] * 2;
                if(odd > 9):
                        odd -= 9
                sum += odd
                if(pos != (length - 2)):
                        sum += reversedSIN[ pos +1 ]
                pos += 2
        checkdigit = (( floor(sum/10) + 1) * 10 - sum) % 10;
        sin  += [checkdigit]
        return ''.join([str(int(x)) for x in sin])

if __name__ == "__main__":
    print(generateSIN())

