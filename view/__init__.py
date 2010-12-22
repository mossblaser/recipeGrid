#!/usr/bin/python

from pprint import pprint


class Cell(object):
	
	def __init__(self, text, height, width = 1):
		self.text = text
		self.height = height
		self.width = width
	
	
	@property
	def html(self):
		return '<td rowspan="%d" colspan="%d">%s</td>'%(
			self.height, self.width, self.text
		)
	
	
	def __repr__(self):
		return "Cell(%s, %s, %s)"%(
			repr(self.text), repr(self.height), repr(self.width)
		)



class Row(list):
	
	@property
	def html(self):
		cell_html = ""
		
		for cell in self:
			cell_html += cell.html
		
		return "<tr>%s</tr>"%cell_html
	
	def __repr__(self):
		return "Row(%s)"%list.__repr__(self)
	
	
	def width(self, rows_above):
		# The width of a row is the width of all its columns plus the width of any
		# columns which extend down from another row
		return (sum(c.width for c in self)
		        + sum(r.width_carried(len(rows_above) - i)
		              for i, r in enumerate(rows_above)))
	
	
	def width_carried(self, num_rows):
		# Get the width carried from this row num_rows below it (e.g. where a cell
		# spans several rows)
		return sum(c.width for c in
		           filter((lambda c: c.height > num_rows), self))


class Table(list):
	
	@property
	def html(self):
		row_html = ""
		
		for row in self:
			row_html += row.html
		
		return "<table border=1>%s</table>"%row_html



def expand_rows(rows):
	# Extend all rows such that they span the same number of columns
	max_width = max(rows[i].width(rows[:i]) for i in range(len(rows)))
	for i, row in enumerate(rows):
		width = row.width(rows[:i])
		# Expand the last element on the row to fill any extra columns
		row[-1].width += max_width - width
	
	return rows

def get_rows(substance):
	if substance.components == []:
		# This is an ingredient, e.g. the start of a row so return one row
		# containing just this item.
		return [Row([Cell(str(substance), 1)])]
	else:
		# This substance contains numerous sub-components, each of which must
		# populate at least one row. Get these rows by recursing over the sub
		# components and getting their rows.
		rows = list(sum((get_rows(c) for c in substance.components), Row()))
		
		# Expand all rows so that they are the same number of columns
		rows = expand_rows(rows)
		
		# Add this substance as a cell at the end of all the rows
		rows[0].append(Cell(str(substance), len(rows)))
		
		return rows



"""
Draw a table containing the tree leading up to the resuts given in the list.
"""
def results_to_html(results):
	# Get the table for all results
	rows = list(sum((get_rows(r) for r in results), Row()))
	
	# De-ragedize the end
	rows = expand_rows(rows)
	
	table = Table(rows)
	return table.html
