#!/usr/bin/python

import re
import os, shutil, os.path

static_resources = [
	"fonts/ajpr.otf",
	"fonts/ajpb.otf",
	"fonts/ajpi.otf",
	"images/bg.png",
	"images/bosspot.png",
	"images/twiddle.png",
	"style.css",
]


def setup_root(directory):
	for resource in static_resources:
		source = os.path.join("./templates", resource)
		target = os.path.join(directory, resource)
		target_dir = os.path.dirname(target)
		
		try:
			os.mkdir(target_dir)
		except OSError:
			# The path already exists, problem solved!
			pass
		
		try:
			shutil.copyfile(source, target)
		except OSError:
			# The file already exists, problem solved!
			pass
	
	serving_re = re.compile("^serves(\d+)$")
	
	servings =  map((lambda m: int(m.group(1))),
	                filter(None,
	                       map((lambda d: serving_re.match(d)),
	                           os.listdir(directory))))
	servings.sort()
	
	template  = open(os.path.join("./templates", "index.html"), "r").read()
	index_filename = os.path.join(directory, "index.html")
	
	pre, list_elem, post = template.split("!!")
	
	html = "%s%s%s"%(
		pre,
		"".join(list_elem.replace("#target", "serves%d"%serving).replace(
		                          "#label", str(serving)) for serving in servings),
		post
	)
	
	open(index_filename, "w").write(html)
	
	return [os.path.join(directory, "serves%d"%s) for s in servings]



def theme_page(page):
	body = open(page, "r").read()
	
	pre, post = open(os.path.join("./templates", "recipe.html"),
	                 "r").read().split("!!")
	
	open(page, "w").write(pre + body + post)


def camel_case_to_sentence_case(string):
	string, _ , _ = string.partition(".")
	spaced = re.sub("([A-Z])", r" \1", string)
	words = filter(None, spaced.split())
	
	for i, word in enumerate(words):
		words[i] = word[0].upper() + word[1:]
	
	return " ".join(words)



def setup_directory(directory):
	subdirectories = filter((lambda x: os.path.basename(x) != "index.html"),
	                        [os.path.join(directory, d)
	                         for d in os.listdir(directory)])
	for path in subdirectories:
		if os.path.isdir(path):
			setup_directory(path)
		else:
			theme_page(path)
	
	subdirectory_titles = map(camel_case_to_sentence_case,
	                          map(os.path.basename, subdirectories))
	
	template = open(os.path.join("./templates", "categories.html"), "r").read()
	pre, link, post = template.split("!!")
	
	html = "%s%s%s"%(
		pre,
		"".join(link.replace("#link", os.path.basename(location)).replace("#label", title)
		        for location, title in zip(subdirectories, subdirectory_titles)),
		post
	)
	
	open(os.path.join(directory, "index.html"), "w").write(html)



if __name__=="__main__":
	import sys
	directory = sys.argv[1]
	
	subdirectories = setup_root(directory)
	for directory in subdirectories:
		setup_directory(directory)
