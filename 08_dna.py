#! /usr/bin/env python
# -*- coding: utf-8 -*-

# You are a biologist examining dna sequences of different life forms. you are given two dna sequences, and the goal is to find the largest ordered set of adjecent bases that are the same in both DNAs. 
# 
# DNA sequences are given as ordered sets of nucleotide bases: adenine (abbreviated a), cytosine (c), guanine (g) and thymine (t). 
# 
# ATGT*CTTCCT*CGA 
#   TG*CTTCCT*ATGAC
#  
# For the example above, the result is CTTCCT because that is the largest ordered set of adjecent bases that can be found in both lifeforms.
# Input and output are received from the standard input and output streams. 
# Input: Two strings of dna nucleotide bases, each representing one genome sequence. 
# Output: A single string - the longest sequence of adjecent nucleotide bases that are present in both lifeforms. 
# 
# Input sample
# 
# ctgactga actgagc
# cgtaattgcgat cgtacagtagc
# ctgggccttgaggaaaactg gtaccagtactgatagt
# 
# Output sample
# 
# actga
# cgta
# actg

import sys

# This is the first solution I came up with.
# Not efficient enough but I find it prettier, so I'm leaving it here.

# for i in sys.stdin:
# 	args = i.split()
# 	end = False
# 	for j in reversed(range(0,len(args[0])+1)):
# 		offset = len(args[0]) - j
# 		while offset >= 0:
# 			if "".join(args[0][0+offset:j+offset]) in args[1]:
# 				print args[0][0+offset:j+offset]
# 				end = True
# 				break
# 			offset -= 1
# 		if end: break

for i in sys.stdin:
	arg = i.split()
	
	longest = []
	matching = []
	offset = len(arg[0])-1
	while offset >= 0:
#		print "%s\n%s%s\n" % (arg[0], " " * offset, arg[1])
		for j in range(0,len(arg[0])):
			try:
				if arg[0][j+offset] == arg[1][j]:
					matching.append(arg[1][j])
				elif matching:
					if len(matching) > len(longest):
						longest = matching
#					print "*", matching
					matching = []
			except IndexError:
				if len(matching) > len(longest):
					longest = matching
#				if matching: print "*", matching
				break
		offset -= 1
	offset = 1
	matching = []
	while offset < len(arg[1]):
#		print "%s%s\n%s\n" % (" " * offset, arg[0], arg[1])
		for j in range(0,len(arg[0])):
			try:
				if arg[0][j] == arg[1][j+offset]:
					matching.append(arg[0][j])
				elif matching:
					if len(matching) > len(longest):
						longest = matching
#					print "*", matching
					matching = []
			except 	IndexError:
				if len(matching) > len(longest):
					longest = matching
#				if matching: print "*", matching
				matching = []
				break
		offset += 1
		matching = []
	print "".join(longest)
			
