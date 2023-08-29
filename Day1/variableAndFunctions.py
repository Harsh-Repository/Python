def my_introduction(name, place, profession):
    print("My name is", name)
    print("I live in", place)
    print("I am a", profession, "and I love what I do!")

name = input("Enter your name: ")
place = input("Enter your place: ")
profession = input("Enter your profession: ")

my_introduction(name, place, profession)
print("This is my python function practice code")
#####################
def will_work_function():
    print("This is all right!")
    if (10>5):
        print("Well 10 is indeed greater than 5")

will_work_function()
#####################
def a_more_complecated_function():
    for i in range (10):
        print("i is now: ", i)

a_more_complecated_function()