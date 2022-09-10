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

## To-do 
- Add generator for Text - Core
- Add generator for Lorem Ipsum - Core 
- Add generator for Time
- Add generator for Dates
- Add generator for Urls
- Add generator for Email Address
- Add generator for Email Subject / Title
- Add generator for Email Body text
- Add generator for Phone numbers
- Add generator for Mailing addresses
- Add generator for Geolocation Coordinates
- Add graphable data
- Add data dumps
- Support assorted types of data dumps - *Plaintext, JSON, CSV, HTML, etc*.
