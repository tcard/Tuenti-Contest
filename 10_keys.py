#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

num_combos = int(sys.stdin.readline())
combos = []
for i in range(0, num_combos):
	keys = set(sys.stdin.readline().strip().split())
	command = sys.stdin.readline().strip()
	combos.append((keys, command))

num_tests = int(sys.stdin.readline())
for i in range(0, num_tests):
	combo = set(sys.stdin.readline().strip().split())
	print filter(lambda x: x[0] == combo, combos)[0][1]