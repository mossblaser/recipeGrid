#!/usr/bin/python

import re

from generator.ingredients import interpret as get_ingredients
from generator.steps       import interpret as get_recipe
from generator.serves      import interpret as get_serves



def parse_recipe_file(english, scale = None, serve = None):
	sections = filter(None, map(str.strip, english.strip().split("\n\n")))
	assert(len(sections) >= 3)
	
	# The title should be the first section
	title = sections[0].strip()
	
	serves = get_serves(title)
	
	# Update the title
	if scale is not None:
		title += " [Scaled by x%.1f]"%(float(scale))
	elif serve is not None and serves is not None:
		title += " [Scaled to serve %d]"%(float(serve))
	
	# Modify the value of serves if it is not set to match the requested number of
	# servings (so the ammounts aren't changed) or to one if the scale is
	# required.
	serves = serves if serves is not None else serve if serve is not None else 1
	
	# The description should be the seocnd (if present)
	description = "\n\n".join(sections[1:-2]) if len(sections) >= 4 else ""
	
	# The last two sections contain the ingredients and recipe
	eng_ingredients, eng_recipe = sections[-2:]
	
	# Get the ingredients and scale them as required
	ingredients = get_ingredients(eng_ingredients)
	def alter_ammonts(ingredient):
		if ingredient.components != []:
			# If this is a substance, try on the subcomponents
			map(alter_ammonts, ingredient.components)
		else:
			try:
				ingredient.quantity.ammount = (
					ingredient.quantity.ammount * float(scale)
					if scale is not None else
					(ingredient.quantity.ammount/float(serves)) * float(serve)
					if serve is not None else
					ingredient.quantity.ammount # Do nothing
				)
			except AttributeError:
				# This is not an ingredient, do nothing
				pass
	map(alter_ammonts, ingredients.values())
	
	# Generate the recipe from the english
	substances = get_recipe(ingredients, eng_recipe)
	
	return title, description, substances

