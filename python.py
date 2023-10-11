####################### CLI

python -m my_module # needs a __main__.py in my_module folder + __init__.py

#  Making an executable file
## #!/usr/bin/env python3
## print("Hello!")
## ./hello.py


s = Template("$greeting, $name!")
s.substitute(greeting="Hello", name="Max")

join > + # for string concat

match name:
    case "Max" | "max":
        print("Hello Max!")
    case _:                     
        print("Hello anonymous") # case 1: default match all
    case name:
        print(f"Hey {name}") # case 2: capture pattern
    case name if 'pedro' in name: # guard
        pass

if type(name) is str:
    pass

if isinstance(age, int):
    pass

copy.copy() / copy.deepcopy()

########################### Metaprogramming: dunder methods ##################

Object ---instance of---> Class
Class  ---instance of---> Metaclasses (ex. type)

print(type("Hello")) #prints <class 'str'>
print(type(Thing))   #prints <class 'type'>
print(type(Thing())) #prints <class '__main__.Thing'>
print(type(type))    #prints <class 'type'>

Food = type('Foo', (), {}) # Class 'Foo', inherits nothing (), no attrs or methods {}

def __init__(obj, toppings):
    obj.toppings = toppings

Pizza = type('Pizza', (Food,), {'name': 'pizza', '__init__': __init__})

if type(answer) is int:
    pass
if isinstance(answer, int):
    pass

my_thing.__doc__
help(my_thing)
dir(my_thing)

__name__ # can be: "__main__" OR "utils_lib.core.game_script" for utils_lib/core/game_script.py
__file__ # absolute path of the module on the current system. ex path = pathlib.Path(__file__).resolve()

def __init__(self, age):        # constructor
    self.age = age

def __repr__(self):             # print object representation
    return self.age

def __str__(self):
    return f"The age is {self.age}"

def __add__(self, other):       # Overload '+'
    return self.age + other.age

def __eq__(self, other):
    return self.age == other.age

def __ge__(self, other):        # Greater than OR equal
    return self.age >= other.age

def __call__(self, other):
    return self.age*3

__enter__(self) | __exit__(self) # used for context managers (with bla...)

class MyClass:
    @classmethod                # method of the class
    def inform(cls, codeword):
        cls._codeword = codeword

    @staticmethod               # method in the namespace of the class (can't access class related things)
    def add(a, b):
        return a + b

    @property
    def sizepx(self):
        return self.size.replace("px", "")

@dataclass
class DTO:
    name="Max"
    age=33

class PositiveInt(int):            # First __new__ : extending built in types 
    def __new__(cls, value):            # __new__ runs before __init__,
        return int.__new__(cls, abs(value))

class Players(object):             # Second __new__ : custom initialization logic
    current_players = 0
    max_players = 4

    def __new__(cls, value):       # ex. limit the number of instances of certain objects 
        if cls.current_players > cls.max_players:
            raise ValueError(f'Max instances reached!')

        cls.current_players += 1
        return super().__new__(cls)

class Singleton:                    # Third __new__ : creating a singleton
    instance = None

    def __new__(cls):
        if cls.instance == None:
            cls.instance = super().__new__(cls)
        return cls.instance

########################### Type Hints
int | float | bool | str | bytes #built ins
list[int] | set[int] | dict[str, float] | 
tuple[int, str, float] | typle[int, ...]
list[int | str]
from typing import Any, Self
from dataclasses import dataclass

class Stack:
    def push(self, item: Any) -> Self:
        self.items.append(item)
        return self

@dataclass
class PersonData:
    age: int = 18
    name: str = ""

########################### ASYNC: asyncio

async def main():
    await asyncio.sleep(1)

asyncio.run(main())

########################### Template strings and related
from string import Template
s = Template("$greeting, $user!, {thing}fication")
print(s.substitute(greeting="Hi", user="Max", thing="uwu"))

message = " ".join(["hey!", "welcome"]) # "hey! welcome"

########################### Pattern matching

match lunch_order:               # MATCH statement
    case 'taco':
        pass
    case 'salad' | 'soup':       # OR
        pass
    case order:                  # CAPTURE patterns
        print(f"Enjoy {order}")
    case sweet if 'sugar' in sweet: # CAPTURE pattern with guard clause
        print(f"THis {sweet} is delicious")
    case _:                      # DEFAULT
        pass

########################### usefull libs
math
pathlib
os
json

########################### context manager ############################

with open("filename.txt", mode="r") as my_file: # r+t r+b
    print(my_file.read()) # my_file.readline() my_file.readlines()

my_file.tell() # where are you stepped on the file counting chars from start
my_file.seek(0) # go to the start of the file
my_file.write(contents) # override with data from the last seek position
my_file.writelines(["line1", "line2"]) #doesnt insert \n chars
print(data1, data2, sep=",", file=my_file)
my_file.truncate()

########################## write to json #################################
with open('nearby.json', 'w') as json_file:
    json.dump(my_obj, json_file)

with open('nearby.json', 'r') as json_file:
    my_obj = json.load(json_file)

########################### Diamond problem: C3 MRO superclass linearization ########
L[Pizza] = merge({Pizza, Food, Object}) = Pizza + Food + object
L[Sandwich] = Sandwich + Food + object

L[Calzone] = merge(Clazone, {Pizza, Food, object}, {Sandwich, Food, object})
L[Calzone] = Calzone + Pizza + merge({Food, object}, {Sandwich, Food, object}) # jump to head of next set coz Food is in tail
L[Calzone] = Calzone + Pizza + Sandwich + merge({Food, object}, {Food, object}) # Food is not in other tails but Heads so add it, same with obj
L[Calzone] = Calzone + Pizza + Sandwich + Food + object

############################# Packing and distributing #########################
https://realpython.com/pypi-publish-python-package/
# pyproject.toml

[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["feed", "reader", "tutorial"]
dependencies = [
    "feedparser >= 5.2.0",
    "html2text",
    'tomli; python_version < "3.11"',
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"

############################### Benchmarking #########################
from timeit import timeit

def fun1: pass
def fun2: pass

time_fun1 = timeit(fun1)
time_fun2 = timeit(fun2)

print("benchmark fun 1: ", time_fun1, sep="\t")
print("benchmark fun 2: ", time_fun2, sep="\t")
