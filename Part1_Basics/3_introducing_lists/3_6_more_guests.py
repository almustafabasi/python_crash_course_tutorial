"""
3-6. More Guests: 
You just found a bigger dinner table, so now more space is available. Think of 
three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print statement 
to the end of your program informing people that you found a bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list.
"""

dinner_list = ['dad', 'mom', 'musab']

dinner_list.insert(0, 'aymen')
dinner_list.insert(2, 'omy')
dinner_list.append('myamen')
print(dinner_list)

print("Hi "+ dinner_list[0].title(), ", will you join me for the dinner today?")
print("Hi "+ dinner_list[1].title(), ", will you join me for the dinner today?")
print("Hi "+ dinner_list[2].title(), ", will you join me for the dinner today?")
print("Hi "+ dinner_list[3].title(), ", will you join me for the dinner today?")
print("Hi "+ dinner_list[4].title(), ", will you join me for the dinner today?")
print("Hi "+ dinner_list[5].title(), ", will you join me for the dinner today?")
