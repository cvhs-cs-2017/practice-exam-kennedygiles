"""Use the range function to print the numbers from 1-20"""

x = 0
for i in range(1,21):
    x = x + i
    print(i)


"""Repeat the exercise above counting by 2's"""

x = 0
for i in range(2,21,2):
    x = x + i
    print(i)

"""Print all the multiples of 5 between 10 and 200 in DECENDING order"""
x = 0
for i in range(200,5,-5):
    x = x + i
    print(i)
