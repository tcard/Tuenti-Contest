#! /usr/bin/env python
# -*- coding: utf-8 -*-

# What is the sum of all emirps up to X?
#
# Sample input
#
# 100
# 200
#
# Sample output
#
# 418
# 1489

import sys
from math import sqrt, floor

def is_prime(n):
	if n == 2:
		return True
		
	if n % 2 == 0:
		return False
	
	for i in range(3, int(floor(sqrt(n))) + 1, 2):
		if n % i == 0:
			return False
	
	return True
	
for i in sys.stdin:
	print sum([n for n in range(1,int(i)) if 
		int(str(n)[::-1]) != n and \
		is_prime(n) and \
		is_prime(int(str(n)[::-1]))])