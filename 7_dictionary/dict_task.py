#Q1 Take a empty Dictionary and Ask user to input the number of time they 
# want to enter and input form user to make dict
khali_dict={}
dict0=int(input("how many times you want to enter:"))

for i in range(dict0):
    key= input(f"enter key{i+1}:")
    value=input(f"enter value {key}:")
    khali_dict[key]=value


    print("final_dict:",khali_dict)


#Q2Given a dictionary employee_details where the keys are employee 
# IDs and values are dictionaries with name, department, and salary, 
# filter and create a list of names of employees who have a salary 
# greater than 50,000.

dict1={

   1: {'name':'yashinder','department':'web','salary':70000},
    2:{'name':'alok','department':'civil','salary':65000},
    3:{'name':'vansh','department':'broker','salary':60000},
    4:{'name':'shubh','department':'sales','salary':40000},

}

higher_salary=[]

for emp_Id,i in dict1.items():
 if i['salary'] > 50000:
    higher_salary.append(i['name'])
    print(higher_salary)
# #Q3 Write a program for a number guessing game where the computer 
# randomly selects a number between 1 and 100, and 
# the user tries to guess it. The program should give hints if
#  the guess is too high or too low.
print("welcome to the world of numbers")
dui=rando
dict2=int("enter you number:")
   if dic

# Q4 Write a program that calculates the discount on a product based 
# on the following criteria:
# If the price is greater than $1000, a discount of 10% is applied.
# If the price is between $500 and $1000, a discount of 5% is applied.
# If the price is below $500, no discount is applied


 #Q5. Write a program that checks the strength of a password based on the following criteria:
# At least 8 characters long
# Contains both uppercase and lowercase characters
# Contains at least one digit
# Contains at least one special character (e.g., !, @, #, $, etc.)


#Q6 WAP to insert values value in the list
#li=[20,30,40,[57,66,30,[70,80],"Hello"],50,True]
#Add value 76 before 80
#Add value 88 after 57
#print the letter H from the list li


#Q7 WAP to plan for a vacation. Take input from asking for the budget.Suggest 
# multiple countries to stay in that budget.
# Ask user to select a country and display a place to visit in that country.
#output
# Welcome to trip planner
# Enter your budget (5000-10000, 10000-20000, 20000-30000, 30000-40000)
# 25000
#ountry available under 30000 are:
# India
# Australia
# USA
#select your choice: India
# the place to visit in the India is the Taj Mahal