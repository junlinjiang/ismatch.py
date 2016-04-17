#!/usr/bin/env python
import fnmatch
import inspect
import re
from isstring import isstring
from tolist import tolist
from public import public

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
            if inspect.isfunction(p):
                return p(s)
            if fnmatch.fnmatch(s,str(p)):
                return True
    return False
