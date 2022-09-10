# Path: databuild\__init__.py

from .ip_address import IpAddress
from .mac_address import MacAddress
from .username import Username

_ip_address = IpAddress()
ipv4_address = _ip_address.ipv4
ipv6_address = _ip_address.ipv6
ip_address = ipv4_address

mac_address = MacAddress()

username = Username()


__all__ = [ "IpAddress", "ipv4_address", "ipv6_address", "ip_address", 
            "MacAddress", "mac_address", "Username", "username", ]
