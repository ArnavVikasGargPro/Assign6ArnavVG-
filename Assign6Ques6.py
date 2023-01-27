'''Ques6-Write a Python function student_data () which will print the id of a student (student_id). 
If the user passes an argument student_name or student_class the function will print the 
student name and class.'''
#22105015
def student_data(student_id, student_name=None, student_class=None):
    if student_name and student_class:
        print('Student ID: {}'.format(student_id))
        print('Student Name: {}'.format(student_name))
        print('Student Class: {}'.format(student_class))
    else:
        print('Student ID: {}'.format(student_id))
#arnav Vikas Garg
student_data(1, 'John', 'A')
# Output:
# Student ID: 1
# Student Name: John
# Student Class: A

student_data(2)
# Output:
# Student ID: 2
