#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Your amazing program should calculate the sum if the numbers given in each line, and output on line for each question with the response. Numbers can be negative, really big and lines contain extra spaces, so make your program resistant to input.
#
# Your program will need to read from standard input, line by line till the end of the input. Consider each line a different question. For each line you read, output the sum of all the given numbers.
# 
# Sample input
# 
# 2 3
# 4 5 -1
#
# Sample output
#
# 5
# 8

import sys

for i in sys.stdin:
	print sum(map(long,i.split()))
