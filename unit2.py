# User Instructions
# 
# Write a function 'sub1' that, given a 
# string, embeds that string in 
# the string: 
# "I think X is a perfectly normal thing to do in public."
# where X is replaced by the given 
# string.
#

given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
    return given_string %s


# sub1("running") 
# => "I think running is a perfectly normal thing to do in public."    
# sub1("sleeping") 
# => "I think sleeping is a perfectly normal thing to do in public."

# User Instructions
# 
# Write a function 'sub2' that, given two 
# strings, embeds those strings in the string: 
# "I think X and Y are perfectly normal things to do in public."
# where X and Y are replaced by the given 
# strings.
#

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
    return given_string2 % (s1, s2)
    

# sub2("running", "sleeping") 
# => "I think running and sleeping are perfectly normal things to do in public."
# sub2("sleeping", "running") 
# => "I think sleeping and running are perfectly normal things to do in public."

# User Instructions
# 
# Write a function 'sub_m' that takes a 
# name and a nickname, and returns a 
# string of the following format: 
# "I'm NICKNAME. My real name is NAME, but my friends call me NICKNAME."
# 

given_string2 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."
def sub_m(name, nickname):
    return given_string2 %({'nickname':nickname, 'name':name})
    
    
# sub_m("Mike", "Goose") 
# => "I'm Goose. My real name is Mike, but my friends call me Goose."
# User Instructions

# User Instructions
# 
# Modify the valid_month() function to verify 
# whether the data a user enters is a valid 
# month. If the passed in parameter 'month' 
# is not a valid month, return None. 
# If 'month' is a valid month, then return 
# the name of the month with the first letter 
# capitalized.
#

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']
          
def valid_month(month):
    month = month.capitalize()
    if(month in months):return month
    return None

# valid_month("january") => "January"    
# valid_month("January") => "January"
# valid_month("foo") => None
# valid_month("") => None
# -----------
# User Instructions
# 
# Modify the valid_day() function to verify 
# whether the string a user enters is a valid 
# day. The valid_day() function takes as 
# input a String, and returns either a valid 
# Int or None. If the passed in String is 
# not a valid day, return None. 
# If it is a valid day, then return 
# the day as an Int, not a String. Don't 
# worry about months of different length. 
# Assume a day is valid if it is a number 
# between 1 and 31.
# Be careful, the input can be any string 
# at all, you don't have any guarantees 
# that the user will input a sensible 
# day.
#

def valid_day(day):
    if day and day.isdigit():
        day = int(day)
        if day > 0 and day <= 31:
            return day
# valid_day('0') => None    
# valid_day('1') => 1
# valid_day('15') => 15
# valid_day('500') => None

# User Instructions
# 
# Modify the valid_year() function to verify 
# whether the string a user enters is a valid 
# year. If the passed in parameter 'year' 
# is not a valid year, return None. 
# If 'year' is a valid year, then return 
# the year as a number. Assume a year 
# is valid if it is a number between 1900 and 
# 2020.
#

def valid_year(year):
    if year and year.isdigit():
        year = int(year)
        if year > 1900 and year <= 2020:
            return year


# valid_year('0') => None    
# valid_year('-11') => None
# valid_year('1950') => 1950
# valid_year('2000') => 2000



# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
    for i, o in (("&", "&amp;"),
        (">", "&gt;"),
        ("<", "&lt;"),
        ('"', "&quot;")):
        s = s.replace(i, o)
    return s