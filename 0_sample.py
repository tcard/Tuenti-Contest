#! /usr/bin/env python

# Your amazing program should sum the numbers given in each line, and one line for each question with the response. Note that some numbers might be negative.
#
# Sample input:
#
# 2 3
# 4 5 1
#
# Sample output:
#
# 5
# 10

import sys

for i in sys.stdin:
	print sum(map(int,i.split()))
