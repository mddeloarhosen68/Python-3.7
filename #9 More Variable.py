Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 5
>>> id(num)
140736994465568
>>> name = 'Anon'
>>> id(name)
2315236279536
>>> a = 10
>>> b = a
>>> a
10
>>> b
10
>>> id(a)
140736994465728
>>> id(b)
140736994465728
>>> id(10)
140736994465728
>>> k = 10
>>> id(k)
140736994465728
>>> a = 9
>>> id(a)
140736994465696
>>> id(b)
140736994465728
>>> k = a
>>> id(k)
140736994465696
>>> b = 8
>>> id(b)
140736994465664
>>> PI = 3.14
>>> PI
3.14
>>> PI = 3.15
>>> type(PI)
<class 'float'>
>>> 