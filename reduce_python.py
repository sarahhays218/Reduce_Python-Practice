# Given a list of letters, use the reduce() higher-order function with a lambda function to combine the letters into a single word: 

letters = ['r', 'e', 'd', 'u', 'c', 'e']

# remember to import the reduce function
from functools import reduce

# store the result of your reduce function in the variable word

word = reduce(lambda x,y: x+y, letters)

# print word

print(word)