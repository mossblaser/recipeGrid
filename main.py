from view import results_to_table

from generator import parse_recipe_file

if __name__=="__main__":
	import sys
	english = open(sys.argv[1], "r").read()
	
	title, description, recipe = parse_recipe_file(english)
	
	# Produce a table showing how I can produce both!
	html = "<h1>%s</h1><p>%s</p>%s"%(
		title,
		"</p><p>".join(description.split("\n\n")),
		results_to_table(recipe).html
	)
	print html
