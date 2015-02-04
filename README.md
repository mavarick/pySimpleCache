# pySimpleCache
python simple cache 

## How to Refresh the cache
    (1) refresh the total cache
        `PySimpleCache.refresh()`
    (2) refresh one certain data
        a) use key-argument `refresh=True`
            for:
            `
            @useCache
            def func(arg1, ...): 
                ...
            # refresh the func
            func(arg1, ..., refresh=True)
            `
            - drawbacks:
                - function must has default arguments `*args` and `**kargs`
                - 'refresh' key-argument is unclear for function itself
        b) use function `recache(func)(func_arguments)`
            `
            recache(func)(arg1, ...)
            `
            - drawbacks:
                - the writing style is a little puzzled!
    (3) **Underlying Problems**
        a) multiprocessing
    

## todo list
    * 增加缓存最大量限制
    * 增加多线程实现LRU机制
    * 增加调用计数，时效
    * ~~cache的刷新~~