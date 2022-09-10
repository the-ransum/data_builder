from random import randint
import ipaddress


class IPGenerator:
    """ Binds the generate method to the class with the given name """
    def __init__(self, modname:str, max:int):
        _key = '%sAddress' % modname
        if not hasattr(ipaddress, _key):
            raise AttributeError("ipaddress module does not have %s" % _key)
        
        self._mod = getattr(ipaddress, _key)
        self._MAX = self._mod._ALL_ONES
        if max is not None:
            if type(max) is int:
                self._MAX = max
            else:
                raise TypeError("MAX must be an integer")
        
    def __random(self):
        return self._mod._string_from_ip_int(randint(0, self._MAX))
        
    def generate(self, count:int=0):
        if count == 0:
            return self.__random()
        else:
            return [self.__random() for _ in range(count)]


class IpAddress (IPGenerator):
    """ Generate a random IP address """
    def __init__(self):
        self.ipv4 = IPGenerator('IPv4', None)
        self.ipv6 = IPGenerator('IPv6', None)

