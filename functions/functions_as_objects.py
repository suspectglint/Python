#All functions are first-class objects in python.
#what are first-class objects? difference between objects and first-class objects?

#Simple Function
def display(msg):
    return "Hello "+msg

#Function defined inside another function
def display1(msg):
    def inner_display():
        return "Hey there! How are you doing "
    return inner_display()+msg

#Function passed as a parameter
def display2(msg):
    return msg + "How is it going?"
def fn_as_param():
    return "Hey there litle fella! "

#Function as a return value and after return it needs to be called with parentheses
def display3():
    def inner_display1():
        return "Shotgun sucker!"
    print("Id = ",id(inner_display1))
    return inner_display1

#<class 'function'>
print(type(display),id(display))

#<class 'builtin_function_or_method'>
print(type(id),type(print))

#Various function calls
print(display('Gopi'))
print(display1('Gopi'))
print(display2(fn_as_param()))
fn_as_return_value=display3()
print(fn_as_return_value())
#when display3() returns a function and it is directly called
print(display3()())