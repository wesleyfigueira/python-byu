#tire_volume.py
import math
from datetime import datetime

width =float(input("Enter the width of the tire in mm(ex 205): "))
ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter= float (input("Enter the diameter of the wheel in inches (ex 15): "))

#compute results

volume_liters= ((math.pi * width**2 *ratio*(width * ratio + 2540 * diameter )) / 10000000000)

print("The Approximate volume is {:.2f} liters".format(volume_liters))

#datetime use

current_date = datetime.now()
with open ("volume.txt", "at") as volumes:
    
    print (f"{current_date:%Y-%m-%d} , {volume_liters:.2f}")






# for extra credits /Exceeding the Requirements
if  volume_liters <= 30:
    print("The total volume of your tire is {:.2f} and the price of your tire is U$ 50,00".format(volume_liters))
else:
    print (" the volume of your tire is bigger than 30 volumes ")