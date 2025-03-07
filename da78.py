# -*- coding: utf-8 -*-
"""DA78.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1J95leoEAmhT5dbcTO7UJVbaR77iTpH95
"""

# .py - python extension
# .ipynb - Iron PYthon NoteBook

# Shortcuts
    # esc-B --> new cell below
    # esc-A --> new cell above
    # edit- cntr+M+D ---> delete a cell
    # cntr+entr --> run current cell

# Errors in python
print(dir(__builtins__))

# Compile time error
    # SyntaxError
    # IndentationError

# Runtime time error
    # every error other than compile time error

print('This is my first program')
a = 10
b = 20
c = a+b
print(c)
print('Bye ! See you.')
print(c/0)
print('Hello world')

# variable - is a container

# salt pack - data - 10
# salt container - variabe - a

# data type
    # fundamental - int, float, boolean, complex, string, None
    # derived - list, tuple, set, dictionary, range

# int - whole number

a = 10
print(a)
print(type(a))
print(id(a))

# object reusability --> -5 to 256
x = 100
y = 100
print(id(x))
print(id(y))
print(x is y)

# difference in ids
s = -6
d = -6
print(id(s))
print(id(d))
print(s is d)

# float - decimals
flt = 10.23
print(flt)
print(type(flt))
print(id(flt))

# object reusability - not applicable for float
flt_o = 10.23
print(flt is flt_o)

# type casting - to convert one data type to another
flt_var = 256.89
int_var = int(flt_var)
print(int_var)
print(float(250))

# Boolean - True / False
# what is true? - anything other than 0 is true.

bln = True
bln_o = True
print(bln, type(bln), id(bln), sep='\n')
print(bln, type(bln), id(bln))
print(bln is bln_o)

print(bool(256))
print(bool(0.00000000000000))
print(bool(0.00000000000001))

# complex - real+imag

cpx = 25+3j
print(cpx, type(cpx), sep='\n' )
print(cpx.real)
print(cpx.imag)

# None - empty
n = None
print(n, type(n), sep='\n')

# string - to define string use quotations
strr = 'This is python class'
str_num = '10'
print(strr, type(strr), sep='\n')
print(str_num, type(str_num), sep='\n')

print('This is python class')
print("This is krishna's python class")
print('''This is Krishna's python and "SQL" Class''')
print("""This is Krishna's python and "SQL" Class""")

# escape sequence
print('This is krishna\'s python class')
print("This is Krishna's python and \"SQL\" Class")
print('This is first output line.\nThis is second output line.')   # \n takes the text to next line
print('This is first line.\
This is also the same line.\
This is also the same line')

# Sequence - any data type that can be indexed or sliced.

#  0   1   2   3   4   5      ---> POSITIVE INDEXING
#  P   Y   T   H   O   N
# -6  -5  -4  -3  -2  -1      ---> NEGATIVE INDEXING

# Indexing - access one element at a time
strr = 'python class'
print(len(strr))    # starts from 1 but index starts from 0
print(strr[0])
print(strr[3])
print(strr[6])
print(strr[-1])

# Slicing - accessing range of elements at a time
# syntax - var[start: stop+1: step] - default values are - [0: len(seq): 1]
print(strr[0:6])
print(strr[0:6:2])
print(strr[1:6:2])
print(strr[::2])
print(strr[2::2])
print(strr[::-1])   # reverse sequence

# Concatenation

a = 'python'
b = 'coding invaders class'
print(a+b)
print(a + ' ' + b)

new_str = a+' '+b
print(new_str)

# Arithematic operator
print(10+3)    # addition
print(10-3)    # subtraction
print(10*3)    # multiplication
print(10/3)    # simple division
print(10//3)   # floor division - returns quotient value
print(10%3)    # Modulo division - returns reminder value
print(10**3)   # power of

# floor and ceil value
import math

# floor - lowest possible int
print(math.floor(3.999999))
print(math.floor(3.4))

# ceil - highest possible int
print(math.ceil(3.999999))
print(math.ceil(3.4))
print(math.ceil(3.000001))
print(math.ceil(3.0))

# Comparision operator - output will be boolean

#int
print(10 > 3)
print(10 >= 3)
print(10 < 3)
print(10 <= 3)
print(10 >= 10)
print()

# strings
print('p' > 'P')     #ascii - p = 112, P = 80
print('p' < 'P')
print('py' < 'P')    # if the length of comparision is different then len is used
print('Python' > 'python')
print('python' > 'class')

# to get ascii code
print(ord('p'))

# ascii to char
print(chr(112))

# equality operator
print('p' == 'p')   # equal to
print('P' != 'p')   # not equal to

# Logical operator

# AND - look for false and returns false if it is present

#   A       B    and   RESULTS
# -----------------------------
# True    True          True
# True    False         False
# False   True          False
# False   False         False


# OR - look for true and returns true if it is present

#   A       B    or   RESULTS
# -----------------------------
# True    True          True
# True    False         True
# False   True          True
# False   False         False

print(1 and 10)

# Derived data types - list, tuple, set, dict, range

# List - [] - hetro - sequence - mutable

lst_var = [2, 2.6, 25+8j, True, 'python', None]
print(lst_var)
print(type(lst_var))
print(lst_var[4])      # indexing
print(lst_var[1:5])    # slicing
print(lst_var[::-1])   # reversing
print()

# item assignment
print(lst_var[-2])
lst_var[-2] = 'SQL'
print(lst_var)

print()
print(dir(list))       # all inbuilt functions of the list

# Tuple - () - hetro - sequence - immutable


tpl_var = (2, 2.6, 25+8j, True, 'python', None)
print(tpl_var)
print(type(tpl_var))
print(tpl_var[4])      # indexing
print(tpl_var[1:5])    # slicing
print(tpl_var[::-1])   # reversing
print()
print(dir(tuple))       # all inbuilt functions of the tuple

print(tpl_var[-2])
# tpl_var[-2] = 'SQL'  # item assignment is not possible

# Set - {} - hetro - not a sequence - mutable - it wont hold duplicates

st = {1, 5, 'Suresh', 26, 18, 9, 5, 'Suresh'}
print(st, type(st), sep='\n')
print(dir(set))
# print(st[3])    # TypeError

# Dict - {key: value} - key and value is called as pair - not a sequence
    # keys are immutable, values are mutable
    # mutable data type cant be assigned as key

dct = {'name': 'suresh', 'age' : 26, 'city' : 'chennai', 'phno': 123}
print(dct)
print(type(dct))
print(dct.keys())    # to print keys
print(dct.values())  # to print values
print(dct.items())   # to print both
print()

# print(dct[2])     # KeyError
print(dct['age'])   # access by key

# keys cant be duplicated, but values can be
dct_2 = {'name': 'suresh', 'age' : 26, 'city' : 'chennai', 'phno': 123, 'name' : 'krishna'}

# item assignment
dct_2['city'] = 'Theni'
print(dct_2)

# mutable  datatype as key is not possible
# dct_3 = {['emp_name', 'emp_id']: ['suresh', '001']}

# immutable  datatype as key is possible
dct_3 = {('emp_name', 'emp_id'): ['suresh', '001']}
print(dct_3)

# range - syntax : range(start, stop+1,step)

lst_100_odd = list(range(1, 101, 2))
tpl_50_even = tuple(range(2, 51, 2))
print(lst_100_odd)
print(tpl_50_even)

# Input and output formating

# input formating
# fundamental DT
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))


# output formating
    # expected output "The addition of num_1 and num_2 is result."
print(f'The addition of {num_1} and {num_2} is {num_1+num_2}.')


# Input formating for derived DT
print()
lst_inp = eval(input('Enter a list: '))
print(lst_inp, type(lst_inp), sep='\n')

# Conditional statements - if, elif, else

inp = int(input('Enter a number: '))

if inp%2 == 0:
    print('The number is even')
else:
    print('The number is odd')

# take one number between 1-5 from user and print it in words
num = int(input('Enter a number between 1-5: '))

if num == 1:
    print('The number is one')
elif num == 2:
    print('The nunmber is two')
elif num == 3:
    print('The nunmber is three')
elif num == 4:
    print('The nunmber is four')
elif num == 5:
    print('The nunmber is Five')
else:
    print('Enter a valid number between 1 and 5')

num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

if num2 > num1:
    print('subtraction:', num2-num1)
    if num2 == 0:
        print('Output is Infinity')
    else:
        print('Division:', num1/num2)
else:
    print('subtraction:', num1-num2)
    if num2 == 0:
        print('Output is Infinity')
    else:
        print('Division:', num1/num2)

# basic calculaor
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
opp = int(input('Enter 1 for addition\nEnter 2 for subtraction\
\nEnter 3 for multiplication\nEnter 4 for division\n'))

if opp == 1:
    print(f'The addition of {num1} and {num2} is {num1+num2}')
elif opp == 2:
    if num2 > num1:
        print(f'The subtraction of {num2} and {num1} is {num2-num1}')
    else:
        print(f'The subtraction of {num1} and {num2} is {num1-num2}')
elif opp == 3:
    print(f'The multiplication of {num1} and {num2} is {num1*num2}')
elif opp == 4:
    if num2 == 0:
        print('Dividing number by zero is infinity')
    else:
        print(f'The division of {num1} and {num2} is {num1/num2}')
else:
    print('Enter a valid selection')

# Loops
# for loop
# syntax
    # for variable in seqence:   # for loop runs till the len of the seq is exhausted
    #     code
    #     code
    #     code

# while loop
# syntax
    # while expression :   # (True/False)
        # code
        # code
        # code
        # inc/dec

# for loop
sentence  = 'This is python class'

for letter in sentence:
    print(letter)

# while loop
sentence  = 'This is python class'

indx = 0
while indx < len(sentence):
    print(sentence[indx])
    indx += 1

sentence  = 'This is python class'

cnt = 0
for letter in sentence:
    cnt += 1

print(cnt)

sentence  = 'This is python class'

idx = 0
for letter in sentence:
    print(letter, '---->', idx)
    idx += 1

sentence  = 'This is python class'

pos = 1
for letter in sentence:
    if pos % 2 != 0:
        print(letter)
        pos += 1
    else:
        pos += 1

sentence  = 'This is python class'

out_sentence = ''
for letter in sentence:
    out_sentence += letter

print(out_sentence)

sentence  = 'This is python class'
# expected output - ssalc nohtyp si sihT

out_sentence = ''
for letter in sentence:
    out_sentence = letter + out_sentence

print(out_sentence)

#Write a python program to find below output using loop:-

#Input:- 'peter piper picked a peck of pickled peppers.'
#Output:- ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickled', 'peppers']

sentence = 'peter piper picked a peck of pickled peppers.'

out_lst = []
out_str = ''

for letter in sentence:
    if (letter != ' ') and (letter != '.'):
        out_str += letter
    else:
        out_lst.append(out_str)
        out_str = ''

print(out_lst)

# Alternative
sentence = input('Enter a string: ')

out_lst = []
out_str = ''

sentence += ' '

for letter in sentence:
    if letter == ' ':
        out_lst.append(out_str)
        out_str = ''
    else:
        out_str += letter

print()
print(out_lst)

# functions - user defined function

# syntax

# function defintion
    # def function_name():
    #     code
    #     code
    #     code

# function call
    # function_name()

# simple function to add two numbers

# function definition
def addition():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    print(f'Addition of {num1} and {num2} is {num1+num2}')

# function call
 addition()

# input to the function definiton- parameter
def dummy(a, b):  # parameters
    c = a * b
    print(c)

# input to the function call - Arguments
dummy(5, 3)

# positional parameters / arguments
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))

dummy(num1, num2)

# default parameters / arguments
def prod(a, b=1, c=1, d=1):
    print(a*b*c*d)

# default function calls
prod(1,2,3,4)
prod(1,2,3)
prod(1,2)
prod(1)

# Anonymous function - function without a name - doesnt have function definiton or call
# This is also called as lambda function

# syntax --> var = lambda var1 var2, var_n: expr
out = lambda num: num**2
print(out(3))

# filter, map, reduce

# filter
# syntax --> filter(function, sequence)

lst = list(range(10, 21))

# traditional code
out_lst = []
for ele in lst:
    if ele % 2 == 0:
        out_lst.append(ele)
print(out_lst)

# lambda code
# Alternative
    # function = lambda num: num%2==0
    # out = filter(function, lst)
    # print(list(out))

print(list(filter(lambda num: num%2==0, lst)))

# map
# syntax --> map(function, sequence)
lst = list(range(10, 21))
print('input:', lst)

# traditional code
out_lst = []
for ele in lst:
    out_lst.append(ele*2)
print('traditional:', out_lst)

# lambda code
print('lambda:', list(map(lambda num: num*2, lst)))

# Reduce - we have to import reduce before using it
# syntax -->  reduce(function, sequence)

# input
lst = list(range(1, 1001))

# traditional code
val = 0
for ele in lst:
    val += ele
print(val)

# lambda code
from functools import reduce
print(reduce(lambda num1, num2: num1+num2, lst))

# list of keywords
import keyword
print(keyword.kwlist)



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = sns.load_dataset('penguins')
data.head()

data.describe()

for cols in  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' ]:
    sns.boxplot(data[cols], orient='h')
    plt.show()

# Define a function calls addNumber(x, y) that takes in two number and returns the sum of the two numbers.

def addNumber(x, y):
    '''This function takes two numbers as input
    and returns the sum of the numbers'''
    # the above line is the doc string of the function

    print(x+y)

addNumber(10, 20)

# Write a function getBiggerNumber(x, y) that takes in two numbers as arguments and returns the bigger number.

def getBiggerNumber(x, y):
    '''This function takes two numbers as input
    and validates to find the larger number'''

    if x==y :
        print('Both numbers are equal')
    elif x>y:
        print(x)
    else:
        print(y)

getBiggerNumber(20, 20)

# Write a function to compute the BMI of a person.
#     BMI = weight(kg)  /  ( height(m)*height(m) )

# Note: Return a string of 1 decimal place.
# In - BMI(63, 1.7)
# Out - '21.8'
# In - BMI(110, 2)
# Out - '27.5'

def BMI(weight, height):
    BMI = weight / (height*height)
    BMI = round(BMI, 1)
    print(str(BMI))

BMI(63, 1.7)
BMI(110, 2)

# Write a function percent(value, total) that takes in two numbers as arguments, and returns the percentage value as an integer.
# In - percent(46, 90)
# Out - 51
# In - percent(51, 51)
# Out - 100
# In - percent(63, 12)
# Out - 525

def percent(value, total):
    return int((value/total)*100)

percent(51, 51)

# Recursive function
def validate_str():
    inp = str(input('Enter a upper case string: '))
    if inp.isupper() == True:
        print(inp)
    else:
        print('Enter a valid string')
        validate_str()

validate_str()

"""LIST COMPREHENSION"""

out_lst = []
for ele in dir(str):
    if ele[0:2] != '__':
        out_lst.append(ele)
print(out_lst)

comp_out = [ele for ele in dir(str) if ele[0:2] != '__']
print(comp_out)

lst = list(range(1,11))
ety_lst = []
for num in lst:
    if num%2:
        ety_lst.append(num)
print(ety_lst)

# list comprehension
output = [num for num in lst if num%2]
print(output)

"""METHODS OF STRING"""

# isupper, islower, isspace, isprintable

dstr = 'this is python class'
print(dstr.islower())
print(dstr.isupper())
print('GOOD DAY'.isupper())
print()
print('good day'.isspace())
print(''.isspace())
print(' '.isspace())
print('\n'.isspace())
print('\t'.isspace())
print()
print('this is string'.isprintable())
print('this\nis string'.isprintable())

# startswith, endswith

# startswith
print('Python class'.startswith("P"))
print('Python class'.startswith('Pyt'))
print('Python class'.startswith('pyth'))
print('python class'.startswith('th', 2))
print('python class'.startswith(' ', 7))
print()

# endswith
print('python class'.endswith('ss'))
print('python class'.endswith('lass'))
print('python class'.endswith('Class'))

tstr = 'ThIs iS PyThON ClAsS. suREsh Is TeAChINg.'

# Capitalize - Makes first letter of the string upper and rest lower
print(tstr.capitalize())
nw_str = tstr.capitalize()
print(tstr)
print(nw_str)
print()

# lower - Make entire sentence into lower case
print('Lower:',tstr.lower())
print('PyThON cLAß'.lower())
print()

# casefold - works by force conversion
print('PyThON cLAß'.casefold())
print()

# upper - Make entire sentence into upper case
print('Upper:',tstr.upper())
print('PyThON cLAß'.upper())
print()

# swapcase - converst upper to lower and vice versa
print('Swapcase:',tstr.swapcase())
print('PyThON cLAß'.swapcase())

# count

rstr = 'peter piper picked a peck of pickeled peppers'

# traditional method
cnt = 0
for letter in rstr:
    if letter == 'p':
        cnt += 1
print(cnt)
print()

# inbuild method
print(rstr.count('p'))
print(rstr.count('p', 8))
print(rstr.count('p', 8, 20))
print(rstr.count('z'))

sentence = 'peter piper picked a peck of pickeled peppers'

memory = 0
for letter in sentence:
    if letter == 'p':
        memory = memory + 1

print(memory)

# find and index
sentence = 'peter piper picked a peck of pickeled peppers'

# find - returns the index of first search occurance
print(sentence.find('k'))
print(sentence.find('k', 20))
print(sentence.find('k', 25, 33))
print(sentence.find('kel'))
print(sentence.find('w'))   # returns -1 if the substring is not present
print()

# index - returns the index of first search occurance
print(sentence.index('k'))
print(sentence.index('k', 20))
print(sentence.index('k', 25, 33))
print(sentence.index('kel'))
# print(sentence.index('w'))    # returns ValueError if the substring is not present

# rfind and rindex
sentence = 'peter piper picked a peck of pickeled peppers'

# rfind - returns the index of first search occurance from right side
print(sentence.rfind('k'))
print(sentence.rfind('k', 20))
print(sentence.rfind('k', 25, 33))
print(sentence.rfind('kel'))
print(sentence.rfind('w'))   # returns -1 if the substring is not present
print()

# rindex - returns the index of first search occurance from right side
print(sentence.rindex('k'))
print(sentence.rindex('k', 20))
print(sentence.rindex('k', 25, 33))
print(sentence.rindex('kel'))
# print(sentence.rindex('w'))    # returns ValueError if the substring is not present

# split, join
sentence = 'peter piper picked a peck of pickeled peppers'

# split --> converts string to list
print(sentence.split())
print(tuple(sentence.split('z')))  # typecast if needed
print()

# join( --> convert list to string
lst = ['peter', 'piper', 'picked', 'a', 'peck', 'of', 'pickeled', 'peppers']
print(' '.join(lst))
print('-'.join(lst))
print('>'.join(lst))

# replace

nw_sent = 'Suresh is taking python class to da78'
print(nw_sent.replace('python', 'sql'))
print(nw_sent.replace('taking', 'handling'))
print(nw_sent.replace('Suresh', 'suresh krishna'))
print(nw_sent.replace('s', '**'))

# strip, rstrip, lstrip
word = '        ####python class####          '
word2 = '####python class####'

print(word)
print(word.strip())             # by default removes the blank spaces
print(word2.strip('#'))         # removes the mentioned substring
print(word2.lstrip('#'))        # removes at left side
print(word2.rstrip('#'))        # removes at right side
print('###python class'.lstrip('###py'))

# simple assignment
word = '        ####python class####         '
print(word.strip().strip('#'))
print(word.strip('        ####'))

"""ADDITIONAL CONTENT -- SKIP IF NOT NEEDED --"""

para = '''Contrary to popular belief, Lorem Ipsum is not simply random text.
It has roots in a piece of classical Latin literature from 45 BC, making it
over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney
College in Virginia.'''

print(para)

sentences = para.split('.')
sentences

for sent in sentences:
    print(sent.split())

# alternative method
import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# add-ons
nltk.download('punkt')

print(para)

nltk_sent = sent_tokenize(para)
print(nltk_sent)

for sent in nltk_sent:
    words = word_tokenize(sent)
    print(words)

words = ['programming', 'programs', 'programmed', 'enjoying', 'enjoys', 'enjoyed', 'historical']
for i in words:
    print(i, ' ---> ', PorterStemmer().stem(i))

"""METHODS OF LIST"""

list_methods = [method for method in dir(list) if method[:2] != '__']
print(list_methods)

# Adding elements into the list - append, extend, insert

mlst = list(range(2, 11, 2))

# append - add element as a single element at the end of the list
mlst.append('python')
print(mlst)
mlst.append(list(range(12,17,2)))
print(mlst)
print()

# extend - add element as a individual element at the end of the list
mlst.extend(list(range(18, 23, 2)))
print(mlst, end='\n\n')

# insert - add element at a particular index
mlst.insert(6, 'class')
print(mlst)
mlst.insert(0, (0, 'da78'))
print(mlst)

# count - returns the number of search elements
clst = ['python', 100, 2, 3, 100, 5, 3, 2, 6, 9, 5, 3, 100]
print(clst.count(100))
print(clst.count(999))

# index - return the index of first search occurance
print(clst.index(100))
print(clst.index(100, 2))
print(clst.index(100, 4, len(clst)))
# print(clst.index(999))              # ValueError

# reverse - reverses the entire list
print(clst)
clst.reverse()
print(clst)

# sort - arange list in ascending or descending order
slst = [1,5,9,6,8,4,7,2,3]
print(slst)

# ascending order
slst.sort()
print(slst)

# descending order
slst.sort(reverse = True)
print(slst)

# sort with string
wlst = ['A', 'B', 'V', 'a', 'a', 'python', 'b', 'f', 'h', 'class']
wlst.sort(reverse=True)
print(wlst)

# remove elements from the list
rlst = ['this', 'is', 'python', 'class', 25, 65, 89]

# pop - remove last element by default (removes by index value)
print(rlst)
print(rlst.pop())        # return the removed element
print(rlst)
rlst.pop(-2)             # removes last 2nd element from above list
print(rlst)
print()

# remove - removes by element
rrlst = [1, 2, 5, 'python', 'class', 'sql', 'class']
print(rrlst)
rrlst.remove('class')
print(rrlst)
# rrlst.remove('krishna')   # ValueError
print()

# clear -  it removes all the elements from the list
rrlst.clear()
print(rrlst)

"""COPY"""

# Aliasing copy
rlst = [10, 20, 30]
alst = rlst
print(rlst, alst, sep='\n')
alst[-1] = 300
print(rlst, alst, sep='\n')
print()

# Shallow copy
rlst = [10, 20, 30, [100, 200, 300]]
slst = rlst[::]
print(rlst, slst, sep='\n')
slst[0] = 101
print(rlst, slst, sep='\n')
print()

slst[-1][-1] = 3
print(rlst, slst, sep='\n')

# deepcopy - import before using

from copy import deepcopy
dlst = deepcopy(rlst)
print(rlst, dlst, sep='\n')

# making changes in deepcopied list
dlst[1] = 'python'
dlst[-1][-2] = 'sql'
rlst[-2] = 502
print()
print(rlst, dlst, sep='\n')

# copy method in list - created shallow copy by default

new_lst = [10, 20, 30, [1, 2, 3]]
cpy_lst = new_lst.copy()
print(new_lst, cpy_lst, sep='\n')
print()
new_lst[1] = 200
print(new_lst, cpy_lst, sep='\n')
print()
new_lst[-1][-2] = 200
print(new_lst, cpy_lst, sep='\n')

"""METHODS OF TUPLE"""

tuple_methods = [method for method in dir(tuple) if method[:2] != '__']
tuple_methods

"""METHODS OF SET"""

set_methods = [method for method in dir(set) if method[:2] != '__']
set_methods

"""METHODS OF DICTIONARY"""

dct_methods = [method for method in dir(dict) if method[:2] != '__']
dct_methods

# write a function to validate a string is a palindrom or not

def validate_pallindrome(inp):
    '''This function takes string as input
    and validates if its a palindrome or not'''
    inp = inp.lower()
    if inp == inp[::-1]:
        print('Its a pallindrome')
    else:
        print('Not a pallindrome')

validate_pallindrome('MaLayalam')

"""# NUMPY"""

# NumPy - Numerical Python

import numpy as np
print(np.__version__)
print(len(dir(np)))

# Numpy array
lst = [1, 2, 3, 4, 5]
arr = np.array(lst)
print(lst)
print(arr)
print(type(arr))
print(arr.dtype)

# range of array elements
rarr = np.arange(1, 11, 2)
print(rarr)

# number of elements between given range of values

# 12 equal division between 1 and 3

lar = np.linspace(1, 3, 12)
print(lar)

# upcasting - int --> float --> complex --> object

print(np.array([1,2,3]).dtype)
print(np.array([1,2,3, 4.2]).dtype)
print(np.array([1,2,3, 4.2, 25+3j]).dtype)
print(np.array([1,2,3, 4.2, 25+3j, 'python']).dtype)   # object
print(np.array([1,2,True]).dtype)

# Array dimension

# zero dimension
zero_arr = np.array('Atul')
print(zero_arr)
print('Number of dimensions:', zero_arr.ndim)

# one dimension - either row or column
one_arr = np.array(['Atul', 'Shareen', 'Anchal'])
print(one_arr)
print('Number of dimensions:', one_arr.ndim)

# two dimension - both row and column
two_arr = np.array([['Atul', 'Shareen'],
                    ['Anchal','Arjun']])

print(two_arr)
print('Number of dimensions:', two_arr.ndim)

# three dimension - stack and row and column
three_arr = np.array([[['Atul', 'Shareen'],
                    ['Anchal','Arjun']]])

print(three_arr)
print('Number of dimensions:', three_arr.ndim)

tarr = np.array([[[1,4,7],[2,9,7], [1,3,0],[9,6,9]],
                 [[2,3,4],[1,3,5], [8,6,2], [2,4,8]]])

print(tarr)
print(tarr.shape)  # stack, rows, cols
print(tarr.size)

# Creating a transpose of a array (transpose matrix)

ar1 = np.array([[2,3,4],[4,5,6],[7,8,9]])
print('Non transpose 2D matrix:')
print(ar1)
print('\nTranspose 2D matrix:')
print(ar1.T)

"""# PANDAS"""

import pandas as pd     # Importing pandas library
print(pd.__version__)   # To check numpy version
print(len(dir(pd)))     # number of functions available within pandas

# to display all rows and cols
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Pandas Series - REFER THE NOTES
# https://github.com/Sureshkrishh/Datascience-notes/blob/main/Python/010.%20Pandas.ipynb

"""DATAFRAME"""

lst = ['India', 'Canada', 'USA', 'Singapore', 'Australia']
s_df = pd.DataFrame(lst, index=list(range(1, len(lst)+1)), columns=['country'] )
s_df

# creating dataframe from a dictionary

dct = {'emp_id':['001','002','003','004','005','006'],
       'emp_name':['Tom','bob','jerry','matt','steve','nick'],
       'emp_sal': [800000,500000,600000,650000,560000,1000000]}

d_df = pd.DataFrame(dct)
d_df

# Creating a dataframe from a nested list

nst_lst = [[2002, 'Japan', 'Brazil', 161],
                [2006, 'Germany', 'Italy', 147],
                [2010, 'South Africa', 'Spain', 145],
                [2014, 'Brazil', 'Germany', 171]
              ]

nst_df = pd.DataFrame(nst_lst, columns=['year', 'host', 'team', 'goals'])
nst_df

# get rid warnings
import warnings
warnings.filterwarnings('ignore')

"""IMPORTING DATA"""

imdb_data = pd.read_csv(r'/content/sample_data/imdb_rating.csv')
imdb_data

# to see the number of rows and cols
print(imdb_data.shape)
print(imdb_data.shape[0])             # rows
print(imdb_data.shape[1])             # cols
rows, cols = imdb_data.shape          # variable allocation
print(f'The data has {rows} rows and {cols} columns.')

# to see the total elements
imdb_data.size

# to see all column names
imdb_data.columns

# to see the data type of columns along with count of non null values
imdb_data.info()

# first 5 data rows
imdb_data.head()

# last 5 data rows
imdb_data.tail()

# first "n" data rows
imdb_data.head(7)

# last "n" data rows
imdb_data.tail(7)

# count of null values in each column
imdb_data.isnull().sum()

# percentage of null values in each column
imdb_data.isnull().mean()*100

# null value of specific column
imdb_data['duration'].isnull().mean()*100

loan_data = pd.read_csv('/content/drive/MyDrive/Datasets/Input/loan.csv')

loan_data.head()

loan_data.isnull().mean()*100

# delete data that has more than 30% missing value

for col in loan_data.columns:
    if loan_data[col].isnull().mean()*100 > 30:
        del loan_data[col]

# creating list of numerical column

numeric_data = []
for col in loan_data.columns:
    if loan_data[col].dtype != 'O':
        numeric_data.append(col)

print(numeric_data)

# writing the above code using list comprehension

num_data = [col for col in loan_data.columns if loan_data[col].dtype != 'O']
print(num_data)

# list comprehension to extract non numeric cols

obj_data = [col for col in loan_data.columns if loan_data[col].dtype == 'O']
print(obj_data)

# statistical summary
loan_data.describe()

# stats of particular cols
loan_data['loan_amnt'].describe()

# indiviadual values of a particular cols
print(loan_data['loan_amnt'].mean())
print(loan_data['loan_amnt'].std())
print(loan_data['loan_amnt'].max())
print(loan_data['loan_amnt'].min())

# understanding basic functions of pandas
imdb_data

# removing a row by index
imdb_data.drop(9, axis=0, inplace=True)

# remove a column by index (column name)
imdb_data.drop('duration', axis=1, inplace=True)

# viewing rest of the data
imdb_data

# reseting the index numbers to start from one

imdb_data.index = imdb_data.index+1
imdb_data

# accessing a particular row using loc (location)
imdb_data.loc[9]

# adding a new row at end
imdb_data.loc[len(imdb_data.index)+1] = [9.4, 'End Game', 'Action']
imdb_data

# reallocating index values
imdb_data.index = ['movie_1', 'movie_2', 'movie_3', 'movie_4',
                  'movie_5', 'movie_6', 'movie_7', 'movie_8',
                  'movie_9', 'movie_10']
imdb_data

# access rows

# using the user defined row value - loc method
print(imdb_data.loc['movie_6'])
print()

# using default index value - iloc method
imdb_data.iloc[5]

# sorting the data (ascending order)
imdb_data.sort_values('star_rating', ascending=True)

# sorting the data (descending order)
imdb_data.sort_values('star_rating', ascending=False)

# reset the index to default
imdb_data = imdb_data.reset_index()
imdb_data

# delete extra cols
del imdb_data['index']      # works only for columns

imdb_data

final_df = loan_data.iloc[:20, :10]
final_df

final_df.iloc[5:12, 0:5:2]

final_df.iloc[:, [0, 6, 7]]

final_df

final_df.loc[0:5, ['member_id', 'term']]

"""MATPLOTLIB"""

# 2-D visualisation library

import matplotlib
print(matplotlib.__version__)
print(dir(matplotlib))

print(dir(matplotlib.pyplot))

# importing the actual matplotlib visual module

import matplotlib.pyplot as plt


# import other required module
import numpy as np
import pandas as pd

# basic chart of matplotlib

ar1 = np.arange(1,11)
ar2 = np.linspace(1000,2000,10)

ar3 = np.arange(5,11)
ar4 = np.linspace(400,800,6)

plt.plot(ar1, ar2, label='B-Line', marker='o', linestyle='--', color='r',
         markerfacecolor='g', markeredgecolor='black')
plt.plot(ar3, ar4, label='O-Line', marker='D', ls=':', color='g')
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.title('This is title')
plt.legend(loc=0)
plt.show()              # print option to extact graph from object

"""SEABORN"""

# both 2D and 3D visual library
# efficient to create visuals from data frame


import seaborn as sns
print(sns.__version__)
print(dir(sns))

# seaborn library has inbuild data for practice purpose
?? sns.load_dataset

# list of data set inside seaborn
print(sns.get_dataset_names())

# importing titanic
tdata = sns.load_dataset('titanic')
tdata

# distribution of data

vis = sns.displot(tdata['fare'], kind='kde')
vis.set(xlabel = 'Ticket Price', title='Distribution plot')

plt.show()

# outliers
sns.boxplot(tdata['fare'], orient='h')
plt.show()

# penguin data
penguin = sns.load_dataset('penguins')
penguin

# unique data in columns
print(penguin['species'].unique())
print(penguin['species'].nunique())
print(penguin['species'].value_counts())
print(penguin['species'].value_counts(normalize=True)*100)

# stat summary
penguin.describe()

# ploting boxplot for all numerical columns

for cols in penguin:
    if penguin[cols].dtype != 'O':
        sns.boxplot(penguin[cols], orient='h')
        plt.show()

# scatter plot
sns.scatterplot(penguin, x='bill_length_mm', y='body_mass_g', hue='species')
plt.show()

# pairplot
sns.pairplot(penguin)
plt.show()

# pair plot for x_vars vs y_vars

x = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
y = ['body_mass_g']

sns.pairplot(penguin, x_vars=x, y_vars=y, height=5, aspect=0.8, kind='reg')
plt.show()

# pair plot for x_vars vs y_vars

x = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
y = ['body_mass_g']

sns.pairplot(penguin, x_vars=x, y_vars=y, height=5, aspect=0.8, kind='reg', hue='species')
plt.show()

# pair plot for x_vars vs y_vars

x = ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm']
y = ['body_mass_g']

sns.pairplot(penguin, x_vars=x, y_vars=y, height=5, aspect=0.8, hue='island')
plt.show()



