import random

#Question 1
def multiples():
    nums = []

    for i in range(1500, 2701):
        if i % 7 == 0 and i % 5 != 0:
            nums.append(i)

    print(','.join([str(n) for n in nums]))

multiples()

#Question 2
print("\n\n")

def farenheit_to_celcius(num):
    return (num - 32) * 5 / 9

def celcius_to_farenheit(num):
    return num * 9 / 5 + 32

print(farenheit_to_celcius(45))
print(celcius_to_farenheit(60))

#Question 3
print("\n\n")
r = random.randint(1, 9)

while True:
    num = int(input("Guess a number: "))
    if(num == r):
        print("Well Guessed!")
        break
    else:
        print("Incorrect")

#Question 4/5
print("\n\n")

for i in range(0, 9):
    line = ''
    for j in range(0, 5 - (abs(4 - i))):
        line += '*'
    print(line)


#Question 6
print("\n\n")

word = input("Enter word: ")
print(word[::-1])

#Question 7
print("\n\n")

def even_odd(nums):
    even = 0
    odd = 0

    for n in nums:
        if(n%2 == 0):
            even += 1
        else:
            odd += 1

    print("Number of even numbers: " + str(even))
    print("Number of odd numbers: " + str(odd))

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even_odd(nums)

#Question 8
print("\n\n")

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for d in datalist:
    print("{}: {}".format(type(d), d))

#Question 9
print("\n\n")

output = ''

for i in range(0, 7):
    if i == 3 or i == 6:
        continue
    output += str(i) + ' '

print(output)





