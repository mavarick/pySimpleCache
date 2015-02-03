#!/usr/bin/env python

import time
from pySimpleCache import useCache

def CalTime(info):
    def wrapper(func):
        def _wrapper(*args, **kargs):
            print info
            st = time.time()
            func(*args, **kargs)
            et = time.time()
            print "Time used: ", et - st
        return _wrapper
    return wrapper

@CalTime(">>Test")
@useCache
def GetValue():
    time.sleep(1)
    return "ok"

GetValue()

GetValue()


