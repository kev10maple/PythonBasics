#Question 1+2: Based on instructors revision of the problem
#Output: (OrderNumber, Quantity*Price per Item)

accounting = [[34587, "Learning Python, Mark Lutz", 4, 40.95],
              [98762, "Programming Python, Mark Lutz", 5, 56.80],
              [77226, "Head First Python, Paul Barry", 3, 32.95],
              [88112, "Einfuhrung in Python3, Bernd Klein", 3, 24.99]]

def get_data(info):
    return list(map(lambda x : (x[0], x[2]*x[3]), info))

print(get_data(accounting))


#Question 3
accounting2 = [34587,("Learning Python, Mark Lutz", 4, 40.95),
               98762,("Programming Python, Mark Lutz", 5, 56.80),
               77226,("Head First Python, Paul Barry", 3, 32.95),
               88112,("Einfuhrung in Python3, Bernd Klein", 3, 24.99)]

def get_data2(info):
    info2 = zip(info[::2], info[1::2])
    return list(map(lambda x : (x[0], x[1][1]*x[1][2]), info2))

print(get_data2(accounting2))

