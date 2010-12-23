from view import results_to_html

from generator import parse_recipe_file

if __name__=="__main__":
	import sys
	english = open(sys.argv[1], "r").read()
	
	title, description, recipe = parse_recipe_file(english)
	
	# Produce a table showing how I can produce both!
	html = results_to_html(recipe)
	html = "<h1>%s</h1><p>%s</p>%s"%(
		title,
		"</p><p>".join(description.split("\n\n")),
		html
	)
	print html
