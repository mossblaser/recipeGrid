from model import Substance, Quantity, Ingredient
from view import results_to_html

from generator import generate

if __name__=="__main__":
	recipe = generate(
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
	
	print recipe
	
	# Produce a table showing how I can produce both!
	html = results_to_html(recipe)
	print html
	
	open("out.html","w").write(html)
