#!/usr/bin/env python
#encoding:utf8
'''
python的简单的缓冲池的实现，利用dict来保存数据

dict的值的形式是：
    {"value": value,        # 保存值
     "count": 1,            # 引用计数
     "time": saving_time}   # 保存时间
     如果refresh，那么各值重新赋值
'''
import datetime

class PySimpleCache(dict):
    _instance = None
    _disable = False
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = dict.__new__(cls)
        return cls._instance
    @classmethod
    def refresh(cls):
        cls._instance = None

    def setDisable(self, value):
        PySimpleCache._disable = value

    def getDisable(self):
        return PySimpleCache._disable

    def get_key(self, name, default=None):
        if not name: return default
        if name not in self:
            return default
        self[name]['count'] += 1
        return self[name]["value"]

    def set_key(self, name, value):
        self[name] = {
            "value": value, 
            "count": 1,
            "time": datetime.datetime.now()
            }

    def getset(self, name, value):
        result = self.get_key(name)
        if not result:
            self.set_key(name, value)
            result = value
        return result

    def get_size(self):
        return len(self)

def useCache(func):
    def wrapper(*args, **kargs):
        _cache_dict = PySimpleCache.getInstance()
        fn = "#".join(["cache", func.__module__, func.__class__.__name__, func.__name__,
             str(args), str(kargs)])

        val = _cache_dict.get_key(fn)
        if ((not kargs.get("refresh", False)) and  # use key-argument to refresh the key-value
             val and                               # if value is not none
             (not _cache_dict.getDisable())):       # should be available
            return val

        val = func(*args, **kargs)
        _cache_dict.set_key(fn, val)
        return val
    return wrapper

def reCache(func):
    def wrapper(*args, **kargs):
        _cache_dict = PySimpleCache.getInstance()
        _cache_dict.setDisable(True)
        func(*args, **kargs)
        _cache_dict.setDisable(False)
    return wrapper



