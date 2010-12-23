#!/usr/bin/python

from generator import parse_recipe_file
from view      import results_to_table


def parse_args():
	import argparse
	parser = argparse.ArgumentParser(
		description = "Translate a recipe description into a table."
	)
	
	parser.add_argument("filename", type=str, nargs = "?",
	                    default = "/dev/stdin",
	                    help = "The filename to read the recipe from (or stdin if not supplied).")
	
	parser.add_argument("output", type=str, nargs = "?",
	                    default = "/dev/stdout",
	                    help = "The filename to write the html to (or stdout if not supplied).")
	
	group = parser.add_mutually_exclusive_group()
	
	group.add_argument("-s", "--serve", type=int,
	                   default = None,
	                   dest = "serve",
	                   metavar = "N",
	                   help = "Scale quantities to serve N people.")
	
	group.add_argument("-S", "--scale", type=float,
	                   default = None,
	                   dest = "scale",
	                   metavar = "N",
	                   help = "Scale quantities by a factor of N.")
	
	return parser.parse_args()



if __name__=="__main__":
	args = parse_args()
	
	english = open(args.filename, "r").read()
	
	title, description, recipe = parse_recipe_file(english,
	                                               serve = args.serve,
	                                               scale = args.scale)
	
	# Produce a table showing how I can produce both!
	html = "<h1>%s</h1><p>%s</p>%s"%(
		title,
		"</p><p>".join(description.split("\n\n")),
		results_to_table(recipe).html
	)
	
	open(args.output, "w").write(html)
