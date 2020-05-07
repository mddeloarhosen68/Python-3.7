Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums = [25,14,58,96]
>>> nums
[25, 14, 58, 96]
>>> nums[0]
25
>>> nums[4]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    nums[4]
IndexError: list index out of range
>>> nums[-1]
96
>>> names = ['anon','asif','adit','shakil','hridoy']
>>> names
['anon', 'asif', 'adit', 'shakil', 'hridoy']
>>> values = [95,'anon',25.9]
>>> values
[95, 'anon', 25.9]
>>> mil = [nums, names]
>>> mil
[[25, 14, 58, 96], ['anon', 'asif', 'adit', 'shakil', 'hridoy']]
>>> nums.append(77)
>>> nums
[25, 14, 58, 96, 77]
>>> nums.insert(2,74)
>>> nums
[25, 14, 74, 58, 96, 77]
>>> nums.remove(14)
>>> nums
[25, 74, 58, 96, 77]
>>> nums.pop(1)
74
>>> nums
[25, 58, 96, 77]
>>> nums.pop()
77
>>> nums
[25, 58, 96]
>>> del nums[2:]
>>> nums
[25, 58]
>>> nums.extend([29,98,78,57,12])
>>> nums
[25, 58, 29, 98, 78, 57, 12]
>>> min (nums)
12
>>> max (nums)
98
>>> sum(nums)
357
>>> nums.sort()
>>> nums
[12, 25, 29, 57, 58, 78, 98]
>>> new = 'Telusko'
>>> print(new[-3])
s
>>> 