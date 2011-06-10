#! /usr/bin/env python

import sys

for i in sys.stdin:
	print sum(map(int,i.split()))
