#Question 1
def func():
    print("Hello World")

func()


#Question 2
print("\n\n")

def func1(name):
    print(f"Hi My name is {name}")

func1("Google")


#Question 3
print("\n\n")

def func3(x, y, z):
    if z:
        return x
    else:
        return y

print(func3("hello", "goodbye", False))

#Question 4
print("\n\n")

def func4(x, y):
    return x * y

print(func4(2, 3))

#Question 5
print("\n\n")

def is_even(num):
    return num%2 == 0

print(is_even(3))

#Question 6
print("\n\n")

def is_greater(x, y):
    return x > y

print(is_greater(3, 2))

#Question 7
print("\n\n")

def total_sum(*args):
    return sum(args)

print(total_sum(1, 2, 3, 4, 5))

#Question 8
print("\n\n")

def even_only(*args):
    evens = []
    for a in args:
        if is_even(a):
            evens.append(a)
    return evens

print(even_only(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#Question 9
print("\n\n")

def camel_case(word):
    answer = []
    count = 0

    for w in word:
        if is_even(count):
            answer.append(w.upper())
        else:
            answer.append(w.lower())
        count += 1

    return ''.join(answer)

print(camel_case("Hello World"))

#Question 10
print("\n\n")

def parity(x, y):
    if is_even(x) and is_even(y):
        return min(x, y)
    else:
        return max(x, y)

print(parity(2, 4))

#Question 11
print("\n\n")

def first_letter(x, y):
    if x[0] == y[0]:
        return True
    else:
        return False

print(first_letter("Hello", "Hi"))

#Question 12
#Instructed by instructor to skip question 12 due to poor wording of the question


#Question 13
print("\n\n")

def capitalize(s):
    return s[0].upper() + s[1:3] + s[3].upper() + s[4:]

print(capitalize("hello"))





