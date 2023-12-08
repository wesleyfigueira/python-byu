initial_odo=float(input("Enter the fisrts odometer reading (miles): "))
final_odo=float(input("Enter the second odometer reading (miles): "))
gallon=float(input("Enter the amount of fuel used (gallons):"))
 
mpg= (final_odo - initial_odo) / gallon

print("{:.2f} , miles per gallon".format(mpg))


