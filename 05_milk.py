#! /usr/bin/env python
# -*- coding: utf-8 -*-

# You are an entrepreneur in Madrid, and have a brilliant idea to open a milk shop in Plaza Mayor. As you are very conscious, you want the milk you sell to be perfectly natural and fresh, and for that reason, you are shipping healthy cows from Zaragoza region to Madrid. At your disposal you have a truck with the weight limit, and a group of cows available for sale. Each cow can weigh differently, and produce a different amount of milk per day.
# 
# Your goal as an entrepreneur is to choose which cows to buy and transfer in your truck, so you can maximize the milk production, observing the truck weight limit.
# 
# Input Total number cows in Zaragoza area that are for sale.
# Input Total weight you truck can handle.
# Input List of cow weights, one per cow.
# Input List of cow milk production in liters per day, one per cow.
# 
# Output the maximum amount of milk production you can get.
# 
# Sample input
# 6 700 360,250,400,180,50,90 40,35,43,28,12,13
# 8 1000 223,243,100,200,200,155,300,150 30,34,28,45,31,50,29
# 10 2000 340,355,223,243,130,240,260,155,302,130 45,50,34,39,29,40,30,52,31
# 
# Sample output
# 93
# 188
# 320

import sys

class Cow:
	def __init__(self, weigth, milk):
		self.milk = milk
		self.weigth = weigth
	
	def productivity(self):
		return float(self.milk) / float(self.weigth)
		
	def __cmp__(self, other):
		if self.productivity() < other.productivity():
			return -1
		elif self.productivity() == other.productivity():
			return 0
		else:
			return 1
	
	def __repr__(self):
		return "%s kg, %s l/day, c. %s" % \
			(self.weigth, self.milk, self.productivity())
	
def select_cows(limit, truck, cows):
	# We will handle the problem this way:
	# 1. We assign each cow a productivity cocient: milk production/weigth.
	# 2. We fill the truck of cows, starting from the most productive to the least.

	truck_weigth = reduce(lambda x,y: x + y.weigth, truck, 0)
	
	for i in reversed(cows):
		if truck_weigth + i.weigth <= limit:
			truck.append(i)
			cows.remove(i)
			return select_cows(limit, truck, cows)
	
	# 3. When the truck is full, we check for each remaining cow if exchanging it with the
	# least productive cows in the truck would improve the total milk production.
	
	for i in reversed(cows):
		cows_to_remove = 0
		weight_to_free = limit - truck_weigth
		for j in reversed(truck):
			if weigth_to_free >= i.weigth:
				break
			cows_to_remove += 1
			weight_to_free += j.weigth
					
		if reduce(lambda x,y: x + y.milk, truck[-cows_to_remove:], 0) < i.milk:
			# 4. If any of them does, we exchange it and go to step 2
			
			while cows_to_remove > 0:
				cows_to_remove -= 1
				cows.append(truck.pop())
			cows.remove(i)
			truck.append(i)
			return select_cows(limit, truck, cows)
	
	# 5. If none of them do, we are finish.
	
	return (truck, cows)
	
for i in sys.stdin:
	args = i.split()
	cows = []
	weights = args[2].split(",")
	milks = args[3].split(",")
	
	for i in range(0,int(args[0])):
		cows.append(Cow(int(weights[i]), int(milks[i])))

	print reduce(lambda x,y: x+y.milk, select_cows(int(args[1]), [], cows)[0], 0)