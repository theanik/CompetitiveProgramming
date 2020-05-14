my_list = [0, 1, 2, 3, 4, 5]

for item in my_list:
    print("Item : "+str(item))

my_list = [0, 1, 2, 3, 4, 5]

for i,item in enumerate(my_list):
    print("Item : "+str(i)+" = "+str(item))

family = ['anik','mona','rajdon','halim']

for i,data in enumerate(family):
    print(str(family[i])+" = "+str(data))


my_dict = {'a': 'jill', 'b': 'tom', 'c': 'tim'}
for key in my_dict:
    print(key + ', ' + my_dict[key])


my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)



def smallest_positive(in_list):
    sm = None
    for num in in_list:
        if num > 0:
            if sm == None or num < sm:
                sm = num
    return sm
# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))

def smallest_nagetive(list_):
    sn = None
    for num in list_:
        if num < 0:
            if sn == None or num > sn:
                sn = num
    return sn

print(smallest_nagetive([4, -6, 7, 2, -4, 10]))



courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


def when_offered(courses, course):
    data =[]
    for ckey in courses:
        for key in courses[ckey]:
            if key == course:
                data.append(ckey)

    return data



print(when_offered(courses, 'cs101'))
# Correct result: 
# ['fall2020', 'spring2020']