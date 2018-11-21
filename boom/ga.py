import random
import math

def selection(generation, width):
	results = [hit_coordinate(theta, v, width)[1] for (theta, v) in generation]
	return cumulative_probabilities(results)

def hit_coordinate(theta, v, width):
	x = 0.5 * width #bag size
	x_hit = width
	if theta > math.pi/2:
		x = -x
		x_hit = 0
	t = x / (v * math.cos(theta))
	y = v * t * math.sin(theta) - 0.5 * 9.81 * t * t
	if y > 0: y = 0.0
	return x_hit, y

def escaped(theta, v, width, height):
	x_hit, y_hit = hit_coordinate(theta, v, width)
	return (x_hit==0 or x_hit==width) and y_hit > height

def cumulative_probabilities(results):
	#could use itertools import accumulate in python3
	#scott, look that up because you don't know what she's talking about

	cp = []
	total = 0
	for res in results:
		total += res
		cp.append(total)
	return cp

def selection (generation, width):
	results = [hit_coordinate(theta, v, width)[1] for (teta, v) in generation]
	return cumulative_probabilities(results)

def choose(choices):
	p = random.uniform(0,choices[-1])
	for i in range(len(choices)):
		if choices[i] >= p:
			return i

def crossover(generation, width):
	choices = selection(generation, width)
	next_generation = []
	for i in range(0, len(generation)):
		num = generation[choose(choices)]
		dad = generation[choose(choices)]
		next_generation.append(breed(mum, dad))