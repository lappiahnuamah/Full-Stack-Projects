#####################################
#### PART 6: EXERCISE REVIEW  #######
#####################################

# Time to review all the basic data types we learned! This should be a
# relatively straight-forward and quick assignment.

###############
## Problem 1 ##
###############

# Given the string:
s = 'django'

# Use indexing to print out the following:
# 'd'
print(s[0])

# 'o'
print(s[-1])
# 'djan'
print(s[:4])
# 'jan'
print(s[1:4])
# 'go'
print(s[4:])

print(s[::-1])
# Bonus: Use indexing to reverse the string


###############
## Problem 2 ##
###############

# Given this nested list:
l = [3,7,[1,4,'hello']]
# Reassign "hello" to be "goodbye"
l[2][2]="goodbye"
print(l)

###############
## Problem 3 ##
###############

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
print(d1['simple_key'])

d2 = {'k1':{'k2':'hello'}}
print(d2['k1']['k2'])

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


###############
## Problem 4 ##
###############

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
converted = set(mylist)
print(converted)

###############
## Problem 5 ##
###############

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
# "Hello my dog's name is Sammy and he is 4 years old"
sentence = "Hello my dog's name is {name} and he  is {age} years old".format(name=name, age=age)
print(sentence)


# lambda expression

mylist = [1,2,3,4,5,6,7,8]

# def even_bool(num):
#     return num%2==0

# evens = filter(even_bool, mylist)
# print(list(evens))

lambda num:num%2==0

evens = filter(lambda num:num%2==0, mylist)
print(list(evens))

