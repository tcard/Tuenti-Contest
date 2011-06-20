#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
			
for i in sys.stdin:
	args = i.split(" ")
	source = unicode(args[0], "utf-8")
	target = unicode(args[1], "utf-8")
	cost = (int(args[2][0]), int(args[2][2]), int(args[2][4]))

	# Levenshtein distance algorith. Not mine!
	
	d = []
	for i in range(0, len(source)+1):
		d.append([])
		d[i].append(i)
	for i in range(1, len(target)+1):
		d[0].append(i)
	for i in range(1, len(source)+1):
		for j in range(1, len(target)+1):
			d[i].append(min(
				d[i-1][j] + cost[1],
				d[i][j-1] + cost[0],
				d[i-1][j-1] + (source[i-1] != target[j-1] and cost[2] or 0)))
	print d[len(source)][len(target)]