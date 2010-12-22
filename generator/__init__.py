#!/usr/bin/python

import re

from generator.ingredients import interpret as ingredient_interpret


# Split a list of ingredients in english into individual ingredients
def split_eng_ingredients(english):
	return filter(None, (s.strip() for s in
	                     english.split("\n")))


# Given a list of ingredients (in english) produce a model of the ingredients
# list (with preperation steps added). A dictionary mapping the ingredient name
# to the model is returned.
def generate_ingredients(english):
	# The ingredients dictionary should contain Substance objects refrenced by the
	# engish of their root substance name.
	ingredients = dict(map(ingredient_interpret,
	                       split_eng_ingredients(english)))
	
	return ingredients



if __name__=="__main__":
	print generate_ingredients(
	"""
	2 tablespoons butter
	1 onion, chopped
	2 large parsnips, peeled and chopped into 1 cm cubes
	1 clove garlic, finely chopped
	1 1/3 l boiling water
	1 stock cube
	2 teaspoons curry powder
	100ml double cream
	Salt and pepper
	""")
