# Advanced Python: Iterators, Generators, Context Managers & Decorators

## Course Description

Python provides a number of advanced constructs that can make the language more expressive, and in many cases more efficient.  Python expresses “laziness” via iterators, sometimes defined by generator functions, which are a way of describing delayed computation and infinite data streams. Context managers are a means of surrounding blocks of code with reusable setup and teardown.  Decorators allow you to express cross-cutting concerns for functions or classes that are given a general aspect, again with an emphasis on reusability.

## Learning Objectives

* Construct lazy data streams with generator expressions and generator functions
* Write custom iterator classes
* Combine lazy data streams using itertools
* Wrap operations in custom contexts
* Decorate functions in reusable orthogonal ways

## Topics

* Writing generator functions
  * Understand the iterator protocol
  * Write class-based versions of iterators  
  * Use yield and yield from
* The itertools modules
  * Combine lazy iterator streams
  * Describe infinite/unbounded operations
  * A calculus for streams
* Context Managers
  * Use common existing context managers
  * Create context managers using decorated functions and yield
  * Write class-based versions of context managers
* Decorators
  * Write decorator functions and classes
  * Write parameterized decorators


## Programming Exercises

* Iterator protocol
* Yield and yield from
* Class-based iterators
* Combine streams
* Working with infinite streams
* Use standard context managers
* Use contextlib to create context manager
* Create class-based context manager
* Create a decorator function
* Create a parameterized decorator
