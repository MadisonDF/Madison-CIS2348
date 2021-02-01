# Madison Fletcher
# 1868748

print('Birthday Calculator')
print('Current Day')
month = int(input("Month:"))
day = int(input('Day:'))
year = int(input("Year:"))
print('Birthday')
month1 = int(input('Month:'))
day1 = int(input('Day:'))
year1 = int(input('Year:'))
age = (year -year1) - 1
age2 = year - year1
if month < month1:
    print('You are', age, 'years old.') # if month < month1 then your birthday hasn't passed the current date yet
    # If your birthday hasn't passed the current date then to get your age you need to subtract the current year by
    # your birthday year then after that subtract one more
elif month > month1:
    print('You are', age2, 'years old.') # if month > month1 then your birthday has already passed the current date
    # If your birthday has passed the current date then you just subtract the current year from your birthday year
else:
    print('Happy Birthday!')
