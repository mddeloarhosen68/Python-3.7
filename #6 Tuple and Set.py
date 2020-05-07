Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup = (21,36,14,25)
>>> tujp
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tujp
NameError: name 'tujp' is not defined
>>> tup
(21, 36, 14, 25)
>>> s = {22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s = {25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s [2]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s [2]
TypeError: 'set' object is not subscriptable
>>> s.add{10}
SyntaxError: invalid syntax
>>> s.add(10)
>>> s
{98, 10, 75, 14, 25, 63}
>>> s.remove(10)
>>> s
{98, 75, 14, 25, 63}



