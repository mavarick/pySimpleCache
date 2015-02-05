#!/usr/bin/env python

import time
from pySimpleCache import useCache, reCache
import pdb

def CalTime(info):
    def wrapper1(func):
        def _wrapper(*args, **kargs):
            print info
            st = time.time()
            func(*args, **kargs)
            et = time.time()
            print "Time used: ", et - st
        return _wrapper
    return wrapper1

#pdb.set_trace()

@CalTime(">>Test")
@useCache
def GetValue(*args, **kargs):
    time.sleep(1)
    return "ok"


GetValue()

GetValue()

reCache(GetValue)()

GetValue()

GetValue(refresh=True)

GetValue()
GetValue()
GetValue()
GetValue()