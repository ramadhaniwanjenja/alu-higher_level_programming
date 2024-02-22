#!/usr/bin/env python3

custom_pow = __import__('11-pow').pow

print(custom_pow(2, 2))
print(custom_pow(98, 2))
print(custom_pow(98, 0))
print(custom_pow(100, -2))
print(custom_pow(-4, 5))
