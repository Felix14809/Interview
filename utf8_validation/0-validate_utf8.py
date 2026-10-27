#!/usr/bin/python3

"""This program check wether the input list of data is UTF-8 valid"""


def validUTF8(data):
    """This is doing the checks with byte shifting"""
    continuations = 0

    for number in data:
        byte = number & 0xFF
        if continuations == 0:
            if byte >> 7 == 0b0:
                continuations = 0
            elif byte >> 5 == 0b110:
                continuations = 1
            elif byte >> 4 == 0b1110:
                continuations = 2
            elif byte >> 3 == 0b11110:
                continuations = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                continuations -= 1
            else:
                return False
    if continuations == 0:
        return True
    else:
        return None
