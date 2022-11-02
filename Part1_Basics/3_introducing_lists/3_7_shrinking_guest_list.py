"""
3-7. Shrinking Guest List: 
You just found out that your new dinner table won’t arrive in time for the dinner, 
and you have space for only two guests.
• Start with your program from Exercise 3_6. Add a new line that prints a message 
saying that you can invite only two people for dinner.
"""

dinner_list = ['dad', 'mom', 'musab']

dinner_list.insert(0, 'aymen')
dinner_list.insert(2, 'omy')
dinner_list.append('myamen')
print(dinner_list)

print("Only two people can be invited for dinner.\n")

"""
• Use pop() to remove guests from your list one at a time until only two names remain 
in your list. Each time you pop a name from your list, print a message to that person 
letting them know you’re sorry you can’t invite them to dinner.
"""

name1 = dinner_list.pop()
print(name1.title() + " Sorry you are not invited to dinner.")

name2 = dinner_list.pop()
print(name2.title() + " Sorry you are not invited to dinner.")

name3 = dinner_list.pop()
print(name3.title() + " Sorry you are not invited to dinner.")

name4 = dinner_list.pop()
print(name4.title() + " Sorry you are not invited to dinner.\n")

"""
• Print a message to each of the two people still on your list, letting them know 
they’re still invited.
"""

print(dinner_list[0].title() + " you are still invited to dinner.")
print(dinner_list[1].title() + " you are still invited to dinner.\n")

"""
• Use del to remove the last two names from your list, so you have an empty list. 
Print your list to make sure you actually have an empty list at the end of your program.
"""

del(dinner_list[:])
print(dinner_list)
