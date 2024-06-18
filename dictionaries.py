student={'name':'john','age':20,'grade':'A'}
print(student['name'])
student['age']=21
print(student)
student['city']='New york'
print(student)
del student['grade']
print(student)
print(student.keys())