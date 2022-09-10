from .nouns import NOUNS
from .adjectives import ADJECTIVES

__all__ = [ 'NOUNS', 'NOUNS_DICTIONARY', 'ADJECTIVES', 'ADJECTIVES_DICTIONARY', 
            'WORD_DICTIONARY', 'Word' ]

class Word (object):
    def __init__(self, word:str, **kw):
        self.word = word
        for k,v in kw.items():
            setattr(self, k, v)
        
    def __str__(self):
        return self.word
        
    def __repr__(self):
        return self.word
        
    def __eq__(self, other):
        return self.word == other.word
        
    def __hash__(self):
        return hash(self.word)
        
    def get(self, attr:str, val:str, key=None):
        value = getattr(self, attr, None)
        if hasattr(key, '__call__'):
            return key(value, val)
        return value

NOUNS_DICTIONARY = [Word(w, frequency=f, types=t) for w, f, t in NOUNS]
ADJECTIVES_DICTIONARY = [Word(w, frequency=f, types=t) for w, f, t in ADJECTIVES]
WORD_DICTIONARY = list(set(NOUNS_DICTIONARY + ADJECTIVES_DICTIONARY))
