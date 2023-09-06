'''
Print student information based on the provided arguments.
'''

def student_data(student_id, student_name=None, student_class=None):
    output = []

    output.append(f"Student ID: {student_id}")
    
    if student_name:
        output.append(f"Student Name: {student_name}")
    
    if student_class:
        output.append(f"Student Class: {student_class}")

    return "\n".join(output)

if __name__ == '__main__':
    print(student_data(101))
    print(student_data(102, "Rahul"))
    print(student_data(103, "Roy", "XI"))