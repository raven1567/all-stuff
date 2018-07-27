The purpose of this file is to provie examples of list and tuples concepts
to better understand how they work. Feel free to comment out code to test
something specific.
'''
################################################################################
'''
list.sort()
'''
#try this list as wellS
#list = [6,9,3,5,8,2]
list = ["poo", "amir", "learning", "coffee", "supercalifragilisticexpialidocious"]
print("Before: ", list)
#sorting numerically
list.sort()
print("After: ", list)

'''
weird thing 1: capital vs lowercase letters
'''
ew = ["poo", "amir","Divya","learning", "coffee", "supercalifragilisticexpialidocious"]
print("Before: ", ew)
ew[2].lower()
#ask jessica about lower and then sort
ew.sort()
print("After: ", ew)

'''
weird thing 2: sorting numbers and words
'''
poo = ["hello", 5,1,3, "everyone"]
print("Before: ", poo)
poo.sort()
print("After: ", poo)

'''
weird thing 3: sorting lists of lists
'''
addy = [["weird", "thing"], ["number", "3"], ["we", "will", "see!"]]
print("Before: ", addy)
addy.sort()
print("After: ", addy)

'''
side note: sorting the listtle lists and then the big another_one
'''
addy = [["weird", "thing"], ["number", "3"], ["we", "will", "see!"]]
print("Before: ", addy)
for little_list in addy:
    little_list.sort()
print("In between: ", addy)
addy.sort()
print("After: ", addy)

'''
list.reverse
'''
selah = ["reverse", "example", "test"]
print("Before: ", selah)
selah.sort(reverse = True)
print("After: ", selah)

'''
sorted()
-might not work because it might be a python 2 thing
'''
selah = ["zsorted", "example", "test"]
print("Before: ", selah)
sorted(selah)
print("After: ", selah)
#can also do
sorted(selah, reverse = True)
print("Another example: ", selah)
#to make everything in the list lowercase
print sorted(selah, key=str.lower)
print("Making lowercase: ", selah)

'''
slicing
'''
my_list = [1,2,3,4,5,6,7,8,9]
print("Before: ", my_list)
print("test 1: ",my_list[1:6])
print("test 2: ",my_list[:6])
print("test 3: ",my_list[4:])
print("test 4: ",my_list[1:8:2])
print("test 5: ",my_list[:6:3])
print("test 6: ",my_list[1::2])

'''
searching lists
'''
my_list =["people", "order", "our", "patties"]
result = my_list.index("people")
print(result)
alternate_result = my_list.index("hello")
print(hello)

'''
append and extend
'''
my_list = [1,2,3]
my_list.append(4)
print("First: ",my_list)

second = [5,6,7]
my_list.extend(second)
print("Second: ",my_list)

'''
tuples
'''
tup = (1,2,3)
tup2 = (5,6,7)
tup3 = tup+tup2
print(tup3)
tup4 = ([1,2,3],)
print(tup4)
del tup3


-list.sort()
    -sorting and saving the list without making a copy
    -faster
    -cannot retrieve original indexes
    -lets you be speicfic with sorted
        -list.sort(reverse = True)
        -list.sort(reverse = False)
        -key (sort by lower or upper case)
-sorted()
    -sorting the list and making a copy of the list

-slicing lists
    -cut off certain elements from list
    -can define a place to start and stop the slicing
    -you can also skip
    -does NOT change original list

-searching lists list.index("blah")
    -you can find stuff in a list
    -returns the index where the element is
    -otherwise, an error happens

-list.append() vs list.extend()
    -.append() adds value as one element
    -.extend() includes elements from a second list
    -list.append(["a",true]) will add as an element in the list
        -[["a", true], something_else, another_one]

-tuples
    -like a list
    -parenthesis instead of square brackets
    -unchangeable == immutable
    red = (255,0,0)
    tup = (1,2,3)
    list = [1,2,3]
    -can delete tuples and add them
    -adding tuples is solely for the purpose of updating the tuple
    
