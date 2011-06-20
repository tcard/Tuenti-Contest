#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Some Tuenti engineers really enjoy traveling around Spain by car. As any engineer, they like to plan and optimize things, so at every trip they plan in advance the stops they will need to make to refill the gas tank.
# There's a detailed map of the distances between the gas stations on their way, where d1 < d2 < ... < dn are the coordinates of all the n gas stations in their route and di is the distance from their origin to the gas station pi.
#
# It's known that:
# * the car starts traveling with the full tank
# * if the tank is full, they can travel for k kilometers
# * the distance between gas stations is no more than k
#
# Your task is to write an algorithm that calculates, for each trip, the list of gas stations they will need to stop to refill, in a way that they can complete the trip with the minimum possible number of stops.
#
# Input and output format:
# Input and output are received from the standard input and output streams.
#
# Input:
# T - the number of test cases you will need to solve
# For each test case you will receive:
# k - the max distance in kilometers that the car can travel if the tank is full
# df - the total distance to be traveled
# n - the number of gas stations on the way
# d1 d2 ... dn - the distance from the origin to each gas station (separated by a whitespace)
#
# Output:
# For each input, a line containing the list of gas station coordinates where the car should stop in a way that it stops as few as possible. Or No stops if they don't need to do any stop
#
# Limits
#   1 <= T <= 1000 
#   1 <= k <= 10^9 
#   1 <= df <= 10^9
#   1 <= n <= 10^9
#
# Sample input:
#
# 3
# 300
# 650
# 4
# 50 200 350 550
# 200
# 1000
# 17
# 8 50 90 180 200 290 390 480 551 600 620 730 850 860 880 930 980
# 100
# 95
# 4
# 10 40 50 60
#
# Sample output:
#
# 200 350
# 200 390 550 730 930
# No stops

import sys

num_tests = int(sys.stdin.readline())
for i in range(0, num_tests):
	max_d = long(sys.stdin.readline())
	total_d = long(sys.stdin.readline())
	num_stations = long(sys.stdin.readline())
	ds = map(long,sys.stdin.readline().split())
	
	km = max_d
	stations = []
	for j in range(0,num_stations):
		if ds[j] > km:
			stations.append(str(ds[j-1]))
			km = ds[j-1] + max_d
		if km >= total_d:
			break
	print " ".join(stations or ["No stops"])