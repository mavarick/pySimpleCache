# pySimpleCache
python simple cache 

## Refresh the cache
* refresh the total cache
```python
    PySimpleCache.refresh()	
```
* refresh one certain data
use key-argument `refresh=True`
```python
		@useCache		
		def func(arg1, ...): 		
		 ...		
		\# refresh the func		
		func(arg1, ..., refresh=True)		
```
this method need: 
	1. function must has default arguments `*args` and `**kargs`
	2. 'refresh' key-argument is unclear for function itself
or, use function `recache(func)(func_arguments)`
```python
		recache(func)(arg1, ...)		
```
* **Underlying Problems**
	1. multiprocessing
    
## TODO
- [ ] 增加缓存最大量限制
- [ ] 增加多线程实现LRU机制
- [ ] 增加调用计数，时效
- [x] ~cache的刷新~~
