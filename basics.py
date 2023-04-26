# builld madlibs in python
'''color = input('enter a color: ')
plural_noun = input('enter a plural noun: ')
adjective = input('enter an adjecrive: ')
print('trees are '+color)
print(plural_noun +' are mean')
print('please keep it '+ adjective)'''

# lists
from multiprocessing import Manager, managers


x = [1,2,3,4,'ali', 'abu basem']
z = [5,6,7,'hello world', 'mohammed']
x.append(z)
x.insert(0,'hello')
x.remove('abu basem')
x.pop()
print(x)
x.clear()
print(x)
print(z.index(5))
print(z)
print(z.count(7))
y = z.copy()
print(y)
print(z)
print()

# tuples          tuples does not support item assignment
coor = (23,45)   # use it if you no want to change the coor
print(coor)
print()

# python funcs
def say_hi(name, age):
    print('hello', name, 'your age is',age)
say_hi('islam',25)
print()

# return
def cube(num):
    return num*num*num
ra = cube(4)
print(ra)
print(cube(3))
print()

def sum(num1,num2):
    return num1+num2
print(sum(3,5))
print()

# python comparisons
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1 
    elif num2 >= num1 and num2 >= num3:
        return num2 
    else:
        return num3
print(max_num(54,65,34))
print(max(34,45,756,32,3434,4534))
print()

# while loop
i = 1 
while i <= 10:
    print(i)
    i += 1
else:
    print('the condition is not true')
print('the loop has ended')
i = 1 
while i <= 10:
    i += 1
    if i == 6:
        continue
    print(i)
print('hello world')
i = 1 
while i <= 10:
    i += 1
    if i == 6:
        break
    print(i)
print()

# for loop
buddies = ['pikachu', 'grandizer','subzero','winner']
for i in buddies:
    print(i)
print()
for x in range(5):
    print(x)
print()
for u in range(len(buddies)):
    print(u)
    print(buddies[u])
print()
for o in range(10):
    if o % 2 == 0:
        print(o,'is an even number')
    else:
        print(o, 'is an odd number')
print()
for b in range(len(buddies)):
    if buddies[b] == 'winner':
        print(b, 'is the winner')
    else:
        print(b, 'is not the winner')
print()
# exponent function
def power(baseNum, powNum):
    result = 1
    for i in range(powNum):
        result = result * baseNum
    return result
print(power(3,3))
print()

# 2D lists
numList = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(numList[2][1])
for r in numList:
    for column in r:
        print(column*2)
print()

# python errors
'''try:
    value = int(input('enter a number: '))
    print(value)
    result = 10 / 0
except ZeroDivisionError:
    print('you cannot divide by zero')
except:
    print('invalid input')
print('success')'''
print()

# classes & opjects
class employee:
    def __init__ (self, name, age, department, is_manager, rating):
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
employee1 = employee('islam', 50, 'codezilla', True, 5)
employee2 = employee('ali', 39, 'facebook', False, 3.5)
print(employee1.age)
print()

# class func
'''def is_good (self):
    if self.rating >= 4.5:
        return True
    else :
        return False
print(employee1.is_good())
print(employee2.is_good())'''


