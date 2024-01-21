# By Using Regular Expression
import re


def validate_ip_regex(ip_address):
    match = re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip_address)

    if not bool(match):
        print(f"The IP address {ip_address} is not valid")
        return False

    bytes = ip_address.split(".")

    for ip_byte in bytes:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"The IP address {ip_address} is not valid")
            return False
    print(f"The IP address {ip_address} is valid")
    return True


validate_ip_regex('172.10.10.111')


# By Using Class Object
class Solution(object):
    def IsValid_IPV4_IPAddress(self, IP):
        def IsIPV4(s):
            try: return str(int(s)) == s and 0 <= int(s) <= 255
            except: return False

        if IP.count(".") == 3 and all(IsIPV4(i) for i in IP.split(".")):
            return IP+ " is a valid IPV4 IP Address"
        return IP+ ' is not a valid IPV4 IP Address'
ob = Solution()
print(ob.IsValid_IPV4_IPAddress("172.30.12.10"))


class Solution(object):
    def Validate_IP_Address(self, IP):
        def IsIPV4(s):
            try:
                return 0 <= int(s) <= 255
            except:
                return False

        if IP.count(".") == 3 and all(IsIPV4(i) for i in IP.split(".")):
            return "Valid IP Address"
        return "Invalid IP Address"


ob = Solution()
print(ob.Validate_IP_Address("172.101.101.01"))


class Solution(object):
    def IsValid_IPV4_IPAddress(self, IP):
        def IsIPV4(s):
            try:
                return s.isdigit() and 0 <= int(s) <= 255
            except:
                return False

        if IP.count(".") == 3 and all(IsIPV4(i) for i in IP.split(".")):
            return IP + " is a valid IPV4 IP Address"
        return IP + ' is not a valid IPV4 IP Address'

ob = Solution()
print(ob.IsValid_IPV4_IPAddress("172.30.12.10"))

class Solution(object):
   def IsValid_IPV6_IPAddress(self, IPv6):
      """
      :type IP: str
      :rtype: str
      """
      def isIPv6(s):
         if len(s) > 4:
            return False
         try: return int(s, 16) >= 0 and s[0] != '-'
         except:
            return False
      if IPv6.count(":") == 7 and all(isIPv6(i) for i in IPv6.split(":")):
         return IPv6+ " is a valid IPv6 IP Address"
      return IPv6+ " is not a valid IPv6 IP Address"


ob = Solution()
print(ob.IsValid_IPV6_IPAddress("2001::10"))

# Validating an IP address using the ipaddress() module


import ipaddress

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} is valid. The object returned is {}".format(address, ip))
    except ValueError:
        print("IP address {} is not valid".format(address))


validate_ip_address("10.10.101.10")


def validate_ip(ip_address):
    try:
        ipaddress.IPv4Address(ip_address)
        print(f"{ip_address} is a valid IPv4 address")
    except ValueError:
        print(f"{ip_address} is not a valid IPv4 address")


validate_ip("172.10.1.264")


# How to Check If an IP is of Type IPv4 or IPv6 Using Python


def get_ip_type(address):
    try:
        ip = ipaddress.ip_address(address)
        if isinstance(ip, ipaddress.IPv4Address):
            print("{} is an IPv4 address".format(address))
        elif isinstance(ip, ipaddress.IPv6Address):
            print("{} is an IPv6 address".format(address))
    except ValueError:
        print("{} is an invalid IP address".format(address))


