# arithmetic operator
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)  # returns a float
print(a%b)
print(a//b)   # returns a integer always rounds down
print(a**b)

# assignment operator
_a= 100
print(_a)

# addition assignment operator
_a+=100
print(_a)

# subtraction assignment operator
_a-=100
print(_a)

# multiplication assignment operator
_a*=100
print(_a)

# comparison operator
a=50
b=50
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b) 


# logical operator
# and or not
# and returns true if both operands are true
# or returns true if any of the operands are true
# not returns the opposite, if the operand is true, returns false
a=True
b=False
x= 10
print(x>5 and x<15)
print(x>5 or x<15)
print(a and b)
print(a or b)
print(not a)

# identity operators
# used to compare the objects, not if they are equal
# is, is not
v=['apple', 'banana', 'cherry']
w=['apple', 'banana', 'cherry']
u=v
print(v is w)
print(v is not w)
print(v is u)


# membership operator
# in, not in
# returns true if a sequence with the specified value is present in the object
x=['apple', 'banana', 'cherry']
print('banana' in x)
print('banana' not in x)