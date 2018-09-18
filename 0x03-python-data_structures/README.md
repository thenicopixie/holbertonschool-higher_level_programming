# README
### Description
Python - Data Structures: Lists, Tuples
#### What I should learn:
- What are lists and how to use them
- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
- What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the `del` statement and how to use it
#### Requirements:
- Allowed editors: `vi`, `vim`, `emacs`
- All files to be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3)
- Python stype: `PEP 8` style (version 1.7.)
- C files are compile with `gcc 4.8.4` using the flags `-Wall` `-Werror`, `-Wextra`, and `-pedantic`
- Style: `Betty` style. `betty-style.pl` and `betty-doc.pl`
- Not allowed to use global variables
- No more than five functions per file
---
File | Function Prototype | Description
-----|--------------------|------------
0-print\_list\_integer.py | def print\_list\_integer(my\_list=[]): | Function that prints all integers of a list. Not allowed to import modules. Can assume the list only contains integers. Not allowed to case integers into strings. Have to use `str.format()` to print strings.
1-element\_at.py |  def element\_at(my\_list, idx): | A function that retrieves an element from a list in C. If `idx` is negative, the function should return `None`. If `idx` is out of range, the function should return `None`. Not allowed to import any module of use `try/except`
2-replace\_in\_list.py | def replace\_in\_list(my\_list, idx, element): | A function that replaces an element of a list at a specific position. If `idx` is negative, the function should not modify anything, and returns the original list. If `idx` is out of range, the function should not modify anything, and returns the original list. Not allowed to import any module or use`try/except`
3-print\_reversed\_list\_integer.py | def print\_reversed\_list\_integer(my\_list=[]): | A function that prints all integers of a list, in reverse order. Format: one integer per line. Not allowed to import any module or case integers into strings.
4-new\_in\_list.py | def new\_in\_list(my\_list, idx, element): | A function that replaces an element in a list at a specific position without modifying the original list. If `idx` is negative, the function should return a copy of the original `list`. If `idx` is out of range, the function should return a copy of the original `list`. Not allowed to import and module of use `try/except`
5-no\_c.py | def no\_c(my\_string): | A function that removes all characters `c` and `C` from a string. The function should return the new strings. Not allowed to import any module or use `str.replace()`.
6-print\_matrix\_integer.py | def print\_matrix\_integer(matrix=[[]]): | A function that prtins a matrix of integers. Not allowed to import any module or cast any integer into strings.
7-add\_tuple.py | def add\_tuple(tuple\_a=(), tuple\_b=()): | A function that adds 2 tuples. Returns a tuple with 2 integers: The first element should be the addition of the first element of each argument; the second element should be the addition of the second element of each argument. Not allowed to import any module. If a tuple is smaller that 2, use the value `0` for each missing integer. If a tuple is bigger than 2, use only the first 2 integers.
8-multiple\_returns.py | def multiple\_returns(sentence): | Write a function that returns a tuple with the length of a string and its first character. If the sentence is empty, the first character should be equal to `None`. Not allowed to import any module.
9-max\_integer.py | def max\_integer(my\_list=[]): | A function that finds the biggest integer of a list. If the list is empty, return `None`. Not allowed to import and module or use the builtin `max()`.
10-divisible\_by\_2.py | def divisible\_by\_2(my\_list=[]): | A function that finds all multiples of 2 in a list. Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2. The new list should have the same size as the original list. Not allowed to import and module.
11-delete\_at.py | def delete\_at(my\_list=[], idx=0): | A function that deletes the item at a specific position in a list. If `idx` is negative or out of range, nothing chages (return the same list). Not allowed to import any module or use `pop()`.
12-switch.py | ... | Complete the source code in order to switch value `a` and `b`. Code should be exactly five lines.
13-is\_palindrome.c, lists.h | int is\_palindrome(listint\_t \*\*head); | A function that checks if a singly linked list is a palindrome. Return `0` if it is not a palindrome, `1` if it is a palindrome. An empty list is considered a palindrome.

Source code for #12:
```
#!/usr/bin/python3
a = 89
b = 10
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print("a={:d} - b={:d}".format(a, b))
```
#### Author
Nicole Swanson - [@Nicolette_Swan](https://twitter.com/Nicolette_Swan) 
