import pytest
from uber_calculator import calculate_trip_price, calculate_fuel_used, calculate_total_price

# Replace 'your_trip_calculator_module' with the actual name of your Python file or module

def test_calculate_fuel_used():
    assert calculate_fuel_used(100, 10) == 10  # Assuming 10 liters for 100 km at 10 km/l

def test_calculate_total_price():
    assert calculate_total_price(100, 10, 2) == 152  # Assuming 2 USD per liter, base fare 2 USD, 1.5 USD per km

def test_calculate_trip_price():
    assert calculate_trip_price(100, 10, 2) == 152  # Assuming 2 USD per liter, base fare 2 USD, 1.5 USD per km

# You can add more tests based on your specific requirements and scenarios

if __name__ == "__main__":
    pytest.main()
