def document_function():
    """This function does something that is well documented"""
    print("Hello")

print(document_function)
print(document_function.__doc__)

another_function = document_function
print(another_function())
#####################
name = "Harshit"
city = "Bengaluru"

def introduction():
    print("My name is:", name)
    print("I live in:", city)

introduction()