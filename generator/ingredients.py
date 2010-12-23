#!/usr/bin/python

# Code for extracting a list of ingredients from the input

import re

from model import Ingredient, Quantity, Substance


# A regex which splits up an ingredient from the preperation for that engredient
split_ingredient_preperation = re.compile(
	r"(?P<ingredient>[^,]+)(, ?(?P<preperation>.*))?")


# Match a quantity
quantity_regex = (
	r"(((?P<frac_whole>\d+)\s+)?(?P<frac_top>\d+)\s*/\s*(?P<frac_btm>\d+)"
	+ r"|(?P<decimal>\d+(.\d+)?))"
)


# Table of possible unit abbreviations to a single version. For future, more
# advanced use.
units = {
	"g"     : ["g", "gram", "grams"],
	"kg"    : ["kg", "kilo", "kilos", "kilogram", "kilograms"],
	"cup"   : ["cup", "cups"],
	"l"     : ["l", "litre"],
	"ml"    : ["ml", "mill", "mills", "millilieters", "millilieter"],
	"lb"    : ["lb", "lbs", "pound", "pounds"],
	"oz"    : ["oz", "ozs", "ounce", "ounces"],
	"tsp"   : ["tsp", "tsps", "teaspoons", "teaspoon", "tea spoon", "tea spoons"],
	"tbsp"  : ["tbsp", "tbsps", "tablespoon", "tablespoons", "table spoon", "table spoons"],
	"clove" : ["clove", "cloves"],
	"pint"  : ["pint", "pints"],
	"can"   : ["can"],
}

unit_regex = "(%s)"%("|".join(sum(units.itervalues(), [])))

# A regex which matches joining phrases between ammounts/units and the
# ingredient
join_regex = "(%s)"%("|".join([
	"of"
]))


# Split the quantities from an ingredient
split_ingredient_quantities = re.compile(
	"\s*((?P<quantity>%s)"%quantity_regex
	+ "\s*(?P<unit>%s)?"%unit_regex
	+ "(\s+%s)?"%join_regex
	+ r"\s+)?(?P<ingredient>.+)", re.IGNORECASE)


# Interpret just the ingredient pert of of the english ingredient line
def interpret_ingredient(english):
	match = split_ingredient_quantities.match(english)
	assert(match is not None)
	
	eng_quantity = match.group("quantity")
	
	quantity = 1
	if eng_quantity is not None:
		if match.group("decimal"):
			quantity = float(match.group("decimal"))
		elif match.group("frac_top"):
			if match.group("frac_whole"):
				quantity = int(match.group("frac_whole"))
			else:
				quantity = 0
			
			quantity += float(match.group("frac_top")) / float(match.group("frac_btm"))
	
	unit = match.group("unit") or ""
	
	ingredient = match.group("ingredient")
	
	return ingredient, Ingredient(Quantity(quantity, unit), ingredient)



# Split a list of ingredients in english into individual ingredients
def split_eng_ingredients(english):
	return filter(None, (s.strip() for s in
	                     english.split("\n")))




# Interpret an ingredient in english and return a tuple with the ingredient name
# and a Substance object.
def interpret_single(english):
	match = split_ingredient_preperation.match(english)
	assert(match is not None)
	
	# Extract the preperation step from the ingredient
	eng_ingredient = match.group("ingredient")
	eng_prep = match.group("preperation")
	
	name, ingredient = interpret_ingredient(eng_ingredient)
	
	if eng_prep is not None:
		return name, Substance(eng_prep, ingredient)
	else:
		return name, ingredient



# Given a list of ingredients (in english) produce a model of the ingredients

# list (with preperation steps added). A dictionary mapping the ingredient name
# to the model is returned.
def interpret(english):
	# The ingredients dictionary should contain Substance objects refrenced by the
	# engish of their root substance name.
	ingredients = dict(map(interpret_single,
	                       split_eng_ingredients(english)))
	
	return ingredients
