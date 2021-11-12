def calcBMI(h, w):
    return w / (h**2)

def getBMI(h, w):
    bmi = calcBMI(h, w)

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    result = ""

    numPeople = int(input("Enter number of people: "))

    for i in range(0, numPeople):
        data = input("Enter weight in kg space height in meters: ")
        weight = int(data.split()[0])
        height = float(data.split()[1])

        result += getBMI(height, weight)

    print("\n\nanswer:")
    print(result)

if __name__ == "__main__":
    main()


