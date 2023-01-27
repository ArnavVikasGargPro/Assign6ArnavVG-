'''Ques7--Write a Python program to create two empty classes, Student and Marks. Now create 
some instances and check whether they are instances of the said classes or not. Also, 
check whether the said classes are subclasses of the built-in object class or not'''
class Student:
    pass
class Marks:
    pass
std1 = Student()
mrk1 = Marks()
print(isinstance(std1, Student))
print(isinstance(mrk1, Marks))
print(issubclass(Student, object))
print(issubclass(Marks, object))

# Output
# True
# True
# True
# True
