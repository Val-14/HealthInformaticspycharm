# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
print("Hello Health informatics")

my_var = 5
my_second_var = 11

calculation = my_var + my_second_var
print(calculation)

first_name = "Valentine"
second_name = "Uche"

print(f"My name is {first_name} {second_name}")

type(first_name)
type(my_var)
#you can call this function to find out the type of variable

#Date and Time
from datetime import date, timedelta
#datetime is a lbirary that allows us to deal with time

queen_bday = date(year=1936, month=4, day=3)

print(queen_bday.strftime("%d, %B, %Y"))
#changes the presentation of the date and time as strftime is very powerful
# you can change the format to use %d/%m/%y
#Look at the documentation for strftime

today_date = date.today()
#this fucntion returns the current date
print(today_date.strftime("%d/%m/%Y"))

if queen_bday < today_date:
    print("The queen is old")

queen_Day = today_date - queen_bday
print(queen_Day)

tank_days = timedelta(days=10000)
#this function creates a variable that caould be used to add 10000 days to any datetime
my_bday = date( year=2001, month=2, day=15)
ten_an = my_bday + tank_days

print(ten_an.strftime("%d/%m/%y"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
