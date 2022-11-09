#what is a python
print('''why python?

there are so many libraries in python?
python is a general purpose , high level, interpreted langugage, with easy syntax and dynamic semantics
python is created by Guido Van Rossum in 1989

*interpreted langugae- control flow line by line 
*dynamic semantics- python sense which data type is it 
*python is a slow language as compared to the other language 

clean and beautiful language - working as a interface with the user 
because of high computing level it is perfectly fine


why is python popular?
easy
free(open source)
applications
library and support-library is the piece of code written by someone else.
python interface -work done by the others 
using python is very easy
to make a real world project - python takes 40 or 50 lines because there are so many libraries 


python behaviour is same in mac or linux system
embeddable &extensible-this is a python project - we can have a c++java project
we cna have programming files included in the python projects

huge libraries -numpy,pandas, etc
object orientation- to create a program by focusing on the object 

whereis python used in the industry?
google
dropbox
netflix
bittorrent
nasa

Learning path
main motive is to learn AI and ml
python crash course by eric 
python basics till oops 


career opportunity
web development
game development  is at peak

big data  -very prominent
web testing
ai/data science
smart devices

machine learning vs artificial intelligence VSdeep learningVS data science

AI- enables machine to think
ML- machine learning is the subset of AI - ml includes all the - statistical tools to explore the AI
supervised learning, unsupervised learning, reinforced learning
Reinforced learning- whenever machine rewrite prediction we give them positive marks, otherwise 
negative marks
deep learning- multi neural architecture 
[ANN,CNN,RNN- ]
DATA SCIENCE- STATS, PROBABILITY , ALGEBRA 

INSTALLATION
PYTHON CRASH COURSE -BY ERIC MATHEWS 
ANACONDA NAVIGATOR -JUPYTER NOTEBOOKS
MINICONDA - WHICH IS SMALLER SIZE OF ANACONDA
YOU CAN USE GOOGLE COLAB
DOWNLOAD ANACONDA FROM GOOGLE 



''')
#keywords are reserved words in python
#we cannot use keywords as a variable name, function name or any other identifier 
#keywords are case sensitive

#get all keywords of python
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))


print("hello message")

'''identifiers is the name given to the entities like class, function, variables.it helps in differentiating 
one entitity to another.

rules for identifiers
it can be combination of letters(a-z) or upper case (A-Z) or digits or underscore
it cannot start with number, 1variable is invalid but variable1 is fine.
keywords cannot be used as identifiers 
'''
x=10
Global="hello world"
print(Global)

'''global is a keyword and Global is an identifier'''

"identifer cannot start with any digit"

'''Every variable holds a value which is the information associated wiht the variable'''
_message="hello"
print(_message)
'''
assignment happense from right hand sigh to left hand side'''
message=123
print(message)
print(type(message))
message="bye bye 2020"
print(type(message))
print(message)


a=20
print(type(a))
a="20"
print(a+a)


'''indentation'''

'''multiple statements in one line'''
a=20;b=30
print(a)
print(b)
'''we can also use comma too'''

'''numbers,
for division - float is the resultant value on completely dividing by any number fully.
floor division
-17//4
answer is -5
smallest integral value ----in the number line 
use bodmas

A string is a sequence of character.
computers do not deal with character
computer deal with numbers (binary)

in python sting is a sequence of unicode character 


'''

s2="demo123"
s="make it count"
print(s[4:9])

s3="demopython"
print(s3[3:8])
