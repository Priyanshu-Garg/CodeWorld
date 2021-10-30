#This program will tell you how old are calculating your year, month as well as days.

from datetime import date
#importing library for decting current system date.

def How_old_are_you(year,month,day): 
    #creating a function called How_old_are_you with inputs 'year','month' and 'day' which represents the birthday year month and date in the same order.
    today = date.today()
    #'today' variable has the current date in the format yyyy-mm-dd
    l=[]
    a=str(today)
    for i in a:
        l.append(i)
    y=l[0]+l[1]+l[2]+l[3]
    #'y' variable now has the current year in string form.
    y=int(y)
    #converting 'y' to integer type.
    
    m=l[5]+l[6]
    #'m' variable now has the current month in string form.
    m=int(m)
    #converting 'm' to integer type.
    
    d=l[8]+l[9]
    #'d' variable now has the current day in string form.
    d=int(d)
    #converting 'd' to integer type.
    
    print("Today's date:", today)
    print("Your birthday date:",year,'-',month,'-',day)
    
    if day>d:
        m-=1
        d+=30
    #if the birthday date is greater than the current date, we need to borrow a month and hence add 30 days to the birthday date. So that we can perform the substraction.
    if month>m:
        y-=1
        m+=12
    #if the birthday month is greater than the current month, we need to borrow a year and hence add 12 months to the birthday month. So that we can perform the substraction.
    
    diff_in_year=y-year
    diff_in_month=m-month
    diff_in_day=d-day
    #Here we substract the birthday year,month and date from the current year,month and date.
    

    print("You are",diff_in_year,'years',diff_in_month,'months','and',diff_in_day,'days old.')
    print("Thank you")
    i=int(input('enter 1 to restart and 0 to exit the program.'))
    #for repeatability, we ask the user if he/she wants to continue finding out the age of different people.


i=1
while i==1:
#for repeatability, we put a condition that if the variable 'i' has the value 1 the program will continue to run and stop if the variable 'i' has the value 0.
    year=int(input('Enter your birthday year.'))
    month=int(input('Enter your birthday month.'))
    day=int(input('Enter your birthday date.'))
    How_old_are_you(year,month,day)
    
    
    
    
