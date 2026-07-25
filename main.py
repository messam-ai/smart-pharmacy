# ---------------- Store Users ----------------

users = {}

# ---------------- Store Products ----------------

products = {}

# ---------------- Signup Function ----------------

def signup():
    username = input("Enter Username: ")
    if username in users:
        print("Username Already Exists")
        return
    email = input("Enter Email: ")
    if "@" not in email or "." not in email:
        print("Invalid Email")
        return
    password = input("Enter Password: ")
    users[username] = {
        "email": email,
        "password": password
    }
    print("Signup Successful")


# ---------------- Login Function ----------------
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username not in users:
        print("User Not Found")
        return
    if users[username]["password"] == password:
        print("\nLogin Successful")
        product_menu()
    else:
        print("Incorrect Password")

# ---------------- Add Product ----------------
def add_product():
    name = input("Enter Product Name: ")
    if name in products:
        print("Product Already Exists")
        return
    price = float(input("Enter Product Price: "))
    stock = int(input("Enter Stock Quantity: "))
    category = input("Enter Product Category: ")
    products[name] = {
        "price": price,
        "stock": stock,
        "category": category
    }
    print("Product Added Successfully")

# ---------------- View Products ----------------
def view_products():
    if not products:
        print("No Products Available")
        return
    print("\n------ Product List ------")
    for name, detail in products.items():
        print("--------------------------")
        print("Name :", name)
        print("Price :", detail["price"])
        print("Stock :", detail["stock"])
        print("Category :", detail["category"])

# ---------------- Update Product ----------------
def update_product():
    name = input("Enter Product Name: ")
    if name not in products:
        print("Product Not Found")
        return
    price = float(input("Enter New Price: "))
    stock = int(input("Enter New Stock: "))
    category = input("Enter New Category: ")
    products[name]["price"] = price
    products[name]["stock"] = stock
    products[name]["category"] = category
    print("Product Updated Successfully")

# ---------------- Delete Product ----------------
def delete_product():
    name = input("Enter Product Name: ")
    if name in products:
        del products[name]
        print("Product Deleted Successfully")
    else:
        print("Product Not Found")

# ---------------- Increase Stock ----------------
def increase_stock():
    name = input("Enter Product Name: ")
    if name not in products:
        print("Product Not Found")
        return
    qty = int(input("Enter Quantity to Increase: "))
    products[name]["stock"] += qty

    print("Stock Increased Successfully")
    print("Current Stock:", products[name]["stock"])

# ---------------- Decrease Stock ----------------
def decrease_stock():
    name = input("Enter Product Name: ")
    if name not in products:
        print("Product Not Found")
        return
    qty = int(input("Enter Quantity to Decrease: "))
    if qty > products[name]["stock"]:
        print("Error! Negative Stock Not Allowed")
        return
    products[name]["stock"] -= qty
    print("Stock Decreased Successfully")
    print("Remaining Stock:", products[name]["stock"])

# ---------------- Product Menu ----------------
def product_menu():
    while True:
        print("\n========== Product Menu ==========")
        print("1. Add Product")
        print("2. View Products")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Increase Stock")
        print("6. Decrease Stock")
        print("7. Logout")
        choice = input("Enter Choice: ")
        if choice == "1":
            add_product()
        elif choice == "2":
            view_products()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            increase_stock()
        elif choice == "6":
            decrease_stock()
        elif choice == "7":
            print("Logged Out Successfully")
            break
        else:
            print("Invalid Choice")


# ---------------- Main Menu ----------------

while True:
    print("\n========== Main Menu ==========")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        signup()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")




