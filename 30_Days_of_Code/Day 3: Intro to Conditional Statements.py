#Given an integer,n, perform the following conditional actions:

 #   If n is odd, print Weird
 #   If n is even and in the inclusive range of 2 to 5 , print Not Weird
 #   If n is even and in the inclusive range of 6 to 20 , print Weird
 #   If n is even and greater than 20, print Not Weird
# Constraints 1<= n <=100 

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    N = int(input())
    if(N % 2 != 0):
        print("Weird")
    else:
        if(N>=2 and N<=5):
            print("Not Weird")
        elif(N>=6 and N<=20):
            print("Weird")
        elif(N>20):
            print("Not Weird")
