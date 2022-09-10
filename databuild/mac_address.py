import random

# MAC Address Standards: https://standards-oui.ieee.org/oui/oui.txt

class MacAddress:
    _BASE16_CHARS = [*"0123456789abcdef"]
    _UNICAST_LOCAL = ["2", "6", "a", "e"]
    
    def __init__(self):
        pass
        
    @staticmethod
    def _strip_sep(mac:str):
        """ Strips the seperator from the mac address """
        return mac.translate(str.maketrans("", "", ":-."))
        
    def __gen_char_seq(self):
        """ Generate a sequence of characters base-16 char MAC address. """
        seq = [random.choice(self._BASE16_CHARS) for _ in range(16)]
        seq[1] = random.choice(self._UNICAST_LOCAL)
        return seq
        
    def __set_sep(self, mac, sep=':'):
        segs = []
        if type(mac) is str:
            segs = self._strip_sep(mac)
        elif type(mac) is list:
            segs = mac
        else:
            raise TypeError("mac must be a string or list")
        
        couples = [''.join(segs[i:i+2]) for i in range(0, 16, 2)]
        return sep.join(couples)
        
    def __random(self, partial:str=None, sep=':'):
        mac = self.__set_sep(self.__gen_char_seq(), sep)
        if partial is not None:
            _mac = mac[::-1]
            partial = self._strip_sep(partial)
            mac = self.__set_sep([*partial, *_mac[len(partial):]][:16], sep)
        
        return mac
        
    def generate(self, count:int=0, partial:str=None, sep=':'):
        macs = None
        if count == 0:
            macs = self.__random(partial=partial, sep=sep)
        else:
            macs = [self.__random(partial=partial, sep=sep) for _ in range(count)]
        return macs
