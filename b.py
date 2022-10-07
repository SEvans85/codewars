

#You are given a string containing a sequence of character sequences separated by commas.

#Write a function which returns a new string containing the same character sequences except the first and the last ones but this time separated by spaces.

#If the input string is empty or the removal of the first and last items would cause the resulting string to be empty,
#return an empty value (represented as a generic value NULL in the examples below).


def array(string):
    new_string = ''
    a = string.split(',')
    del a[0]
    del a[-1]
    list_to_str = ' '.join([str(i) for i in a])
    print(list_to_str)

abc = '1,2,3,4,5,6'
array(abc)

