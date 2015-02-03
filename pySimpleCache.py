#!/usr/bin/env python
#encoding:utf8
'''
python的简单的缓冲池的实现，利用dict来保存数据
'''
class PySimpleCache(dict):
    _instance = None
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = dict.__new__(cls)
        return cls._instance

    def get(self, name, default=None):
        if not name: return default
        if name not in self:
            return default
        return self[name]

    def set(self, name, value):
        self[name] = value

    def getset(self, name, value):
        result = self.get(name)
        if not result:
            self.set(name, value)
            result = value
        return result

def useCache(func):
    def wrapper(*args, **kargs):
        _cache_dict = PySimpleCache.getInstance()
        fn = "#".join(["cache", func.__module__, func.__class__.__name__, func.__name__,
             str(args), str(kargs)])
        val = _cache_dict.get(fn)
        if not val:
            val = func(*args, **kargs)
            _cache_dict.set(fn, val)
        return val
    return wrapper


