"""
Question 2
Question 2 (a)
Create the simple class below, using your function above. Following the example for Question 1 value will be 159, approx._value will be 12. The function calculate_square_root will be your function returning the square root.

Question 2 (b)
Write a simple program that uses your class above.
"""
import math


class SquareRoot:


    def calculate_square_root(self, N):
        n = N
        # precision
        precision = 10 ** (-10)
        while abs(N - n * n) > precision:
            n = (n + N / n) / 2
        return n


root = SquareRoot()
square_root = root.calculate_square_root(159)
approx_value = math.floor(square_root)
# print(type(approx_value))
print("approximate value of square root is: ", approx_value)
