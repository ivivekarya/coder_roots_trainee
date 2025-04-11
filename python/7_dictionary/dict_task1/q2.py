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