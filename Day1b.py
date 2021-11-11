import math

print('Question 1: ')
print (50+50)
print (100-10)

print('\nQuestion 2: ')
print(30+6)
print(6^6)
print(6**6)
print(6+6+6+6+6+6)

print('\nQuestion 3: ')
print('Hello World')
print('Hello World : 10')

print('\nQuestion 4: ')
def calculatePayment(P, R, L):
    #P is loan size
    #R is interest rate IN DECIMAL
    #L is length of time to pay out (Months)

    #formula:
    #Monthly Payment M = P[R(1+R)^L] / [(1+R)^L - 1]
    interest = R / 12
    return (P * (interest * ((1 + interest) ** L))) / (((1 + interest) ** L) - 1)

payment = math.ceil(calculatePayment(800000, 0.06, 103))

print('Monthly Payment: ' + str(payment))

