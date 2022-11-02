"""
3-10. Every Function: 
Think of something you could store in a list. For example, you could make a list 
of mountains, rivers, countries, cities, languages, or anything else you’d like. 
Write a program that creates a list containing these items and then uses each 
function introduced in this chapter at least once.
"""

sudan_cites = ['nyala', 'khartoum', 'madani', 'portsudan', 'kasala']
print(sudan_cites)

sudan_cites.sort()
print(sudan_cites)

sudan_cites.sort(reverse = True)
print(sudan_cites)

sudan_cites.reverse()
print(sudan_cites)

list_length = len(sudan_cites)
print(list_length)
