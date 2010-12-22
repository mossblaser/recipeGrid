#!/usr/bin/python

import re

from generator.ingredients import interpret as ingredient_interpret
from generator.steps import interpret as step_interpret


# Split a list of ingredients in english into individual ingredients
def split_eng_ingredients(english):
	return filter(None, (s.strip() for s in
	                     english.split("\n")))


# Given a list of ingredients (in english) produce a model of the ingredients
# list (with preperation steps added). A dictionary mapping the ingredient name
# to the model is returned.
def get_ingredients(english):
	# The ingredients dictionary should contain Substance objects refrenced by the
	# engish of their root substance name.
	ingredients = dict(map(ingredient_interpret,
	                       split_eng_ingredients(english)))
	
	return ingredients


def generate(english):
	# The ingredients list is at the top and the recipe is after the first empty
	# line.
	empty_line = re.compile("^\s*$", re.MULTILINE)
	eng_ingredients, eng_recipe = empty_line.split(english.strip(), 1)
	
	ingredients = get_ingredients(eng_ingredients)
	
	substances = step_interpret(ingredients, eng_recipe)
	
	return substances



if __name__=="__main__":
	print generate(
	"""
	2 tablespoons butter
	1 onion, chopped
	2 large parsnips, peeled and chopped into 1 cm cubes
	1 clove garlic, finely chopped
	750ml boiling water
	1 stock cube
	2 teaspoons curry powder
	100ml double cream
	Salt and pepper
	
	season(stir in(blend (simmer(
		fry(fry(melt(butter), onion), large parsnips, garlic, curry poweder),
		mix(boil(water), stock cube)
	)), creme), salt and pepper)
	""")
