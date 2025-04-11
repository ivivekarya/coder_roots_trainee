
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

user=int(input("Enter your budget (5000-10000, 10000-20000, 20000-30000, 30000-40000):"))



if 5000 <= user <= 10000:
    countries = ["Nepal", "Sri Lanka"]
elif 10000 < user <= 20000:
    countries = ["Thailand", "Malaysia"]
elif 20000 < user <= 30000:
    countries = ["India", "Australia", "USA"]
elif 30000 < user <= 40000:
    countries = ["France", "Japan", "Canada"]
else:
    print("Sorry! We don't have packages for this budget.")
    
for user in countries:
    print("-",user)

selected = input("Select your country from the list above: ").strip()


places = {
        "Nepal": "Mount Everest",
        "Sri Lanka": "Sigiriya",
        "Thailand": "Phi Phi Islands",
        "Malaysia": "Petronas Towers",
        "India": "Taj Mahal",
        "Australia": "Sydney Opera House",
        "USA": "Grand Canyon",
        "France": "Eiffel Tower",
        "Japan": "Mount Fuji",
        "Canada": "Niagara Falls"
    }

if selected in places:
        print("The place to visit in", selected, "is the", places[selected])
else:
        print("Invalid selection. Please run the planner again.")
