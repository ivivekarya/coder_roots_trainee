#Q1 Take a empty Dictionary and Ask user to input the number of time they 
# want to enter and input form user to make dict
khali_dict={}
dict0=int(input("how many times you want to enter:"))

for i in range(dict0):
    key= input(f"enter key{i+1}:")
    value=input(f"enter value {key}:")
    khali_dict[key]=value


    print("final_dict:",khali_dict)
