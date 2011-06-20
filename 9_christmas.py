#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

num_cases = int(sys.stdin.readline())
cases = []
for i in range(0, num_cases):
	num_ligths = int(sys.stdin.readline())
	time = long(sys.stdin.readline())
	cases.append((num_ligths, time))
	
for i in cases:
	ligths = [str(n) for n in range(not i[1] % 2, min(i[0], i[1]), 2)]
	if ligths:
		print " ".join(ligths)
	else:
		print "All lights are off :("
	