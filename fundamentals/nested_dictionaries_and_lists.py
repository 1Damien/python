x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def iterate_dictionary(students):
    for names in students:
        print(f"first_name - {names['first_name']}, last_name - {names['last_name']}")

iterate_dictionary(students)
print()

def iterate_dictionary2(first_name, students):
    for names in students:
        print(names[first_name])

iterate_dictionary2('first_name', students)
print()

def iterate_dictionary3(last_name, students):
    for dictionary in students:
        print(dictionary[last_name])

iterate_dictionary3('last_name', students)
print()

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def print_info(dojo):
    for locations, instructors in dojo.items():
        print(f"{len(instructors)} {locations}")
        for item in instructors:
            print(item)
        print()

print_info(dojo)


