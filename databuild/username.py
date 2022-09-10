import random
import requests

from .data import NOUNS_DICTIONARY, ADJECTIVES_DICTIONARY, WORD_DICTIONARY

#def __fetch_usernames():
#	r = requests.get('https://raw.githubusercontent.com/jeanphorn/wordlist/master/usernames.txt')
#	r.raise_for_status()
#	return [l for l in r.text.split('\n') if len(l) > 2]
# usernames = __fetch_usernames()

class Username:
	HYPHEN_CHANCE = 10
	UNDERSCORE_CHANCE = 25
	NUMERIC_CHANCE = 50
	CAPITALIZATION_CHANCE = 80
	
	""" Generate a random username """
	def __init__(self):
		pass
		
	def __roll(self):
		d = {}
		d['HYPHEN'] = random.randrange(100) < self.HYPHEN_CHANCE
		d['UNDERSCORE'] = False if d['HYPHEN'] else random.randrange(100) < self.UNDERSCORE_CHANCE
		d['NUMERIC'] = random.randrange(100) < self.NUMERIC_CHANCE
		d['CAPITALIZATION'] = random.randrange(100) < self.CAPITALIZATION_CHANCE
		return d
		
	def __random(self):
		adjective = random.choice(ADJECTIVES_DICTIONARY).word
		noun = random.choice(NOUNS_DICTIONARY).word
		num = str(random.randrange(10000))
		
		_roll = self.__roll()
		
		if _roll['HYPHEN']:
			separator = '-'
		elif _roll['UNDERSCORE']:
			separator = '_'
		else:
			separator = ''
		
		if _roll['NUMERIC']:
			numeric = num
		else:
			numeric = ''
		
		segs = [adjective, noun, numeric]
		if _roll['CAPITALIZATION']:
			segs = [s.capitalize() for s in segs]
		
		return separator.join([ f for f in segs if f ])
		
	def generate(self, count=0):
		if count == 0:
			return self.__random()
		else:
			return [self.__random() for _ in range(count)]
