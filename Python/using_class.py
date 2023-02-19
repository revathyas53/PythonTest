from ques_two import SquareRoot

lst = [12, 45, 60, 100]
bonus = []
for i in lst:
    x = SquareRoot().calculate_square_root(i)
    bonus.append((i, x))
    if x == 10:
        print(f"Square root of 10 is in {lst.index(i)} in the given list")
print(f"list of square root of given values \n{bonus}")
