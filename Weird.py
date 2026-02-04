#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    prop_1 = n % 2 == 1
    prop_2 = n % 2 == 0 and (n <= 5 and n >= 2)
    prop_3 = n % 2 == 0 and (n <= 20 and n >= 6)
    prop_4 = n % 2 == 0 and n > 20

    if prop_1 or prop_3:
        print("Weird")
    if prop_2 or prop_4:
        print('Not Weird')
