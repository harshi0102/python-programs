#variables are container that store information that can be  manipulated and referenced later by the programmer within the code
# we simply assign value to the variable
name="abhisheak"# type str
age="20"  # type int
passed=True #type bool

#set of conventions while creating variables
#variable names can only contain alpa numeric characters and underscores (A-z,0-9 and _)
#variable  names should start with a letter or underscore character 
#variables are case sensitive
#variables names cannot start with a number

Color="yellow" #valid variable name
cOlor="red"# valid variable name
_color="pink" #valid variable name

#5color="blue"#invalid variable name
#$color="peach"#invalid variable name


NameofCity="Mumbai"#Pascal case
nameOfCity="delhi"#Camel case
name_of_city="jaiput"#snake case


#scope of a variable
#The scope of the variable is the area within which the variable has been created. Based on this a variable can either have a local scope or a global scope.

#A.Local variable- A local variable is created within a function and can be only used inside that function. Such a variable has a local scope.

icecream="vanilla"#global variable
def foods():
    vegetable="potato"#local variable
    fruit="lichi"# local variable
    print(vegetable,"is a local variable")
    print(icecream+"is a global variable")
    print(fruit+"is a alocal variable")
foods()

#B.Global variable- A global variable is created in the main body of the code and can be used anywhere within the code. Such a variable has a global scope.

icecream="vanilla" #global variable
def foods():
    vegetable="potato" #local variable 
    fruits="lichi" #local variable
    print(vegetable+"is a local variable")


foods()
print(icecream+"is a global variable")
