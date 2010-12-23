Recipe Grid
===========

A tool for generating tables similar to those on www.cookingforengineers.com to
use as recipies. Also facilitates scaling of quantities. This project was a
quick afternoon hack and so the code is in major need of refactoring but asside
from that it works quite well.

Usage
-----

The program takes an argument of a recipe file in the format discussed below (or
uses standard input if none is provided) and produces HTML on the standard
output.

It also takes a `--serve N` argument (`-s N`) which will scale the ingredients
to make them serve `N` people. This only works when the number of people the
recipe serves is known. If it is not specifed in the recipe then the ammounts
won't change. You also use `--scale N` (`-S N`) which scales the ammounts
by a factor of `N`. This will work on all recipes.


Input Format
------------

One of the novel features of the tool is the input language is fairly flexible.
It started life as an ill-fated attempt to be an automated translator for
standard recipe formats. It has since been demoted to only parsing standard
ingredients lists and providing a really simple and easy syntax for the recpie
itself.

Sections of the file are seperated by a single empty line.

Title, Servings and Description
```````````````````````````````

The first section contains the title. The title may contain serving information
(for example, serves 4). If provided, this allows the system to scale the recipe
by number of servings rather than just by some arbitary factor.

Any number of description sections may now be included which will be presented
as paragraphs of preamble in the output.

Ingredients List
````````````````

The next section contains a list of ingredients, one per line. These may be
formatted as normal. For example::

	2 tablespoons butter
	1 1/4 oz digestives
	Salt and pepper
	1 onion, chopped

This would be parsed as you'd expect (even the fraction). The onion has an
instruction for preperation after a comma. The parser interprets this to be a
stage in the cooking and automatically inserts it into the final instructions.

Ingredients can be refrenced in the recpie by just their name (e.g. `onion` or
`Salt and pepper`).

If you don't specify an ingredient in this list it will not be scaled when the
recipe's quantites are automatically scaled.

Recipe
``````

The next section contains the recipe itself. It consists of a comma-seperated
list of nested instructions. For example::

	pour into(
		heat(
			dilute(open(can of soup), water))),
	bake(garlic bread)

In this recipe, two things are made, the garlic bread (which is baked) and the
canned tomato soup (which was opened, diluted with water, heated and then poured
into a bowl).

Steps are simply nested in the form::

	step description (list, of, components, used)

These steps can be nested arbitarily deep. You should refer to your ingredients
at the deepest levels.

recipeGrid_dir
==============

A tool which takes two arguments, a source directory and destination directory.
The destination directory tree is emptied (so don't put anything important
there) and then filled with HTML versions of the recipies in the first
directory.

icing
=====

Takes a template directory (one is included in `icing_template`) and a directory
produced by `recipeGrid_dir` and prettifies it.
