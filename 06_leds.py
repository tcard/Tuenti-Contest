#! /usr/bin/env python
# -*- coding: utf-8 -*-

# You have a digital, 7 led segment, clock. One day, while waking up from a sci-fi dream, you wonder: how many times will the individual leds turn on after X seconds, from a 00:00:00 position? Take into account that every second, all leds turn off and then the ones for the next position will turn on.

import sys, time

segments = {
	"0": 6,
	"1": 2,
	"2": 5,
	"3": 5,
	"4": 4,
	"5": 5,
	"6": 6,
	"7": 3,
	"8": 7,
	"9": 6
}

for i in sys.stdin:
	orig = time.mktime((2000,1,1,0,0,0,0,1,-1))
	secs = int(i)
	num_leds = 0
	
	while secs >= 0:
		num_leds += reduce(lambda x,y: x + segments[y], time.strftime("%H%M%S", time.localtime(orig+secs)), 0)
		secs -= 1
	
	print num_leds
	