import csv


def read_dictionary(products, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Initialize an empty dictionary to store the data
    compound_dict = {}

    try:
        # Open the CSV file for reading
        with open(products, 'r', newline='') as file:
            # Create a CSV reader
            csv_reader = csv.reader(file)

            # Read the header to get the column names
            header = next(csv_reader, None)

            # Check if the key_column_index is valid
            if key_column_index < 0 or key_column_index >= len(header):
                raise ValueError("Invalid key_column_index")

            # Iterate through the rows in the CSV file
            for row in csv_reader:
                # Extract the key from the specified column
                key = row[key_column_index]

                # Create a sub-dictionary for the current row
                row_dict = {}
                for i in range(len(header)):
                    if i != key_column_index:
                        row_dict[header[i]] = row[i]

                # Add the sub-dictionary to the compound dictionary
                compound_dict[key] = row_dict

    except FileNotFoundError:
        print(f"Error: File '{products}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return compound_dict

def main():
    # Call read_dictionary function and store the compound dictionary in products_dict
    products_dict = read_dictionary('products.csv', 0)

    # Print the products_dict
    print("Products Dictionary:")
    print(products_dict)

    try:
        # Open the request.csv file for reading
        with open('request.csv', 'r', newline='') as request_file:
            # Create a CSV reader
            csv_reader = csv.reader(request_file)

            # Skip the first line (column headings)
            next(csv_reader, None)

            # Iterate through the rows in the request.csv file
            for row in csv_reader:
                # Extract information from the row
                product_number = row[0]
                requested_quantity = int(row[1])

                # Use the requested product number to find the corresponding item in products_dict
                product_info = products_dict.get(product_number)

                # Check if the product exists in the dictionary
                if product_info:
                    product_name = product_info.get('Product Name')
                    product_price = float(product_info.get('Price'))

                    # Print the product details
                    print(f"Product Name: {product_name}, Requested Quantity: {requested_quantity}, Product Price: ${product_price:.2f}")

                else:
                    print(f"Product with number {product_number} not found in the products dictionary.")

    except FileNotFoundError:
        print("Error: File 'request.csv' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the main function
main()
