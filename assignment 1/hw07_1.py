#!/usr/bin/env python

"""
This module defines a method, IsValidIdentifier, which takes a string
as an argument and determines whether the string is a valid Python
identifiers. It will reject any string which does not begin with
either an alphabetic character or an underscore, or which contains
any characters which are not alphanumeric or an underscore.
"""

import keyword
import re

DATA = ('x', '_x', '2x', 'x,y', 'yield', 'is_this_good')

def IsValidIdentifier(string):

    if keyword.iskeyword(string):
        return (False, "Invalid: this is a keyword!")
    elif not re.match('^\w|\_', string):
        return (False, "Invalid: first symbol must be alphabetic or underscore.")

    for i in range(1, len(string)):
        if not re.match('\d|\w|\_', string[i]):
            err = 'Invalid: "%s" is not allowed.' % string[i]
            return (False, err) 
    
    return (True, "Valid!")

for d in DATA:
   print "\n" + d.rjust(15) + " -> " + IsValidIdentifier(d)[1]