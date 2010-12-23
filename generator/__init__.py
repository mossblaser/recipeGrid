#!/usr/bin/python

import re

from generator.ingredients import interpret as get_ingredients
from generator.steps       import interpret as get_recipe



def parse_recipe_file(english):
	sections = filter(None, map(str.strip, english.strip().split("\n\n")))
	assert(len(sections) >= 3)
	
	# The title should be the first section
	title = sections[0].strip()
	
	# The description should be the seocnd (if present)
	description = "\n\n".join(sections[1:-2]) if len(sections) >= 4 else ""
	
	# The last two sections contain the ingredients and recipe
	eng_ingredients, eng_recipe = sections[-2:]
	
	# Generate the recipe from the english
	ingredients = get_ingredients(eng_ingredients)
	substances = get_recipe(ingredients, eng_recipe)
	
	return title, description, substances

