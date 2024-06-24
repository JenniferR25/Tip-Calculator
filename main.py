#A tip calculator written by Jennifer R. in Python.
#Created on 24 June 2024 for 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu
#Link to course:  https://100daysofpython.dev/
#Link to author: https://linkstack.lgbt/@JenniferR25

#Greet the user
print("Welcome to the tip calculate.")
#Gather the pre-tip total & assign variable name
bill = float(input("What is the bill total?\n"))
#Gather desired tip % and assign variable name
tip = int(input("What percentage would you like to give?\n"))
#Gather number of people paying the bill
ppl = int(input("How many ways would you like to spilt the bill?\n"))
#Calculate the bill total (including the tip)
total = round((tip / 100) * bill + bill, 2)
#Determin how much each person will pay
split = round(total / ppl, 2)
#Relay the ammounts to the user
print(f"The total is ${total}. Each person needs to pay ${split}.")