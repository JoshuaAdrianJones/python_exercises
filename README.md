# python_exercises

> Repo purpose is project based learning including setting up:
> - tests
> - CI runner
> -  makefiles
> - dockerfiles

### tools used

black
isort
pylint
pytest
mypy
coverage

### Notes on TDD and red-green-refactoring in Python

    Red green refactoring is the process of writing failing tests, then writing code to make them pass.

    https://gideonbrimleaf.github.io/2021/01/26/relative-imports-python.html

    Getting relative imports working for the tests/ folder was annoying
    
    - added Make file
    - added docker running with makefile
    - set up tests and coverage

    Red : write tests first that fail
    Green : write code that passes the tests
    Refactor : cleanup

    Should be a good starting point for new projects

Book used: Exercises for programmers (57) by B P Hogan




### Notes on behaviour driven development 

Read about Cucumber and Gherkin


### Coding style

emphasis on functional core imperative shell patterns.


### Exercise .3 quotes

quotes.py = a random quote + author
quotes.py --pick = pick a specific api source from a menu.

aggregate 3 different APIs' into a command line utility


quote apis 
https://type.fit/api/quotes

https://zenquotes.io/api/random

https://quotes.rest/qod.json