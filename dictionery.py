student = {
    "name":"pretty",
    "age": "20",
    "class":"10",
    "dob":"2005-01-18"
}
print(student)
print(student["age"])
student["school"]=" ABC school"
student["age"]=19
print(student)

del student ["class"]
print(student)

print(student.keys())

print(student.items())

#to convert dict into tuple
my_tuple =tuple(student.items())
print(my_tuple)

#to convert tuple into dict.
my_tuple =(('name' ,'ram'),('age','20'), ('class','10'))
my_dict =dict(my_tuple)
print(my_dict)


#to convert dict into list
my_list =list(student.items())
print(my_list)



