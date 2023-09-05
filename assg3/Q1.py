'''
**kwargs in Python is used to pass a keyworded, variable-length argument list
'''

def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}")
student_data(1)
print()
student_data(2, student_name="Someone")
print()
student_data(3, student_name="Rahul", student_class="Class 12")