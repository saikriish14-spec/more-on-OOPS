class Employee:

    def __init__(self):
        print("Employee cretaed")


    def __del__(self):
        print("destructor called")

def Create_obj():
    print("Making object...")
    obj = Employee()
    print("function end...")
    return obj



print("Calling Create_obj() function...")
obj = Create_obj()
del obj
print("Program end..")