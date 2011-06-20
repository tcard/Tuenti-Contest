#! /usr/bin/env python
# -*- coding: utf-8 -*-

# You are trying to solve a very complex problem. In order to simplify it, you have divided it into many sub tasks. Most of these sub-tasks can be run in parallel, but some are dependent on the previous resolution of other tasks. There is no limit on the number of tasks that can be run in parallel. Each task has an associated computation time.
# You are be given a subset of these tasks. For each of them you need to specify what is the minimal computation time for resolving the task (you must consider task dependencies).
# 
# The relations between the tasks are represented in the file contained in this archive: in.zip.This file is in the following format:
# 
# #Number of tasks
# n
# 
# #Task duration <- task x has an associated computation time of tx
# x,tx
# 
#Task dependencies <- the resolution of task x depends of previously solving tasks y,z,w
# x,y,z,w
# 
# It is imposible for two different tasks to be dependent on the resolution of one common task:
# 
# #Task dependencies <- this is not valid
# x,y
# z,y
# 
# The expected output is the following format: taskId taskComputationTime
# 
# x tx
# y ty
# z tz

# From the standard input you will receive a set of tasks for which to compute the total time in the following format:
#
# x,y,z

import sys

def get_deps(task):
	"Returns a set with every task a task is depending on, including its children's dependences."
	ret = set([task])
	try: 
		for i in tasks_deps[task]:
			ret.add(i)
			ret = ret.union(get_deps(i))
		return ret
	except KeyError:
		return set()

def get_times(task):
	"Returns the time that a task would take, counting on its dependences."
	ret = tasks_times[task]
	try:
		deps_times = []
		for i in tasks_deps[task]:
			deps_times.append(get_times(i))
		ret += max(deps_times)
	except KeyError:
		pass
	return ret
	
infile = open("in")
wanted_tasks = sys.stdin.read().split(",")

tasks_deps = {}		# 1,2,3 -> {"1":["2","3"]}
tasks_times = {}	# 1,2 -> {"1":2}

# A little trick now: go backwards until the start position of the dependencies.

infile.seek(0,2)
while infile.read(1) != "s":
	infile.seek(-2,1)
infile.seek(1,1)

# Now parse each dependence declaration line, storing at tasks_deps.

for i in infile:
	l = i.strip().split(",")
	tasks_deps[l[0]] = l[1:]

infile.seek(0,0)
while infile.readline().strip() != "#Task duration":
	pass
init_times = infile.tell()
wanted = set()

for task in wanted_tasks:
	task = task.strip()
	wanted = get_deps(task).difference(wanted) 
	infile.seek(init_times,0)
	while wanted:
		line = infile.readline().strip().split(",")
		if line[0] in wanted:
			# We're only parsing the duration declaration of the tasks we are actually
			# interested at, for memory saving reasons.
			
			tasks_times[line[0]] = int(line[1])
			wanted.remove(line[0])
	print task, get_times(task)