
# function Defination
def triple_and(first, second, third):
    result = first and second and third
    return result


x = triple_and(True, True, True)
print(x)  # True as all params are true

y = triple_and(True, True, False)
print(y)  # False as the third param is false
