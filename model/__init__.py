#!/usr/bin/python


class Substance(object):
	
	def __init__(self, description):
		if description is not None:
			self.description = description
		
		self.components = []
	
	
	def made_from(self, *components):
		self.components.extend(components)
	
	
	def __len__(self):
		return sum(len(c) for c in self.components)
	
	
	def __str__(self):
		return self.description



class Quantity(object):
	
	def __init__(self, ammount, unit = ""):
		self.ammount = float(ammount)
		self.unit = unit
	
	
	def __str__(self):
		return ("%.1f %s"%(self.ammount, self.unit)).strip()



class Ingredient(Substance):
	
	def __init__(self, quantity, name):
		Substance.__init__(self, None)
		
		self.quantity = quantity
		self.name = name
	
	
	@property
	def description(self):
		return "%s of %s"%(str(self.quantity), self.name)
	
	
	def __len__(self):
		return 1;


