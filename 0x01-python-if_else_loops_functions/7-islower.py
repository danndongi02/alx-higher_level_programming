#!/usr/bin/python3
"""Check if a character is lowerstring"""


def islower(c):
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
