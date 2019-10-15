#!/usr/bin/python3.6

#create a list for user input
user_input = input('Enter element in list : using space ')
list  = user_input.split(',')

#creating vowels string
vowels=['a','A','e','E','i','I','o','O','u','U']

new_list_vowels=[]
for i in range(len(user_input)):
    for j in range(len(vowels)):
        if user_input[i]==vowels[j]:
            new_list_vowels.append(user_input[i])

#removing data from list
res = []
for k in new_list_vowels:
    if k not in res:
        res.append(k)
print('Remove redundant list elements: {}'.format(res))
