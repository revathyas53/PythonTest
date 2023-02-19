"""
Question 1
@Question 1 (a)
Iteration can be used to calculate the square root of a number using the following steps.
Start with N the number whose square root is requested.
Divide this by n  an approximate root of N.
Take the mean of the quotient and the approximate root.
The formula would be .
The result of this becomes the new approximate value.
Repeat step 2. If the quotient is equal to approximate value used, then you have found the square root.
For example, to find the square root of 159.

@Question 1 (b) Create a list with 159, 3400, 67, 598 and 8999. Write some code to create a new list of square roots
using this list as input. You can use your function from Question 1 (a). @Question 1 (c) Using the list, 159, 3400,
67, 598 and 8999 create a list of tuples. Each tuple should have the value and its square root. If possible,
use named tuples as bonus.

"""


# Answer for Question 1 (a)
# function which return square root using formula (n+n/N)/2
def square_root(N):
    n = N
    # precision
    precision = 10 ** (-7)
    while abs(N - n * n) > precision:
        n = (n + N / n) / 2
    return n


'''
#Question 1 (c)
#A function which created List of tuble, Each tuple having the value and its square root
def tuple_of_SqrRoot(l):
    bonus=[]
    for i in l:
        root=round(squareRoot(i),8)
        bonus.append((i,root))
    #print(f"List of tuble, Each tuple having the value and its square root: \n{bonus}")
    return bonus
'''

if __name__ == "__main__":

    # list of values to find square root
    lst = [159, 3400, 67, 598, 8999]
    sqr_rt = []
    bonus = []
    # Question 1 (b)
    for i in lst:
        root = round(square_root(i), 8)
        # print(f"Square root of {i} is {root}")
        sqr_rt.append(root)

        # Question 1 (c)
        bonus.append((i, root))

    print(f"List of square root for given list of values are : \n{sqr_rt}")
    print(f"List of tuple, Each tuple having the value and its square root: \n{bonus}")
