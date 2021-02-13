def decoretor_fun(original_fun):
    def wrapper_fun():
        return original_fun()
    return wrapper_fun
@decoretor_fun
def display():
    print('display funcation ran')
display()
print('Hello World and nothig')
