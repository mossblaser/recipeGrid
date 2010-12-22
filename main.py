from model import Substance, Quantity, Ingredient
from view import results_to_html

if __name__=="__main__":
	sugar = Ingredient(Quantity(0.5, "cups"), "sugar")
	butter = Ingredient(Quantity(0.5, "cups"), "butter")
	cocoa = Ingredient(Quantity(6, "tsp"), "cocoa powder")
	syrup = Ingredient(Quantity(2, "tbsp"), "golden syrup")
	digestives = Ingredient(Quantity(450, "g"), "digestives")
	chocolate = Ingredient(Quantity(1, "bar"), "chocolate")
	
	sauce = Substance("mix in pan, low heat")
	sauce.made_from(sugar, butter, cocoa, syrup)
	
	base = Substance("mix")
	base.made_from(sauce, digestives)
	
	melted_choc = Substance("melt")
	melted_choc.made_from(chocolate)
	
	tiffin = Substance("cover")
	tiffin.made_from(base, melted_choc)
	
	foo = Ingredient(Quantity(1), "foo")
	bar = Ingredient(Quantity(1), "bar")
	
	jubulated = Substance("jubulate")
	jubulated.made_from(bar)
	
	stuff = Substance("mix")
	stuff.made_from(foo, jubulated)
	
	html = results_to_html([tiffin, stuff])
	print html
	
	open("out.html","w").write(html)
