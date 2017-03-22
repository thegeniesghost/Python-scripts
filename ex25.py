def break_words(stuff):
	"""This function will break up words for us."""
	words = stuff.split(' ')
	return stuff
	
def sort_words(stuff):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(stuff):
	"""Prints the forst word after poping it off."""
	word = words.pop(0)
	print word
	
def print_last_word(stuff):
	"""Prints the last word after poping it off."""
	word = words.pop(-1)
	print word
	
def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last(sentence):
	"""Prints the last and first words of a sentence."""
	word = break_words(sentence)
	return