# pySimpleCache
python simple cache 

## How to Refresh the cache
1. refresh the total cache
```python
PySimpleCache.refresh()
```
2. refresh one certain data
       1. use key-argument `refresh=True`
            for:
```
            @useCache
            def func(arg1, ...): 
                ...
            # refresh the func
            func(arg1, ..., refresh=True)
```
            - drawbacks:
                - function must has default arguments `*args` and `**kargs`
                - 'refresh' key-argument is unclear for function itself
        2. use function `recache(func)(func_arguments)`
```
            recache(func)(arg1, ...)
```
            - drawbacks:
                - the writing style is a little puzzled!
3. **Underlying Problems**
        a) multiprocessing
    

## todo list
- [x] 增加缓存最大量限制
- [x] 增加多线程实现LRU机制
- [x] 增加调用计数，时效
- [x] ~cache的刷新~~
