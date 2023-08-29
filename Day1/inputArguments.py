def my_introduction(name, place):
    print("Hello, my name is", name)
    print("I live and work in", place)

name = input("name:")
place = input("place:")
my_introduction(name, place)
#####################
num1 = 25
another_num=10
def square(x):
    print("Square of", x ,"is", x*x)
square(num1)
square(another_num)
#####################

def my_savings(a,b):
    print("My total savings:", int(a)-int(b))

salary=input("Salary: ")
expenses=input("Expenses: ")
my_savings(salary,expenses)

#######################

def print_many_timeswith_doc(string, times):
    """""Lorem ipsum dolor sit amet consectetur adipisicing elit. Sapiente
        consequatur doloribus unde praesentium ipsum mollitia sint accusantium
        harum itaque incidunt earum, quod non deserunt at facere, nemo voluptate
        iste dolore aliquam. Minus nesciunt facilis suscipit quaerat libero!
        Ipsam sapiente maxime eum dicta fuga, consequatur iure perferendis ab
        odio quibusdam alias quasi, eveniet non repudiandae itaque cumque saepe
        impedit error voluptate? Quod, officia vitae. Rem est obcaecati ut
        doloribus praesentium voluptate quae cum modi, neque nesciunt. Nostrum
        hic repudiandae cumque ducimus vero modi quam architecto est commodi
        cupiditate, deleniti unde adipisci labore tempore et."""
    for i in range(times):
        print(string)

print(print_many_timeswith_doc.__doc__)