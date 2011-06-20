#! /usr/bin/env python
# -*- coding: utf-8 -*-

# We use a variety of languages and technologies here at Tuenti. Sometimes we even develop our own languages and tools. Here is an example from a programming language that we use when we want to blow our minds. Your task is to interpret it!

# Sample input

# ^= 1 2$
# ^# 2 2$
# ^@ 3 1$

# Sample output
# 3
# 4
# 2

import sys

class ParseException(Exception):
	def __init__(self, command, info):
		self.command = command
		self.info = info
	def __str__(self):
		return "Unrecognized command: %s, %s" % self.command, self.info
		
def parse(command):
	command = command.strip()
	if command.isdigit():
		return long(command)
	if command[0] == "^" and command[-1] == "$":
		op1 = ""
		depth = 0
		pointer = 3
				
		while 1:
			try:
				if command[pointer] == "^":
					depth += 1
				elif command[pointer] == "$":
					if depth == 0:
						break
					else:
						depth -= 1
				elif command[pointer] == " " and depth == 0:
					break
				op1 += command[pointer]
				pointer += 1
			except IndexError:
				raise ParseException(command, "unbalanced expression")
		
		if command[pointer] == "$":
			if command[1] == "=":
				return parse(op1)
			elif command[1] == "@":
				return -parse(op1)
			else:
				raise ParseException(command, "unknown operator: %s" % command[1])
				
		op2 = ""
		pointer += 1
		
		while 1:
			try:
				if command[pointer] == "^":
					depth += 1
				elif command[pointer] == "$":
					if depth == 0:
						break
					else:
						depth -= 1
				op2 += command[pointer]
				pointer += 1
			except IndexError:
				raise ParseException(command, "unbalanced expression")
				
		if command[1] == "=":
			return parse(op1) + parse(op2)
		elif command[1] == "#":
			return parse(op1) * parse(op2)
		elif command[1] == "@":
			return parse(op1) - parse(op2)
		else:
			raise ParseException(command, "unknown operator: %s" % command[1])
	else:
		raise ParseException(command, "syntax error")
		
for i in sys.stdin:
	try:
		print parse(i)
	except ParseException as error:
		print "Problem at line: %s" % i
		print error