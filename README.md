# pySimpleCache
python simple cache 

## Refresh cache
* refresh total cache
```python
    PySimpleCache.refresh()	
```
* refresh one certain data
use key-argument `refresh=True`
```python
		@useCache		
		def func(arg1, ...): 		
		 ...		
		func(arg1, ..., refresh=True)		
```
<ul>some drawbacks here: 
	<li>function must has default arguments `*args` and `**kargs`</li>
	<li>'refresh' key-argument is unclear for function itself</li>
</ul>

or, use function `recache(func)(func_arguments)`
```python
		recache(func)(arg1, ...)		
```
* **Underlying Problems**
	* multiprocessing
    
## TODO
- [ ] 增加缓存最大量限制
- [ ] 增加多线程实现LRU机制
- [ ] 增加调用计数，时效
- [x] ~cache的刷新~~
