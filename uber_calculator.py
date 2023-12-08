def calculate_trip_price(distance, fuel_efficiency, fuel_price_per_liter):
    """Calculate the total cost of the trip."""
    fuel_used = calculate_fuel_used(distance, fuel_efficiency)
    total_price = calculate_total_price(distance, fuel_used, fuel_price_per_liter)
    return total_price

def calculate_fuel_used(distance, fuel_efficiency):
    """Calculate the amount of fuel used for the given distance."""
    fuel_used = distance / fuel_efficiency
    return fuel_used

def calculate_total_price(distance, fuel_used, fuel_price_per_liter):
    """Calculate the total cost of the trip."""
    total_price = fuel_used * fuel_price_per_liter
    # Assuming a base fare of $2 plus $1.5 per kilometer
    total_price += 2 + 1.5 * distance
    return total_price

def main():
    # Example values
    distance_traveled = float(input("Enter the distance traveled in kilometers: "))
    fuel_efficiency = float(input("Enter the fuel efficiency in kilometers per liter: "))
    fuel_price_per_liter = float(input("Enter the fuel price per liter: "))

    # Calculate and print the total trip price
    total_price = calculate_trip_price(distance_traveled, fuel_efficiency, fuel_price_per_liter)
    print(f"The total price of the trip is: ${total_price:.2f}")

if __name__ == "__main__":
    main()
