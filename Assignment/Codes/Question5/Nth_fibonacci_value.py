# function defination:
def fibonacci(n):

    a, b = 0, 1

    if (n == 1):
        return 0

    elif (n == 2):
        return 1

    for i in range(n-2):
        temp = a + b
        a = b
        b = temp
    return temp


print(fibonacci(9))
