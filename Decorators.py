# Any callable python objects that is used to modify a function or a class 


# function decorators and class decorators


from unittest import result


# def outer():
#     x = 3
#     def inner():
#         y = 3
#         result = x + y 
        
#         return result
#     return inner

# a = outer()
# print(a())        


# ======================================


# def function():
#     print("hi am function 1")

# def fuction2(fun):
#     print("hi am fuchtion 2")
#     fun()

# fuction2(function)       


# ======================================


# def all(fun):
#     def inner():
#         str =fun()
#         return str.upper()
#     return inner    

# def print_str():
#     return "Abhijith"

# print(print_str())

# d = all(print_str)
# print(d())
# ======================================


def all(fun):
    def inner():
        str =fun()
        return str.upper()
    return inner()   

@all
def print_str():
    return "Abhijith"

print(print_str)

                #   =====================| 1  |



# ======================================
