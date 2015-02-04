# pySimpleCache
python simple cache 

## How to Refresh the cache
1. refresh the total cache

2. refresh one certain data
	1. use key-argument `refresh=True`
		* drawbacks:
			- function must has default arguments `*args` and `**kargs`
			- 'refresh' key-argument is unclear for function itself
	2. use function `recache(func)(func_arguments)`
		* drawbacks:
			- the writing style is a little puzzled!
3. **Underlying Problems**
	1. multiprocessing
    
## TODO
- [ ] 增加缓存最大量限制
- [ ] 增加多线程实现LRU机制
- [ ] 增加调用计数，时效
- [x] ~cache的刷新~~
