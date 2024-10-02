print("hello world!")
print("hello ", "AIE", "It is me!")
print ("Hello AIE" , "\nthis is omar ", 26+1)
## new printing test
print("Hello",end=" ")
print("AIE!")

print("hello",end="")
print("today we have ",3,"activity.")
#################################################################
############################# Variables #########################
#################################################################
x = 10 #declaring variables 
y = 15.5
print(x, " " ,y)
b:int = 18
b = "hello"
print(type(b))
###################### Arithmetic operations ######################
a = 10
b = 2
print("res = ",a + b)
print("res = ",a - b)
print("res = ",a * b)
print("res = ",a / b)
print("res = ",a // b)
print("res = ",a % b)
print("res = ",a ** b)
###################### Input funtion ######################
name = input("please enter your name: ")
print("welcome ",name)
num = input("please enter a number: ")
print("result = ", num * 5)
####################### converting to int #################
num2 = int(input("please enter a number: "))
print("result = ", num2 * 5)
#########################Strings###########################
#1. Concatenation using +
str1 = "Hello"
str2 = " World"
result = str1 + str2  # Combining the strings
print("result (+): ", result)

# 2. Repetition using *
str3 = "AIE! "
result = str3 * 3  # Repeating the string 3 times
print("result (*): ", result)

# 3. Indexing
str4 = "Hello, Python!"
first_char = str4[0]  # First character ('H')
last_char = str4[-1]  # Last character ('!')
substring = str4[7:13]  # Extracting a substring ('Python')
print("Indexing [0]:", first_char)
print("Indexing [-1]:", last_char)
print("Slicing [7:13]:", substring)

# 4. String Length
length = len(str4)
print("Length of string:", length)
############################ if statement ####################
testNum = int(input("pls enter a num: "))
if testNum > 0:
    if testNum%2 == 0:
        print("Even number")
    else:
        print("Odd number")
a = 1
b = 5
operation = '+'
res = 0
if operation == '+':
    res = a+b
elif operation == '-':
    res = a - b
elif operation == '*':
    res = a * b
elif operation == '/':
    res = a // b
print("result = ",res)
#########################Relational operators#########################
print(1 > 5)
print(1 < 5)
print(1 == 5)
print(1 != 5)
print("OMAR" == "omar")
print( 5 > 5)
print( 5 >= 5)
print( 3 <= 5)
##########################Logical operators ###########################
print(15 > 5 and 1 > 5)
print(15 > 5 or 1 < 5)
print(15 > 5 and 1 < 5)
print(15 < 5 or -1 > 4)
print(not 15 == 15)
print(not ( (13 == 13 and 11 < 100) or 17 < 30) )

