1. What is GIL (Global Interpreter Lock)?
- It is a mutex in CPython that permits only one thread to execute Python bytecode at a time
- This applies to even multicore systems
- Prevents true parallelism in multi-threaded CPU-bound tasks
- Simplifies memory management by avoiding reference count races
- Forces threads to context switch after ~5ms or 100 bytecode operations
- Ideal for I/O-bound work (eg web services) where threads yield during wait

For CPU bound tasks, like computations, bypass GIL with multiprocessing:
Multiprocessing:
- Each process gets its own interpreter and GIL
- Enables parallel core usage
- But this comes with higher memory utilization because of data duplication
---------------------------------------------------------------------------------------------------
2. What is a Decorator?
- Decorators are functions (or classes) that wrap others to extend behavior without modifying the original code
- Uses the @ symbol for syntactic sugar (eg @timer def func(): is equivalent to func = timer(func))
- Work great for logging, caching, authentication or metrics.
- decorator.py
---------------------------------------------------------------------------------------------------
3. What are Metaclasses?
- Metaclasses are classes of classes
- They control how classes themselves are created by subclassing the default 'type' metaclass
- We can specify. meta class as 'metaclass=YourMetaClassName' in the class definitions during declaration
- Used for patterns like - Singleton, ORM or for enforcing rules across subclasses
- metaclass.py
---------------------------------------------------------------------------------------------------
4. What is a Generator?
- Generators produce values lazily via 'yield'
- Work by creating iterators that pause and resume without loading full iterables into memory
- Perfect for processing large datasets like logfiles
- They enable memory efficient comprehensios, coroutines and pipelines
- generator_fibonacci.py
---------------------------------------------------------------------------------------------------
5. What is a Context Manager?
- Context managers in Python handle resource setup and cleanup reliably using with statement
- context_manager.py
- Built-ins like open() use them implicitly
