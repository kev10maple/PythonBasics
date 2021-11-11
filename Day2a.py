import re

print("Question 1: ")
print("Hello World"[8])

print("\nQuestion 2: ")
print("thinker"[2:5])

print("\nQuestion 3: ")
print("hello"[1]) #outputs the letter 'e'
print("Sammy"[2:]) #outputs 'mmy'

print("\nQuestion 4: ")
print(set("Mississippi"))

def isPalindrome():
    count = int(input("\ninput data: "))

    phrases = []
    for i in range(count):
        phrases.append(input())

    results = []

    for phrase in phrases:
        simplifiedWord = re.sub('[^A-Za-z0-9]', '', phrase).lower()

        if simplifiedWord == simplifiedWord[::-1]:
            results.append('Y')
        else:
            results.append('N')

    print(results)

if __name__ == "__main__":
    isPalindrome()


