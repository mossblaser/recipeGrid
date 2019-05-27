from setuptools import setup, find_packages

setup(
	name = "recipeGrid",
	version = "0.1",
	packages = find_packages(),
	scripts = ["scripts/recipeGrid",
	           "scripts/recipeGrid_dir",
	           "scripts/icing"],
)
