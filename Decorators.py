
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

def upper_d(func):
    def inner():
        str = func()
        return str.upper()
    return inner



def split_d(func):
    def outer():
        str2 = func()
        return str2.split() 
    return outer        




@split_d
@upper_d
def ordinary():
    return "good morning"


print(ordinary())



