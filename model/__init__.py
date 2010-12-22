#!/usr/bin/python


class Substance(object):
	
	def __init__(self, description, *components):
		if description is not None:
			self.description = description
		
		self.components = list(components)
	
	
	def made_from(self, *components):
		self.components.extend(components)
	
	
	def __len__(self):
		return sum(len(c) for c in self.components)
	
	
	def __str__(self):
		return self.description
	
	
	def __repr__(self):
		return "Substance(%s%s)"%(
			repr(self.description),
			(", " + ", ".join(repr(c) for c in self.components))
			 if self.components != [] else ""
		)



class Quantity(object):
	
	def __init__(self, ammount, unit = ""):
		self.ammount = float(ammount)
		self.unit = unit
	
	
	def __str__(self):
		return ("%.1f %s"%(self.ammount, self.unit)).strip()
	
	
	def __repr__(self):
		return "Quantity(%s, %s)"%(
			repr(self.ammount),
			repr(self.unit)
		)



class Ingredient(Substance):
	
	def __init__(self, quantity, name):
		Substance.__init__(self, None)
		
		self.quantity = quantity
		self.name = name
	
	
	@property
	def description(self):
		if self.quantity.unit == "" and self.quantity.ammount == 1:
			return self.name
		else:
			return "%s of %s"%(str(self.quantity), self.name)
	
	
	def __len__(self):
		return 1;
	
	
	def __repr__(self):
		return "Ingredient(%s, %s)"%(
			repr(self.quantity),
			repr(self.name)
		)


