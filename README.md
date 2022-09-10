# Databuild
A Python3 package library for generating randomized data for a wide range of data structures or scenarios.

## Structure
- **databuild\\** - Core
  - PACKAGE CONTENTS
    - data (package)
    - ip_address
    - ipv4_address
    - ipv6_address
    - mac_address
    - networking (package)
    - username
    - databuild.mac_address.MacAddress
    - databuild.username.Username
    - databuild.ip_address.IPGenerator
    - databuild.ip_address.IpAddress
    - class IpAddress(IPGenerator)
      - generate(self, count:int = 0)
    - class MacAddress(builtins.object)
      - generate(self, count:int = 0)
    - class Username(builtins.object)
      - generate(self, count:int = 0)
