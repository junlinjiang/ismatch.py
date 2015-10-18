#!/usr/bin/env python
from fnmatch import *
from inspect import *
import re
from isstring import *
from tolist import *
from public import *

def isregex(object):
    return isinstance(object,re._pattern_type)

@public
def ismatch(string,pattern):
    if string==pattern:
        return True
    if pattern is None:
        return False
    for s in list(set(tolist(string))):
        if s==pattern:
            return True
        if not isstring(s):
            s = str(s)
        for p in tolist(pattern):
            if s==p:
                return True
            if isregex(p):
                return bool(p.match(s))
            if isfunction(p):
                return p(s)
            if fnmatch(s,str(p)):
                return True
    return False

if __name__=="__main__":
    print(ismatch("string","string")) # True
    print(ismatch("string","str*")) # True
    print(ismatch("string",["str*","another pattern"])) # True
    print(ismatch("string",None)) # False
    print(ismatch("string","long string")) # False
