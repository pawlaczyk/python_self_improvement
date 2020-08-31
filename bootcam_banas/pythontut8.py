# def change_name():
#     global gbl_name
#     gbl_name =  "Doug"
#
# gbl_name = "Tom"
# change_name()
# print(gbl_name)

# def is_float(str_val):
#     try:
#         float(str_val)
#         return True
#     except ValueError:
#         return False
#
# pi = 3.14
# print("is pi a float: ", is_float(pi))
# print("is pi a float: ", is_float(str(pi)))
# print("is pi a float: ", is_float("A"))
import re
def solve_eq(eq):
    left_side, right_side = eq.split("=")
    right_side = int(right_side.strip())
    num = re.split("\+|\*|\-|/", left_side)[-1]
    num = int(num.strip())

    result = None
    operator = None
    if "+" in eq:
        result = right_side - num
    if "-" in eq:
        result = right_side + num
    if "*" in eq:
        result = right_side / num
    if "/" in eq:
        result = right_side * num

    return "x = " + str(result)

print(solve_eq("x * 4 = 9"))
print(solve_eq("x - 4 = 9"))