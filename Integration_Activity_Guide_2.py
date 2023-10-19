"""VARIABLES"""
#Assign Value
variable_name = 1  #int
variable_name1 = 1.0  #float
variable_name2 = "Hello"  #string
variable_name3 = True  #boolean
"""DATA TYPES"""
type(variable_name)
type(variable_name1)
type(variable_name2)
type(variable_name3)
"""CAST DATA TYPES"""
#Change from string to float
x = "1"
float(x)
#Change from string to int
x = "2"
int(x)
#---------------------------------------------------------------------#
"""Input/Output"""
input()  # Input Value - Console will wait until response
print()  # Output - Display on console

#---------------------------------------------------------------------#
"""COMPARISON [CONDITIONALS]"""
var_1 = 2
var_2 = 2
#EQUALS
var_1 == var_2
#DIFFERENT
var_1 != var_2
#GREATER THAN 
var_1 > var_2
#SMALLER THAN 
var_1 < var_2
#GREATER EQUAL 
var_1 >= var_2
#SMALLER EQUAL 
var_1 <= var_2
#---------------------------------------------------------------------#
#Conditionals
"""IF"""
condition = True
if (condition):
  print("Condition is true")
"""IF ELSE"""
condition = True
if (condition):
  print("Condition is true")
else:
  print("Condition is false")
"""IF ELIF ELSE"""
#Multiple conditions
condition = True
condition2 = True
if (condition):
  print("This is condition 1")
elif (condition2):
  print("This is condition 2 and can only be printed if condition 1 is false")
else:
  print("No Condition")
"""IF NESTED"""
#Nested if else
condition = True
condition2 = True
if (condition):
  print("This is condition 1")
  if (condition2):
    print("This is condition 2 and can only be printed if condition 1 is true")
else:
  print("No Condition")

#---------------------------------------------------------------------#
"""LOGICAL OPERATORS"""
x = True
y = False
#AND
print("AND")
# ONLY TRUE WHEN BOTH CONDITIONS ARE TRUE
print(x and y)  # False
print(y and y)  # False
print(y and x)  # False
print(x and x)  #True

#OR
print("OR")
# TRUE WHEN ONE OR BOTH CONDITIONS ARE TRUE
print(x or y)  # True
print(y or x)  # True
print(x or x)  # True
print(y or y)  # False

#---------------------------------------------------------------------#
#LOOPS
"""WHILE"""
condition = 1
while (condition <= 10):
  print(condition)
  condition = condition + 1
