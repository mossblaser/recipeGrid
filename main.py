from model import Substance, Quantity, Ingredient
from view import results_to_html

from generator import generate

if __name__=="__main__":
	recipe = generate(
	"""
	6 tsp cocoa powder
	2 tbsp golden syrup
	1/2 cup butter
	1/2 cup sugar
	16oz digestives
	bar of chocolate
	
	eat(
		hide(
			cover(
				mix(
					heat until bubbling (cocoa powder, golden syrup, butter, sugar)
					crush(digestives))
				melt(bar of chocolate))))
	""")
	
	print recipe
	
	# Produce a table showing how I can produce both!
	html = results_to_html(recipe)
	print html
	
	open("out.html","w").write(html)
