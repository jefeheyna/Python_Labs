#----------------------------------------------------
# This program asks the user for their name, number of years in school,
# and number of years left in school. Then, this program will calculate
# how much of their life (percentage) has been spent in school and how far
# along they are in school (also a percentage).
#
# Jeff Hejna
# 9/2/2014
#----------------------------------------------------

print("What is your name?")
name = input()

print("How old are you?")
age = input()
age_int = int(age)

print("How many years have you been in school?")
years_in = input()
years_in_int = int(years_in)

print("How many years do you think you have left in school?")
years_left = input()
years_left_int = int(years_left)

total_years = years_in_int + years_left_int

percent_of_life = years_in_int / age_int * 100
percent_done = 100 - years_left_int / total_years * 100

print("Well,", name, "you have been in school for", percent_of_life,"% of your life, and you are",percent_done, "% done with school.")



