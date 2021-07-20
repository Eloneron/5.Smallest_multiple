"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# Works, but not elegant - to be improved.

divisors = [5,7,9,11,13,16,17,19]

for x in range(20,1000000000,20):
    num = x
    flag = True
    for y in divisors:
        if x % y == 0:
            x /= y
        else:
            flag = False
            break
    if x == 1 and flag == True:
        print(num)