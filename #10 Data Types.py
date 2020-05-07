Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 2
>>> type(num)
<class 'int'>
>>> num = 5.2
>>> type(num)
<class 'float'>
>>> num = 6+9j
>>> type(num)
<class 'complex'>
>>> a = 5.6
>>> b = int(a)
>>> type(b)
<class 'int'>
>>> b
5
>>> k = float(b)
>>> type(k)
<class 'float'>
>>> k
5.0
>>> <class 'complex'>
SyntaxError: invalid syntax
>>> k = 6
>>> c = complex(b,k)
>>> type(c)
<class 'complex'>
>>> c
(5+6j)
>>> b<k
True
>>> bool = b < k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b > k
False
>>> int(True)
1
>>> int(False)
0
>>> lst = [25,12,47,89,57,69]
>>> lst
[25, 12, 47, 89, 57, 69]
>>> type(lst)
<class 'list'>
>>> t = (12,14,58,36,74,98)
>>> t
(12, 14, 58, 36, 74, 98)
>>> type(t)
<class 'tuple'>
>>> s = {25,87,36,14,78,96}
>>> s
{96, 36, 78, 14, 87, 25}
>>> type(s)
<class 'set'>
>>> str = "Anon"
>>> str
'Anon'
>>> type(str)
<class 'str'>
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> type(range(10))
<class 'range'>
>>> list (range(2,10,2))
[2, 4, 6, 8]
>>> list (range(1,9,2))
[1, 3, 5, 7]
>>> d = {'Anon': 'Nokia', 'Asif': 'iphone', 'Adit': 'mi'}
>>> d
{'Anon': 'Nokia', 'Asif': 'iphone', 'Adit': 'mi'}
>>> d.key
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d.key
AttributeError: 'dict' object has no attribute 'key'
>>> d.key()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    d.key()
AttributeError: 'dict' object has no attribute 'key'
>>> d.keys()
dict_keys(['Anon', 'Asif', 'Adit'])
>>> d.values()
dict_values(['Nokia', 'iphone', 'mi'])
>>> d['Anon']
'Nokia'
>>> d.get('Asif)
      
SyntaxError: EOL while scanning string literal
>>> d.get('Asif')
'iphone'
>>> d.get('Adit')
'mi'
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> topics

Here is a list of available topics.  Enter any topic name to get more help.

ASSERTION           DELETION            LOOPING             SHIFTING
ASSIGNMENT          DICTIONARIES        MAPPINGMETHODS      SLICINGS
ATTRIBUTEMETHODS    DICTIONARYLITERALS  MAPPINGS            SPECIALATTRIBUTES
ATTRIBUTES          DYNAMICFEATURES     METHODS             SPECIALIDENTIFIERS
AUGMENTEDASSIGNMENT ELLIPSIS            MODULES             SPECIALMETHODS
BASICMETHODS        EXCEPTIONS          NAMESPACES          STRINGMETHODS
BINARY              EXECUTION           NONE                STRINGS
BITWISE             EXPRESSIONS         NUMBERMETHODS       SUBSCRIPTS
BOOLEAN             FLOAT               NUMBERS             TRACEBACKS
CALLABLEMETHODS     FORMATTING          OBJECTS             TRUTHVALUE
CALLS               FRAMEOBJECTS        OPERATORS           TUPLELITERALS
CLASSES             FRAMES              PACKAGES            TUPLES
CODEOBJECTS         FUNCTIONS           POWER               TYPEOBJECTS
COMPARISON          IDENTIFIERS         PRECEDENCE          TYPES
COMPLEX             IMPORTING           PRIVATENAMES        UNARY
CONDITIONAL         INTEGER             RETURNING           UNICODE
CONTEXTMANAGERS     LISTLITERALS        SCOPING             
CONVERSIONS         LISTS               SEQUENCEMETHODS     
DEBUGGING           LITERALS            SEQUENCES           

help> LISTS
Mutable Sequence Types
**********************

The operations in the following table are defined on mutable sequence
types. The "collections.abc.MutableSequence" ABC is provided to make
it easier to correctly implement these operations on custom sequence
types.

In the table *s* is an instance of a mutable sequence type, *t* is any
iterable object and *x* is an arbitrary object that meets any type and
value restrictions imposed by *s* (for example, "bytearray" only
accepts integers that meet the value restriction "0 <= x <= 255").

+--------------------------------+----------------------------------+-----------------------+
| Operation                      | Result                           | Notes                 |
|================================|==================================|=======================|
| "s[i] = x"                     | item *i* of *s* is replaced by   |                       |
|                                | *x*                              |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s[i:j] = t"                   | slice of *s* from *i* to *j* is  |                       |
|                                | replaced by the contents of the  |                       |
|                                | iterable *t*                     |                       |
+--------------------------------+----------------------------------+-----------------------+
| "del s[i:j]"                   | same as "s[i:j] = []"            |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s[i:j:k] = t"                 | the elements of "s[i:j:k]" are   | (1)                   |
|                                | replaced by those of *t*         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "del s[i:j:k]"                 | removes the elements of          |                       |
|                                | "s[i:j:k]" from the list         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.append(x)"                  | appends *x* to the end of the    |                       |
|                                | sequence (same as                |                       |
|                                | "s[len(s):len(s)] = [x]")        |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.clear()"                    | removes all items from *s* (same | (5)                   |
|                                | as "del s[:]")                   |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.copy()"                     | creates a shallow copy of *s*    | (5)                   |
|                                | (same as "s[:]")                 |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.extend(t)" or "s += t"      | extends *s* with the contents of |                       |
|                                | *t* (for the most part the same  |                       |
|                                | as "s[len(s):len(s)] = t")       |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s *= n"                       | updates *s* with its contents    | (6)                   |
|                                | repeated *n* times               |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.insert(i, x)"               | inserts *x* into *s* at the      |                       |
|                                | index given by *i* (same as      |                       |
|                                | "s[i:i] = [x]")                  |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.pop([i])"                   | retrieves the item at *i* and    | (2)                   |
|                                | also removes it from *s*         |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.remove(x)"                  | remove the first item from *s*   | (3)                   |
|                                | where "s[i]" is equal to *x*     |                       |
+--------------------------------+----------------------------------+-----------------------+
| "s.reverse()"                  | reverses the items of *s* in     | (4)                   |
|                                | place                            |                       |
+--------------------------------+----------------------------------+-----------------------+

Notes:

1. *t* must have the same length as the slice it is replacing.

2. The optional argument *i* defaults to "-1", so that by default
   the last item is removed and returned.

3. "remove()" raises "ValueError" when *x* is not found in *s*.

4. The "reverse()" method modifies the sequence in place for
   economy of space when reversing a large sequence.  To remind users
   that it operates by side effect, it does not return the reversed
   sequence.

5. "clear()" and "copy()" are included for consistency with the
   interfaces of mutable containers that don’t support slicing
   operations (such as "dict" and "set"). "copy()" is not part of the
   "collections.abc.MutableSequence" ABC, but most concrete mutable
   sequence classes provide it.

   New in version 3.3: "clear()" and "copy()" methods.

6. The value *n* is an integer, or an object implementing
   "__index__()".  Zero and negative values of *n* clear the sequence.
   Items in the sequence are not copied; they are referenced multiple
   times, as explained for "s * n" under Common Sequence Operations.

Related help topics: LISTLITERALS

help> 