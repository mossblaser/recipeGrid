from distutils.core import setup

setup(
	name = "recipeGrid",
	version = "0.1",
	package_dir = {"recipeGrid" : "src"},
	packages = ["recipeGrid",
	            "recipeGrid.model",
	            "recipeGrid.view",
	            "recipeGrid.generator"],
	scripts = ["scripts/recipeGrid",
	           "scripts/recipeGrid_dir",
	           "scripts/icing"],
)
