# pySimpleCache
python simple cache 

## How to Refresh the cache
    two ways to refresh the cache for certain keys:
    (1) use key arguments

    @useCache
    def func(*args, **kargs):
        ...

    func(refresh=True)

    the drawback is: 
     a) the functions needed to be cached must have default arguments `*args` 
        and `kargs`
     b) 'refresh' key-argument is unclear for external functions
    (2) use decorator `recache` before functions, like:
     recache(func)(...)
     with drawback:
      a) the writing style is a little puzzled!

    When use multithreading! there accurs problems [TODO]

## todo list
    1, 增加缓存最大量限制
    2, 增加多线程实现LRU机制
    3, 增加调用计数，时效
    4, cache的刷新