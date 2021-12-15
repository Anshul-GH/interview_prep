Reference: https://www.interviewbit.com/python-interview-questions/#what-is-python

1. What is Python?
> Python is a high-level, general-purpose, interpreted programming language.
It can be used to build any type of applications with the right tools and libs.
Additionally, python supports objects, modules, threads, exception-handling, and automatic memory management
***

2. What are the benefits of using Python?
- Python is a general purpose programming language
- Simple and easy to learn syntax that emphasizes readibility and reduces programming maintenance costs
- It is capable of scripting, supports third-party packages, is completely open-source
- Also supports modularity and code reuse
- Supports dynamic typing and dynamic binding
***

3. What is a dynamically typed language?
Typing - It refers to type-checking in programming languages.
Kinds:
A. Strongly-typed: Languages that do not allow for 'type-coercion' (implicit conversion of data types). 
Example: Python. "1"+2 will result in an error
B. Weakly-typed: Languages that allow 'type-coercion'
Example: Javascript. "1"+2 will result in "12"

Type-checking can also be done at two stages:
A. Static: Data types are checked before execution.
B. Dynamic: Data types are checked during execution.

Python is an interpreted language - executes and interprets each statement line-by-line. Thus type-checking is done on the fly, during execution.
Hence, Python is a dynamically typed language.
***

4. What is an interpreted language?
An interpreted language executes its statements line-by-line.
Examples: Python, Javascript, R, PHP and Ruby etc.
There is no code compilation step involved.
***

5. What is PEP8 and why is it important?
PEP stands for Python Enhancement Proposal.
PEP 8 standardizes the style guideline for writing Python code
It is not only a good practice but often mandatory for the code to adhere to PEP8 standards
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
# Modules: simply Python files with .py extension.
- Can have set of functions, classes or variables defined and implemented.
- Can be imported and initialized using the ‘import’ keyword

# Packages: Allow for hierarchical structuring of the module namespace using dot notation.
- Modules help in avoiding clashes between global variable names, in a similar manner, packages help avoid clashes between module names.
***

11. What are global, protected and private attributes in Python?
# Global: Variables are public variables that are defined in the global scope.
- Defined using ‘global’ keyword

# Protected: Variables defined with a single underscore (_) prefixed to their identifiers. Example: _myname
- There is no explicit restriction on usage but as a best practice, they should not be accessed outside the parent or inheriting child classes

# Private: Variables defined with a double underscore (__) prefixed to their identifiers. Example: __myprivatename
- There is no explicit restriction on usage but as a best practice, they should not be accessed outside the defining class

General Definitions:

private - Only the current class will have access to the field or method.
protected - Only the current class and subclasses (and sometimes also same-package classes) of this class will have access to the field or method.
public - Any class can refer to the field or call the method.
***

12. What is self in Python?
- Self keyword in Python is used to identify an instance of the calling class
- Helps in distinguising between the methods and attributes of a class from its local variables
***

13. What is __init__?
__init__ is the constructor method in Pythong
- Automatically gets called to allocate memory whenever a new instance/object of the class is created.
***

14. What is break, continue and pass in Python?
# Break: 
Terminates the loop immediately and the control flows to the statement after the body of the loop.

# Continue: 
Terminates the 