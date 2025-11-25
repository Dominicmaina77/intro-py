_a = "hello world"
print(_a)

b = "python program"
print(b)

# strings are arrays
print(b[2])
print(b[6])
print(b[7])

# loop through a string
for x in "banana":
    print(x)

# slicing 
# from 2 chrarcter - 5th(not included) 
_word= 'Hello python'
print(_word[2:5])

# from beginning to 4th character(not included)
print(_word[:4])

# from 5th character to end
print(_word[5:])

# negative indexing
# from 5th character to 2nd
print(_word[-5:-2])

print(_word.upper())

print(_word.lower())

print(_word.strip())

print(_word.replace("H", "J"))

# concatenate strings
# use the + operator
a = "Hello"
b = "program"
c = a + " " + b
print(c)

# f strings
name = "John"
age = 36
txt = f"Hello {name}, you are {age} years old"
print(txt)

# placeholders and modifiers
# the format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

_price=99
_txt = f"For only {_price:.2f} dollars!"
print(_txt)
