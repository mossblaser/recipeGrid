#!/usr/bin/python

from recipeGrid.model import Ingredient, Quantity, Substance


def multi_find(string, *targets):
	candidate = None
	candidate_pos = -1
	for target in targets:
		pos = string.find(target)
		if pos != -1 and (pos < candidate_pos or candidate_pos == -1):
			candidate = target
			candidate_pos = pos
	
	return (candidate, candidate_pos)


def nested_split(string):
	output = []
	
	while True:
		string = string.strip()
		next_delim, delim_pos = multi_find(string, "(", ",", ")")
		
		if next_delim == "(":
			# Add a bracketed section
			
			# Get the section before the bracket
			before = string[:delim_pos].strip()
			assert(before != "")
			
			# Get the section inside the brackets
			inside, after = nested_split(string[delim_pos+1:])
			assert(after[0] == ")")
			
			output.append((before, inside))
			string = after[1:]
			
		elif next_delim == ",":
			# Just continue on as before, ignoring the comma
			
			before = string[:delim_pos].strip()
			output.append(before)
			
			string = string[delim_pos+1:]
			
		elif next_delim == ")":
			# Reached the end of a bracketed block
			before = string[:delim_pos].strip()
			output.append(before)
			after = string[delim_pos:]
			
			return output, after
			
		elif string != "":
			# One last value is present
			output.append(string)
			string = ""
			
		else:
			# All the data has been handled, job done!
			return output, ""


def interpret_steps(ingredients, steps):
	substances = []
	for step in steps:
		if type(step) is tuple:
			
			substance = Substance(step[0],
			                      *interpret_steps(ingredients, step[1]))
			substances.append(substance)
		elif step in ingredients.keys():
			substances.append(ingredients[step])
		elif step != "":
			substances.append(Substance(step))
	
	assert(substances != [])
	return substances


def interpret(ingredients, english):
	english = english.strip()
	if english == "":
		return None
	
	steps, _ = nested_split(english)
	return interpret_steps(ingredients, steps)

