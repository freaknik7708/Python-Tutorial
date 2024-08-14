#for loop
'''For loop is used inmany different ways. For loop is mainly used when you're using iterables. So, when for loop is used, we always check for iterables.
So, there are so many ways to use for loop.'''
#1
'''a=[1,2,3]
for i in a: #iterates over each element in the list a
    print(i)''' #prints each item

#2
'''for i in range(10): #iterates over each number from 0 to 10(not included)
    print(i)'''

#3 - enumerate
'''a=['c','h','a','k','r','i']
for i,val in enumerate(a): #enumerate is a built-in Python function that allows you to loop over an iterable (like a list or string) while keeping track of the index of the current item.
    print(f'{i} index: value {val}')''' #so, here it prints index with value

"""
    0 index: value c
    1 index: value h
    2 index: value a
    3 index: value k
    4 index: value r
    5 index: value i
    """
#4 -zip
'''x=[1,2,3,4,5]
y=['a','b','c','d','e']

for i,j in zip(x,y): #zip is a built-in function that takes two or more iterables and returns an iterator of tuples, where the first element of each tuple comes from the first iterable, the second element comes from the second iterable, and so on.
    print(f'{i}:{j}')'''
'''
1:a
2:b
3:c
4:d
5:e
'''

#5- Zip + enumerate

'''students=['a','b','c']
marks=[83,90,96]

for i,(s,m) in enumerate(zip(students,marks)):
    print(f'{i+1} s.no: student-{s} marks-{m} ')

1 s.no: student-a marks-83 
2 s.no: student-b marks-90 
3 s.no: student-c marks-96 '''

