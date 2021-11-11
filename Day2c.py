#Three is a Crowd Part 1 + 2
def crowd_test(people):
    if(len(people) > 3):
        print("Room is Crowded")
    else:
        print("Not Crowded")

people = ["Bob", "Billy", "Sam", "Kevin"]

crowd_test(people)

people.pop(3)
people.pop(2)

crowd_test(people)


#Six is a mob
print("\n\n")

def mob_test(people):
    if(len(people) > 5):
        print("There is a mob")
    elif(len(people) >= 3):
        print("There is a crowd")
    elif(len(people) >= 1):
        print("Not Crowded")
    else:
        print("Room is empty")

people = ["Person1", "Person2", "Person3", "Person4", "Person5", "Person6"]

mob_test(people)

people.pop(5)
people.pop(4)

mob_test(people)

people.pop(3)
people.pop(2)

mob_test(people)

people.pop(1)
people.pop(0)

mob_test(people)



