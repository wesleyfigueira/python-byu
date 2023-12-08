import csv
from datetime import datetime

def read_csv(file_path):
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return data

def calculate_subtotal(ordered_items, products):
    subtotal = 0
    for item in ordered_items:
        product_id = item['product_id']
        quantity = int(item['quantity'])
        try:
            product = next(product for product in products if product['product_id'] == product_id)
            price = float(product['price'])
            subtotal += quantity * price
        except StopIteration:
            print(f"Error: Product with ID {product_id} not found.")
        except ValueError:
            print(f"Error: Invalid quantity or price for product with ID {product_id}.")
    return subtotal

def print_receipt(store_name, ordered_items, products):
    print(f"Receipt for {store_name}\n")
    
    total_items = 0
    for item in ordered_items:
        product_id = item['product_id']
        quantity = int(item['quantity'])
        print(f"{quantity} x {products[product_id]['name']}: ${products[product_id]['price']} each")
        total_items += quantity
    
    subtotal = calculate_subtotal(ordered_items, products)
    sales_tax_rate = 0.06
    sales_tax = subtotal * sales_tax_rate
    total_due = subtotal + sales_tax
    
    print("\n-----------------------------")
    print(f"Total items: {total_items}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales Tax ({sales_tax_rate * 100}%): ${sales_tax:.2f}")
    print(f"Total Due: ${total_due:.2f}")
    
    current_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\n-----------------------------")
    print(f"Date and Time: {current_date_time}")
    print("\nThank you for shopping with us!")

# Example usage:
store_name = "Your Store"
products = read_csv('products.csv')
ordered_items = read_csv('request.csv')

if products and ordered_items:
    print_receipt(store_name, ordered_items, products)
