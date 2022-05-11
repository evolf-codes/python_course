#import pdb; pdb.set_trace()

# def divide(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         return ('CAN NOT DIVIDE BY 0')
#     except TypeError as err:
#         return ('a or b must be numbers')
#         print(err)
#     finally:
#         print("this runs not matter what")


# print((divide(1,2)))
# print((divide(1,0)))
# print((divide(1,'a')))


def divide(num1,num2):
    try:
        return int(num1/num2)
    except TypeError:
        return ("Please provide two integers or floats")
    except ZeroDivisionError:
        return ("Please do not divide by zero")
print(divide(4,2))
print(divide([],"1"))
print(divide(1,0))