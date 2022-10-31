# Write a program that takes a date as input and outputs the date's season in the northern hemisphere. 
# The input is a string to represent the month and an int to represent the day.
# In addition, check if the string and int are valid (an actual month and day).

m = input()
d = int(input())

if m == "March" and d >= 20 and d < 31:
    
    print('Spring')
    
elif m == "June" and d > 0 and d <= 20:
    
    print('Spring')
    
elif m == "April" and d > 0 and d <= 30:

    print('Spring')
    
elif m == "May" and d > 0 and d <= 31:
    
    print('Spring')
    
elif m == "June" and d >= 21 and d <= 30:
    
    print('Summer')
    
elif m == "September" and d > 0 and d <= 21:
    
    print('Summer')
    
elif m == "July" and d > 0 and d <= 31:
    
    print('Summer')
    
elif m == "August" and d > 0 and d <= 31:
    
    print('Summer')
    
elif m == "September" and d >= 22 and d <= 30:
    
    print('Autumn')
    
elif m == "December" and d > 0 and d <= 20:
    
    print('Autumn')
    
elif m == "October" and d > 0 and d <= 31:
    
    print('Autumn')
    
elif m == "November" and d > 0 and d <= 30:
    
    print('Autumn')
    
elif m == "December" and d >= 21 and d <= 31:
    
    print('Winter')
    
elif m == "March" and d > 0 and d <= 19:
    
    print('Winter')
    
elif m == "January" and d > 0 and d <= 31:
    
    print('Winter')
    
elif m == "February" and d > 0 and d <= 28:
    
    print('Winter')

else:
    
    print('Invalid')
    
    


    
    