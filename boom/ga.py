import random
import math
import matplotlib.pyplot as plt

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

def breed(mum, dad):
	return (mum[0], dad[1])

def mutate(generation):
	for i in range(len(generation)-1):
		(theta, v) = generation[i]
		if random.random() < 0.1:
			new_theta = theta + random.uniform(-10,10) * math.pi/100
			if 0 < new_theta < 2 * math.pi:
				theta = new_theta
			if random.random < 0.1:
				v += random.uniformation(0.9, 1.1)
			generation[i] = (theta, v)

def fire():
	epochs = 10
	items = 12
	height = 5
	width = 10

	generation = random_tries(items)
	generation0 = list(generation)

	for i in range(1,epochs):
		results = []
		generation = crossover(generation, width)
		mutate(generation)

	display_start_and_finish(generation0, generation, height, width)

def display(generation, ax, hight, width):
	rect = plt.Rectangle((0,0), width, height, facecolor='grey')
	ax.add_patch(rect)
	ax.set_xlabel('x')
	ax.set_ylabel('y')
	ax.set_xlim(-width, 2 * width)
	ax.set_ylim(0,4.0 * height)
	free = 0

	result = launch(generation, height, width)
	for res, (theta, v) in zip(result, generation):
		x = [j[0] for j in res]
		y = [j[1] for j in res]
		if escaped(theta, v, width, height):
			ax.plot(x, y, 'ro-', linewidth=2.0)
			free += 1
		else:
			ax.plot(x,y, 'bx-', linewidth=2.0)
	print("Escaped", free)


