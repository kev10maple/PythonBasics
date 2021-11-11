print("Question 1: ")
test = [1, "Hello", 5.55]
print(test)

print("\nQuestion 2: ")
test = [1, 1, [1, 2]]
print(test[2][1])

print("\nQuestion 3: ")
test = ['a', 'b', 'c']
print(test[1:]) #would output ['b', 'c']

print("\nQuestion 4: ")
week = {"monday":1, "tuesday":2, "wednesday":3, "thursday":4, "friday":5, "saturday":6, "sunday":7}
print(week)

print("\nQuestion 5: ")
d = {'k1':[1, 2, 3]} #would output 2
print(d['k1'][1])

print("\nQuestion 6: ")
test = [1, [2, 3]]
print(tuple(test))

print("\nQuestion 7: ")
test = set('Mississippi')
print(test)

print("\nQuestion 8: ")
print(test.add('X'))

print("\nQuestion 9: ")
print(set([1, 1, 2, 3]))
print("\n\n")

#######################################################
print("Question 1: ")
def multiples():
    nums = []

    for i in range(2000, 3201):
        if i%7 == 0 and i%5 != 0:
            nums.append(i)

    print(', '.join([str(n) for n in nums]))

multiples()

#######################################################
print("\n\nQuestion 2: ")
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(int(input("Enter number: "))))

#######################################################
print("\n\nQuestion 3: ")
def squares(n):
    d = dict()

    for i in range(1, n+1):
        d[i] = i*i

    return d

num = int(input("Enter a number: "))
print(squares(num))

#######################################################
print("\n\nQuestion 4: ")
nums = input("Enter numbers separated by commas: ")
myList = list(nums.split(","))
myTuple = tuple(myList)
print(myList)
print(myTuple)

#######################################################
print("\n\nQuestion 5: ")
class InputOutString(object):

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())

ioString = InputOutString()
ioString.getString()
ioString.printString()