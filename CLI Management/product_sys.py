# Product Inventory Management System

products = [
    {
        "id": 1,
        "name": "Laptop",
        "category": "Electronics",
        "price": 55000,
        "quantity": 10
    },
    {
        "id": 2,
        "name": "Chair",
        "category": "Furniture",
        "price": 1500,
        "quantity": 50
    }
]

# Auto-generate next ID
next_id = len(products) + 1


# Display one product in table format
def display_product(product):
    print("-" * 75)

    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Category':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )

    print("-" * 75)

    print(
        f"{product['id']:<5}"
        f"{product['name']:<20}"
        f"{product['category']:<20}"
        f"{product['price']:<15}"
        f"{product['quantity']:<10}"
    )

    print("-" * 75)


# Add Product
def add_product():
    global next_id

    # Name validation
    while True:
        name = input("Enter product name: ").strip()

        if name == "":
            print("Name cannot be empty.")
        else:
            break

    # Category validation
    while True:
        category = input("Enter category: ").strip()

        if category == "":
            print("Category cannot be empty.")
        else:
            break

    # Price validation
    while True:
        try:
            price = float(input("Enter price: "))

            if price <= 0:
                print("Price must be greater than 0.")
            else:
                break

        except ValueError:
            print("Please enter a valid number.")

    # Quantity validation
    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity < 0:
                print("Quantity cannot be negative.")
            else:
                break

        except ValueError:
            print("Please enter a valid integer.")

    # Create product
    product = {
        "id": next_id,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }

    # Add product to list
    products.append(product)

    # Increase ID
    next_id += 1

    print("Product added successfully!")


# View All Products
def view_products():
    if not products:
        print("No products available.")
        return

    print("\nAll Products:")

    print("-" * 75)
    print(
        f"{'ID':<5}"
        f"{'Name':<20}"
        f"{'Category':<20}"
        f"{'Price':<15}"
        f"{'Quantity':<10}"
    )
    print("-" * 75)

    for product in products:
        print(
            f"{product['id']:<5}"
            f"{product['name']:<20}"
            f"{product['category']:<20}"
            f"{product['price']:<15}"
            f"{product['quantity']:<10}"
        )

    print("-" * 75)


# Search Product
def search_product():
    print("\n1. Search by ID")
    print("2. Search by Name")

    choice = input("Enter your choice: ")

    # Search by ID
    if choice == "1":

        try:
            search_id = int(input("Enter product ID: "))

            for product in products:
                if product["id"] == search_id:
                    print("\nProduct Found:")
                    display_product(product)
                    return

            print("Product not found.")

        except ValueError:
            print("Please enter a valid product ID.")

    # Search by Name
    elif choice == "2":

        search_name = input("Enter product name: ").strip()

        if search_name == "":
            print("Name cannot be empty.")
            return

        for product in products:
            if product["name"].lower() == search_name.lower():
                print("\nProduct Found:")
                display_product(product)
                return

        print("Product not found.")

    else:
        print("Invalid choice.")


# Update Product
def update_product():

    try:
        product_id = int(input("Enter product ID: "))

        for product in products:

            if product["id"] == product_id:

                # Update name
                while True:
                    name = input("Enter new name: ").strip()

                    if name == "":
                        print("Name cannot be empty.")
                    else:
                        product["name"] = name
                        break

                # Update category
                while True:
                    category = input("Enter new category: ").strip()

                    if category == "":
                        print("Category cannot be empty.")
                    else:
                        product["category"] = category
                        break

                # Update price
                while True:
                    try:
                        price = float(input("Enter new price: "))

                        if price <= 0:
                            print("Price must be greater than 0.")
                        else:
                            product["price"] = price
                            break

                    except ValueError:
                        print("Please enter a valid number.")

                # Update quantity
                while True:
                    try:
                        quantity = int(input("Enter new quantity: "))

                        if quantity < 0:
                            print("Quantity cannot be negative.")
                        else:
                            product["quantity"] = quantity
                            break

                    except ValueError:
                        print("Please enter a valid integer.")

                print("Product updated successfully!")
                return

        print("Product not found.")

    except ValueError:
        print("Please enter a valid product ID.")


# Delete Product
def delete_product():

    try:
        product_id = int(input("Enter product ID: "))

        for product in products:

            if product["id"] == product_id:
                products.remove(product)

                print("Product deleted successfully!")
                return

        print("Product not found.")

    except ValueError:
        print("Please enter a valid product ID.")


# Main Function
def main():

    while True:

        print("\n===== PRODUCT INVENTORY MANAGEMENT SYSTEM =====")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            view_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            print("Thank you for using the Inventory Management System!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()