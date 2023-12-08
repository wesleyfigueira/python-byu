def get_initial (name):
    initial = name [0:1].upper()
    return initial

first_name=input("Enter your name: ")
fi_ini= get_initial(first_name)

second_name= input (" Enter your second name: ")
fi_second= get_initial(second_name)

last_name=input(" Enter your last name: ")
last_initial= get_initial(last_name)

print(" your initials are : " + fi_ini+ fi_second+ last_initial)