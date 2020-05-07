Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = {1:'Anon',2:'Asif',4:'Adit'}
>>> data
{1: 'Anon', 2: 'Asif', 4: 'Adit'}
>>> data[4]
'Adit'
>>> data[1]
'Anon'
>>> data[2]
'Asif'
>>> data.get(1)
'Anon'
>>> deta[3]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    deta[3]
NameError: name 'deta' is not defined
>>> data.get(3)
>>> print(data.get(3))
None
>>> data.get(1,'NotFound')
'Anon'
>>> data.get(3,'NotFound')
'NotFound'
>>> keys = ['Anon','Asif','Adit']
>>> values = ['Python','Swift','Networking']
>>> data = dic(zip(keys,vlues))
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    data = dic(zip(keys,vlues))
NameError: name 'dic' is not defined
>>> data = dict(zip(keys,vlues))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    data = dict(zip(keys,vlues))
NameError: name 'vlues' is not defined
>>> data
{1: 'Anon', 2: 'Asif', 4: 'Adit'}
>>> data = dic(zip(keys,values))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    data = dic(zip(keys,values))
NameError: name 'dic' is not defined
>>> data = dict(zip(keys,values))
>>> data
{'Anon': 'Python', 'Asif': 'Swift', 'Adit': 'Networking'}
>>> data['Monika'] = 'CS'
>>> data
{'Anon': 'Python', 'Asif': 'Swift', 'Adit': 'Networking', 'Monika': 'CS'}
>>> del data['Monika']
>>> data
{'Anon': 'Python', 'Asif': 'Swift', 'Adit': 'Networking'}
>>> prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog
{'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}
>>> prog['JS']
'Atom'
>>> prog['Python']
['Pycharm', 'Sublime']
>>> prog['Python'][1]
'Sublime'
>>> prog['Java']
{'JSE': 'Netbeans', 'JEE': 'Eclipse'}
>>> prog['Java']['JEE']
'Eclipse'
>>> 