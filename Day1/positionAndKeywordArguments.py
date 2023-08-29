def sum_of(num1, num2, num3):
    return num1+num2+num3

a,b,c=1,2,3
print("Sum of a,b,c is: ",sum_of(a,b,c))

###########################

def total_score(math, science, english, kannada):
    print("Math: ",math,"Science: ",science,"English: ",english,"Kannada: ",kannada)
    return math+science+english+kannada

student1 = total_score(100,89,78,100) #positional arguments
student2 = total_score(kannada=99, english=90, science=95, math=100) #Keyword arguments
print("Student1: ",student1)
print("Student2: ",student2)

############################

def print_student_details(name, school, maths, physics, chemistry, biology):
    total = maths + physics + chemistry + biology
    print("Name: ", name)
    print("School: ", school)
    print("Total Marks: ", total)

print_student_details("Pruthvi","BIPS Bagalkot", maths=80,chemistry=90,physics=99,biology=85)

############################

num_list = [3,6,1,5,4,2]
print(sorted(num_list))
print(sorted(num_list, reverse=True))

############################

print("Alex", "Peter", "Greg")
print("Alex", "Peter", "Greg", sep=" | ")