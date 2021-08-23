# Created by Prof. Nicolosi & Dominick DiMaggio for CS 115 at Stevens Institute of Technology, 2020

##########################################
# Name: Benjamin Griepp
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
##########################################
from math import floor

######################################################################
# Task 1: Given an 8-digit decimal number representing the date,
#         calculate the day of the week
# Input: 8-digit decimal number in the format of YYYYMMDD
# Saturday: 0, Sunday: 1... Friday: 6  
# Hint: Look at Zeller's congruence.
#       The floor() function may be helpful. (Ex: floor(5.5) = 5)

def getWeekday(timestamp):
    year = floor(timestamp / 10000)
    month = floor(timestamp/ 100) % 100
    if month == 1 or month == 2:
        month += 12
        year -= 1
    day = timestamp % 100
    h = floor((day + ( (13 * (month + 1)) /5 ) + year + floor(year/4) - floor(year/100) + floor(year/400)) % 7)
    return h

######################################################################
# Task 2: For this task, you will create an encoder and decoder
#         for a Caesar cipher using the map function.
# You may find this website helpful:
# https://cryptii.com/pipes/caesar-cipher

######################################################################
# This provided helper function may be useful
# Input: List of ASCII values (Ex: [72, 69, 76, 76, 79])
# Output: String (Ex. 'HELLO')     ('H   E   L   L   O')
def asciiToString(asciiList):
    return ''.join(map(chr, asciiList))

def stringToAscii(str):
    strlist = list(str)
    return list(map(ord, strlist))
# made my own function hope thats cool

######################################################################
# Encoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. HELLO WORLD, 3)
# Output: An encoded string            (Ex. KHOOR ZRUOG)
# Hint: The ord() function converts single-character strings to ASCII
def caesarEncoder(str, shift):
    asciiIn = stringToAscii(str)
    asciiShift = map(lambda a: a + shift - 26 if a + shift >= 90 else a + shift, asciiIn)
    return asciiToString(asciiShift)

######################################################################
# Decoder
# Input: A string value with all capital letters (leave everything
#        else as-is) and a shift value (Ex. KHOOR ZRUOG, 3)
# Output: A decoded string             (Ex. HELLO WORLD)
# Hint: The chr() function converts ASCII to a single-character string
def caesarDecoder(str, shift):
    asciiIn = stringToAscii(str)
    asciiShift = map(lambda a: a - shift + 26 if a - shift <= 64 else a - shift, asciiIn)
    return asciiToString(asciiShift)

print(caesarDecoder("abcd", 2))