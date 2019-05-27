import re

serves_regex = re.compile("(serves?|for|makes) (?P<num>\d+)")

def interpret(english):
	match = serves_regex.search(english)
	return int(match.group("num")) if match is not None else None
