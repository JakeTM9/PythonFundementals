
"""
Order of operations (PEMDAS)
() (Parentheses)
** (Exponent)
~ + - (unary operations)
* / % // (Division, Multiplication)
+ - (Addition, Subtraction)
>> << (shift bitwise)
& (And bitwise)
^ | (NOT, OR bitwise)
<= < > >= (comparison)
<> == != (equality)
= %= /= //= -= += *= **= (assignment)
"""

amount = 163400
time = 57.5

rate = amount / time
print('Rate: ' + str(rate))

bits = 16
size = 2 ** 16
print('size: ' + str(size))

print('11 // 3: ' + str(11 // 3))  # integer division
print('11 / 3: ' + str(11 / 3))  # float division
print('11 % 3: ' + str(11 % 3))  # modulus = remainder
#  print('11 / 0: ' + str(11 / 0))   #div by zero - error

#PEDMAS?
print(10 - 2 ** 2 / 2 + 5)