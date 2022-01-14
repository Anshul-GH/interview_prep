Reference: https://www.interviewbit.com/python-interview-questions/#what-is-python

1. What is Python?
- Python is a high-level, general-purpose, interpreted programming language.
- It can be used to build any type of applications with the right tools and libs.
- Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management
***

2. What are the benefits of using Python?
- Python is a general purpose programming language
- Simple and easy to learn syntax that emphasizes readibility and reduces programming maintenance costs
- It is capable of scripting, supports third-party packages, is completely open-source
- Also supports modularity and code reuse
- Supports dynamic typing and dynamic binding
***

3. What is a dynamically typed language?
- Typing: It refers to type-checking in programming languages.
Kinds:
- Strongly-typed: Languages that do not allow for 'type-coercion' (implicit conversion of data types). 
Example: Python. "1"+2 will result in an error

- Weakly-typed: Languages that allow 'type-coercion'
Example: Javascript. "1"+2 will result in "12"

Type-checking can also be done at two stages:
- Static: Data types are checked before execution.
- Dynamic: Data types are checked during execution.

Python is an interpreted language - executes and interprets each statement line-by-line. Thus type-checking is done on the fly, during execution.

Hence, Python is a dynamically typed language.
***

4. What is an interpreted language?
- An interpreted language executes its statements line-by-line.
Examples: Python, Javascript, R, PHP and Ruby etc.
- There is no code compilation step involved.
***

5. What is PEP8 and why is it important?
- PEP stands for Python Enhancement Proposal.
- PEP 8 standardizes the style guideline for writing Python code
- It is not only a good practice but often mandatory for the code to adhere to PEP8 standards
***

6. What is scope in Python?
A scope is a block of code where a particular object is relevant
1. Local Scope: Local objects available in the current function
2. Global Scope: Objects available thorughout the code execution since their inception
3. Module-level Scope: Refers to global objects of the current module accessible in the program.
4. Outermost Scope: Refers to built-in names callable in the program. The objects in this scope are searched last to find the name referenced.
***

7. What are lists and tuples? What is the key difference between the two?
- Both are sequence data types
- Lists are mutable while Tuples are immutable
- Both can store different datatypes within the same object
- Lists use square brackets while Tuples use parenthesis
***

8. What are the common built-in datatypes in Python?
- None Type
- Numeric Types: int, float, complex, bool
- Sequence Types: list, tuple, range, str
- Mapping Type: dict
- Set Types: set, frozenset
- Modules:
- Callable Types: types to which function call can be applied.
***

9. What is ‘pass’ in Python?
The pas keyword represents a null operation in Python
Used to fill up empty blocks of code which may execute during the runtime but logic for them is yet to be written
***

10. What are modules and packages in Python?
- Modules: simply Python files with .py extension.
- Can have set of functions, classes or variables defined and implemented.
- Can be imported and initialized using the ‘import’ keyword

- Packages: Allow for hierarchical structuring of the module namespace using dot notation.
- Modules help in avoiding clashes between global variable names, in a similar manner, packages help avoid clashes between module names.
***

11. What are global, protected and private attributes in Python?
- Global: Variables are public variables that are defined in the global scope.
- Defined using ‘global’ keyword

- Protected: Variables defined with a single underscore (_) prefixed to their identifiers. Example: _myname
- There is no explicit restriction on usage but as a best practice, they should not be accessed outside the parent or inheriting child classes

- Private: Variables defined with a double underscore (__) prefixed to their identifiers. Example: __myprivatename
- There is no explicit restriction on usage but as a best practice, they should not be accessed outside the defining class

*General Definitions*:

private: Only the current class will have access to the field or method.
protected: Only the current class and subclasses (and sometimes also same-package classes) of this class will have access to the field or method.
public: Any class can refer to the field or call the method.
***

12. What is self in Python?
- 'self' keyword in Python is used to identify an instance of the calling class
- Helps in distinguising between the methods and attributes of a class from its local variables
***

13. What is __init__?
__init__ is the constructor method in Python
- Automatically gets called to allocate memory whenever a new instance/object of the class is created.
***

14. What is break, continue and pass in Python?
- Break: Terminates the loop immediately and the control flows to the statement after the body of the loop.
- Continue: Terminates the current iteration of the statement, skips the rest of the code in the current iteration and the control flows to the next iteration of the loop.
- Pass: Pass keyword in Python is generally used to fill up empty blocks and is similar to an empty statement. Its used as a pace-hoder for code that is yet to be defined or to create abstract entities.
***

15. What is the difference between Python Arrays and Lists?
- Arrays in Python (import array) can only contain elements of the same datatype
- 'array' package is a wrapper around C language arrays and consumes far less memory than lists.
- Lists in python can contain elemnts of different datatypes 
- List consumes large memory
***

16. How is memory managed in Python?
- Memory management in Python is handled by Python Memory Manager.
- The memory allocated by the manager is in form of a private heap space dedicated to Python
- All Python objects are stored in this heap and are private.
- These objects are inaccessible to the programer directly.
- Additionally, Python has built-in garbage collection to recycle unuse memory for the private heap space.
***

17. What are Python namespaces?
- A namespace in Python ensures that object names in a program are unique and can be used without any conflict.
A. Local Namespace: Temporarily created for function calls and gets cleared when the function returns.
B. Global Namespace: Includes the names of various imported packages that are being used in the current project.
C. Built-In Namespace: Includes built-in functions of core Python and built-in names for various types of exceptions.
***

18. What are decorators in Python?
- Decorators in Python are essentially functions that add functionality to an existing function in Python without changing the structure of the function itself.
- They are represented with '@' prefixed names and are called in bottom-up fashion.
- Example:
```
# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    
    return wrapper

# decorator function to split string
def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    
    return wrapper


@splitter_decorator # this is executed second
@lowercase_decorator # this is executed first
def hello():
    return 'Hello World'
```

Decorators can also access arguments for the functions and can modify and pass them back

```
# decorator function to capitalize names
def name_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    
    return wrapper

@name_decorator
def say_hello(name1, name2):
    return "Hello " + name1 + "! Hello " + name2 + "!"
```
***

19. What is pickling and unpickling in Python?
- The 'pickle' module in python is used to serialize objects
- Serialization: Transforming an object into a format (byte stream) that can be stored (dumped in memory as file) and recalled (deserialized) later on from the memory, when needed.
- Function calls:
Pickling: pickle.dump()
Unpickling: pickle.load()
***

20. What are generators in Python?
- Generators are functions in Python that return an iterable collection of items, one at a time, in a set manner.
- Generators use the 'yield' keyword, rather than 'return' to return a generator object.
Example: Fibonacci using generators:
```
def fib(n):
    p, q = 0, 1
    while (p < n):
        yield p
        p, q = q, p+q

x = fib(10)
for i in x:
    print(i)    # output: 0, 1, 1, 2, 3, 5, 8
```
***

21. How is Python interpreted?
- Python is a bytecode (set of interpreter readable instructions) interpreted generally.
- The Python source code is a file with .py extension
- The .py source code is first compiled to give .pyc which is a bytecode. 
- This bytecode can then be interpreted by the official CPython or JIT (Just In Time) compiler compiled by PyPy.
***

22. What are iterators in Python?
- An iterator is an object that can remember its state - i.e. where it is during an iteration
- The __iter__() method initializes an iterator. 
- It has a __next__() method that returns the next item in iteration and points to the next element.
- At the end of the iterable, the __next__() method returns a StopIteration exception.
***

23. What does *args and **kwargs mean?
A. args:
- '*args' is a special syntax used in the function definition to pass variable length arguments.
- "*" means variable length and 'args' is the name used by convention - not mandatory

B. kwargs:
- '**kwargs' is a special syntax used in function definition to pass variable length keyworded arguments.
- Here also 'kwargs' is a name used as convention but can be any other name/string as well
- Keyworded argument means a variable that has a name when passed to a function
- It is actually a dictionary of variable names and corresponding values.
***

24. How does inheritance work in Python?
- Inheritance allows for a class to access the attributes and methods of another class.
- Aids in code reusability and manitaining application without code redundancy
***

25. Types of inheritance in Python:


![A. Single Inheriatnce:](https://s3.ap-south-1.amazonaws.com/myinterviewtrainer-domestic/public_assets/assets/000/000/928/original/Single_Inheritance.jpg?1629984086)

![B. Multi-level Inheritance:](https://s3.ap-south-1.amazonaws.com/myinterviewtrainer-domestic/public_assets/assets/000/000/930/original/Multi-level_Inheritance.jpg?1629984200)

![C. Multiple Inheritance:](https://s3.ap-south-1.amazonaws.com/myinterviewtrainer-domestic/public_assets/assets/000/000/934/original/Multiple_Inheritance.jpg?1629984498)

![D. Heirarchical Inheritance:](https://s3.ap-south-1.amazonaws.com/myinterviewtrainer-domestic/public_assets/assets/000/000/935/original/Hierarchical_Inheritance.jpg?1629985141)
***

26. Why is 'finalize' used?
- Finalize method is used for freeing up the unmanaged resources and clean up before the garbage collection method is invoked
- Helps in performing memory management in Python
***

27. What is 'Pandas'?
- Pandas is an open source, Python-based library used in data manipulation applications requiring high performance.
- Name is derived from 'Panel Data' - having multidimensional data
***

28. How can we combine different pandas dataframes together?
- Stacking Horizontally:
```
df1.append(df2)
```
- Stacking Vertically:
```
df1.concat(df2)
```
- Joining on one or more common columns:
```
df1.join(df2)
```
***

29. Define GIL.
- GIL stands for Global Interpreter Lock
- Its a mutex used for limiting access to Python objects and aids in effective thread synchronization by avoiding deadlocks
- GIL helps in achieving multitasking (and not parallel computing)
***

30. Metaclass in Python. What is its use?
- A class in Python is an object/instance of 'metaclass'
- The default metaclass is 'type'
```
class Foobar:
    pass

type(Foobar) # --> <class 'type'>


foo = Foobar()
type(foo) # --> <class '__main__.Foobar'>
```
![Pictorial Rep:](https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/instance-of.png)

- Alternate way to define a class in Python:
```
MyClass = tyep('MyClass', (), {})
type(MyClass) # --> <class '__main__.MyClass'>
```

- We can also create out own custom metaclass
```
class Meta(type):
    pass

class Complex(metaclass=Mete):
    pass

type(Complex) # --> <class '__main__.Meta'>
```
***

31. Static typing in Python
- Python by default, is a dynamically typed language
- Meaning, it is not necessary to declare the type of a variable when assigning a value to it.
```
# This will work with Python
major = 'Tom'
major = 1
```
- This is convenient as well as challenging in certain scenarios
- Example: If a function only expects integer arguments, throwing strings into the function might crash the program.
- Function Annotation:
```
def foo(n: int, s: str='Tom') -> str:
    return s*n
```
- Variable Annotation:
```
major: str='Tom'
```
- For annotating advanced types like 'list', 'dict', etc, we need to use 'typing' module
```
from typing import List, Tuple, Dict

l: List[int] = [1, 2, 3]
t1: Tuple[float, str, int] = (1.0, 'two', 3)
t2: Tuple[int, ...] = (1, 2.0, 'three')
d: Dict[str, int] = {'uno': 1, 'dos': 2, 'tres': 3}
```
***

32. 'dataclasses' module in Python.
- The ['dataclasses'](https://docs.python.org/3/library/dataclasses.html) module in Python provides a decorator and functions for automatically adding special methods like:
__init__()
__repr__()
to a user defined class.
```
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of an item in inventory."""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```
The above code will add, among other things, a __init__() that looks like:
```
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```
***

33. What is Warlus Operator in Python?
- Walrus operator introduced in Python 3.8 offers a way to accomplish two tasks at once
A. Assigning a value to a variable
B. Returning that value
- It offers a way to write shorter and more readable code that can be more efficient computationally
```
# Old:
num = 15
print(num)

# Walrus:
print(num := 15)

# Output: 15
```
***

34. What are descriptors in Python?
