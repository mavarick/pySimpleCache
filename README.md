# pySimpleCache
python simple cache 

## How to Refresh the cache
* refresh the total cache
	PySimpleCache.refresh()

* refresh one certain data
	1. use key-argument `refresh=True`
		@useCache		
		def func(arg1, ...): 		
		 ...		
		# refresh the func		
		func(arg1, ..., refresh=True)		

		drawbacks:
		- function must has default arguments `*args` and `**kargs`
		- 'refresh' key-argument is unclear for function itself
	2. use function `recache(func)(func_arguments)`
		recache(func)(arg1, ...)		

		drawbacks:
		- the writing style is a little puzzled!

### **Underlying Problems**
	1. multiprocessing
    

## todo list
- [ ] 增加缓存最大量限制
- [ ] 增加多线程实现LRU机制
- [ ] 增加调用计数，时效
- [x] ~cache的刷新~~
