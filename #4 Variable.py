Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 2 + 3
5
>>> x = 2
>>> x = 3
>>> x = 2
>>> x + 3
5
>>> y = 3
>>> x + y
5
>>> x = 9
>>> x + y
12
>>> x
9
>>> x +10
19
>>> x + 10
19
>>> _ + y
22
>>> name = 'youtube'
>>> name
'youtube'
>>> name + ' rocks'
'youtube rocks'
>>> name - ' rocks'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    name - ' rocks'
TypeError: unsupported operand type(s) for -: 'str' and 'str'
>>> name * ' rocks'
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    name * ' rocks'
TypeError: can't multiply sequence by non-int of type 'str'
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:10]
'tube'
>>> name[0:3] = 'my'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[0:3] = 'my'
TypeError: 'str' object does not support item assignment
>>> name[0] ='R'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[0] ='R'
TypeError: 'str' object does not support item assignment
>>> 'my ' + name[3:]
'my tube'
>>> myname = 'DH Anon'
>>> len(myname)
7
>>> print(r'Telusko \n Rocks')
Telusko \n Rocks
>>> 