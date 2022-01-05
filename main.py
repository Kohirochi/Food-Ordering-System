# CHAI LI QI
# YONG KAI BIN

def main_page():
    print("[Online Food Order Management System]".center(54, "="))
    print("[SPIDERMAN ONLINE FOOD SERVICES]".center(54, "="))
    print("[Main Page]".center(54, "="))
    print("\nWELCOME!!!\n"
          "1) Login As Admin\n"  # Display options for everyone
          "2) Login As Customer\n"
          "3) View As Guest\n"
          "4) Exit")
    option = input("\nSelect an option [1-4]: ")  # Accept input from user
    while option not in ["1", "2", "3", "4"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 4.")
        option = input("Select an option [1-4]: ")  # Accept input again
    return option


def exit_program():
    print("\nThank you for using Spiderman Online Food Services.")
    exit()  # Exit program


def admin_page():
    print("\n")
    print("[Admin]".center(54, "="))
    print("\n"
          "1) Add Food Item\n"  # Display options for admin
          "2) Modify Food Item\n"
          "3) View All Records of Food Category\n"
          "4) View All Records of Food Item\n"
          "5) View All Records of Food Customer Orders\n"
          "6) View All Records of Food Customer Payment\n"
          "7) View Specific Record of Customer Order\n"
          "8) View Specific Record of Customer Payment\n"
          "9) Log Out\n"
          "10) Exit")
    option = input("\nSelect an option [1-10]: ")  # Accept input from user
    while option not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 10.")
        option = input("Select an option [1-10]: ")  # Accept input again
    return option


def cust_page():
    print("\n")
    print("[Customer]".center(54, "="))
    print("\n"
          "1) View Menu with Description \n"  # Display options for customer
          "2) View Cart\n"
          "3) Log Out\n"
          "4) Exit")
    option = input("\nSelect an option [1-4]: ")  # Accept input from user
    while option not in ["1", "2", "3", "4"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 4.")
        option = input("Select an option [1-4]: ")  # Accept input again
    return option


def guest_page():
    print("\n")
    print("[Guest]".center(54, "="))
    print("\n"
          "1) View Menu\n"  # Display options for guest
          "2) Sign Up as Customer\n"
          "3) Return to Main Page\n"
          "4) Exit")
    option = input("\nSelect an option [1-4]: ")  # Accept input from user
    while option not in ["1", "2", "3", "4"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 4.")
        option = input("Select an option [1-4]: ")  # Accept input again
    return option


def admin_login():
    print("\n")
    print("[Admin Login]".center(54, "="))
    name = input("Enter username: ")  # Accept username from user
    counter = 4  # Set 5 attempts for the user to enter password
    if check_name("Admin", name):  # Check if username exists
        pwd = input("Enter password: ")  # Accept password from user
        while not check_pass(name, pwd):  # If wrong password entered by user
            if counter == 0:  # When no attempts left, return False
                print("\nNo attempts left")
                print("\nReturning to Main Page...\n")
                return False
            print("\nIncorrect password!")
            print(f"You have {counter} attempts left.")
            counter -= 1  # Attempts decrease by 1
            pwd = input("Enter password: ")  # Accept password from user again
        print("\nLogin Successful")  # If the password matches, return True
        print(f"Welcome {name}")
        return True
    else:
        print("\nUsername not found!")  # If username does not exist, return False
        print("\nReturning to Main Page...\n")
        return False


def cust_login():
    print("\n")
    print("[Customer Login]".center(54, "="))
    name = input("Enter username: ")  # Accept username from user
    counter = 4  # Set 5 attempts for the user to enter password
    if check_name("Customer", name):  # Check if username exists
        pwd = input("Enter password: ")  # Accept password from user
        while not check_pass(name, pwd):  # If wrong password entered by user
            if counter == 0:  # When no attempts left, return False
                print("\nNo attempts left")
                print("\nReturning to Main Page...\n")
                return False
            print("\nIncorrect password!")
            print(f"You have {counter} attempts left.")
            counter -= 1  # Attempts decrease by 1
            pwd = input("Enter password: ")  # Accept password from user again
        print("\nLogin Successful\n"  # If the password matches, return True
              f"Welcome {name}")
        return name
    else:
        print("\nUsername not found!")  # If username does not exist, return False
        print("\nReturning to Main Page...\n")
        return False


def check_name(target, name):
    with open(f"{target}.txt", "r") as file:  # Open text file that records all customers' name
        for line in file:  # Loop through the text file
            names = line.split(";")  # Extract all the names into a list
            names.pop()
    if name in names:  # Check if username exists
        return True
    else:
        return False


def check_pass(name, pwd):
    with open(f'{name}.txt', 'r') as pw:  # Open user's text file
        user_pass = pw.readline().strip("\n")  # Obtain password in text file
    if pwd == user_pass:  # Check if the password matches
        return True
    else:
        return False


def signup():
    print("\n")
    print("[Customer Signup]".center(54, "="))
    print("Criteria for Username")  # Display criteria for creating username
    print("1. Only alphanumeric characters are accepted.")
    print("2. Your username must begin with a letter.")
    print("3. Length must be between 3 and 15 characters.")
    print("-" * 54, "\n")
    print("Criteria for Password")  # Display criteria for creating password
    print("1. Length must be between 8 and 15 characters.")
    print("-" * 54, "\n")
    name = input("Enter username between 3 and 15 characters: ")  # Accept new username from user
    while not check_new_name(name):  # If username does not meet criteria
        name = input("Enter username between 3 and 15 characters: ")  # Accept username again
    pwd = input("Enter password: ")  # Accept new password from user
    while not check_new_pass(pwd):  # If password  does not meets criteria
        pwd = input("Enter password: ")  # Accept password again
    with open("Customer.txt", "a") as cust:  # Open text file containing all customer names
        cust.write(f"{name};")  # Write the new username into the text file
    new_cust = open(f"{name}.txt", "x")  # Open a new text file for that customer
    new_cust.write(pwd)  # Write the new password created by user
    new_cust.close()  # Close the text file
    print("\nSignup Successful.")
    print("\n")


def check_new_name(name):
    if 2 < len(name) < 16:  # Check if length of username given between 3 to 15 character
        words = name.split()  # Separate name into words
        if len(words) == 1:  # Check if username is exactly one word
            if name[0].isalpha():  # Check if username begins with letter
                if name.isalnum():  # Check if username only contains alphanumeric
                    with open("Customer.txt", "r") as cust:  # Open text file that records all customers' name
                        for line in cust:  # Loop through the text file
                            cust_name = line.split(";")  # Extract all the names into a list
                        if name in cust_name:  # If username exists
                            print("Username exists.")
                            print("Please enter another username.\n")
                            return False
                        else:  # If username does not exist
                            return True
                else:  # If username contains characters other than alphanumeric
                    print("Only alphanumeric characters are accepted.\n")
                    return False
            else:
                print("Your username must begin with a letter.\n")
                return False
        else:  # If username more than 1 word
            print("Please enter only one word as your username.\n")
            return False
    else:  # If length of username given not between 3 to 15 character
        print("Your username must be between 3 and 15 characters.\n")
        return False


def check_new_pass(pwd):
    if not 7 < len(pwd) < 16:  # Check if length of password between 8 to 15 characters
        print("Your password must be between 8 and 15 characters.\n")
        return False
    else:
        return True


def menu():
    food_types = food_type()
    foods = []
    with open("Menu.txt", "r") as Menu:  # Open the Menu.txt file from computer and name it as Menu
        for ctg in range(len(food_types)):
            Menu.seek(0)
            foods.append([])
            for details in range(3):
                foods[ctg].append([])
            for line in Menu:  # Loop through each line in the file
                food = line.strip("\n").split(";")  # Extract content into a list
                if food_types[ctg].lower() == food[0]:  # Check if the category matches the category in line
                    foods[ctg][0].append(food[1])
                    foods[ctg][1].append(food[2])
                    foods[ctg][2].append(food[3])
    return foods


def food_type():
    food_category = []  # Food category with duplicates
    final_food_category = []  # Food category without duplicates
    with open("Menu.txt", "r") as Menu:  # Open the Menu.txt file from computer and name it as Menu
        for line in Menu:  # Loop through each line in the file
            food = line.strip("\n").split(";")  # Extract content into a list
            food_category.append(food[0])  # Extract every food categories
    for category in food_category:  # Loop through all food category with duplicates
        uppercase = category[0].upper() + category[1:]  # Capitalise first letter in the string
        if uppercase not in final_food_category:  # Remove duplicates
            final_food_category.append(uppercase)  # Add them into a final food category
    return final_food_category


def food_code():
    food = menu()
    food_types = food_type()
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # Generate alphabets from A to Z
    code = [alphabets[counter]  # Insert alphabets into a list based on total number of food type
            for counter in range(len(food_types))]  # Loop based on total number of food type
    food_codes = [[f"{code[ctg]}{item + 1}"  # Add each food code into list based on number of food in each category
                   for ctg in range(len(food_types))  # Loop based on total number of the food categories
                   for detail in range(1)  # Loop only once for each food category
                   for item in range(len(food[ctg][detail]))
                   # Loop through each food name in each food category to find out number of food in each category
                   if food_types[ctg] == category]  # Check if each food types matches
                  for category in food_types]  # Loop through each food types
    return food_codes


def flatten_code():
    codes = food_code()
    all_code = [code  # Add all codes into list
                for ctg in codes  # Loop through each category
                for code in ctg]  # Loop through each code in each category
    return all_code


def flatten_food_name():
    foods = menu()
    all_food_name = [name  # Add all name into list
                     for ctg in foods  # Loop through each category
                     for name in ctg[0]]  # Loop through each food name in each category
    return all_food_name


def flatten_food_price():
    foods = menu()
    all_food_price = [price  # Add all price into list
                      for ctg in foods  # Loop through each category
                      for price in ctg[1]]  # Loop through each food price in each category
    return all_food_price


def flatten_food_desc():
    foods = menu()
    all_food_desc = [desc  # Add all description into list
                     for ctg in foods  # Loop through each category
                     for desc in ctg[2]]  # Loop through each food description in each category
    return all_food_desc


def view_menu():
    food = menu()
    food_types = food_type()
    print("\n")
    print("[Menu]".center(54, "="))
    for ctg in range(len(food_types)):  # Display each food category
        print(food_types[ctg].center(54, "-"))
        print("{:43}{:5}".format("Item", "Price (RM)"))
        for detail in range(1):  # Display each food based on category
            for item in range(len(food[ctg][detail])):
                print("{:43}{:.2f}".format(food[ctg][detail][item], float(food[ctg][detail + 1][item])))
    print("\n1) Return to Guest Page\n"
          "2) Exit")
    option = input("\nSelect an option [1-2]: ")  # Accept input from user
    while option not in ["1", "2"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 2.")
        option = input("Select an option [1-2]: ")  # Accept input again
    return option


def full_menu():
    food = menu()
    code = food_code()
    food_types = food_type()
    for ctg in range(len(food_types)):  # Display each food category
        print(food_types[ctg].center(54, "-"))
        print("{:43}{:5}".format("Item", "Price (RM)"))
        for detail in range(1):  # Display each food item once based on category
            for item in range(len(food[ctg][detail])):  # Loop based on total number of food
                print(code[ctg][item], "{:43}{:.2f}".format(food[ctg][detail][item], float(food[ctg][detail + 1][item])))
                print("  ", "{:43}".format(enter_next_line(food[ctg][detail + 2][item])))
                print()


def enter_next_line(desc):
    total_length = 0  # Total length of words
    code_length = 3  # Spaces reserved for code
    max_length = 43  # Maximum spaces reserved for description section
    desc_length = max_length - code_length  # Spaces reserved for description
    new_desc = ""
    desc_list = desc.split()  # Separate each word into list
    for word in desc_list:  # Loop through each word
        word += " "  # Spacing between each word
        total_length += len(word)  # Summing up the total length
        if total_length > desc_length:  # If total length of words larger than spaces remain for description
            next_line = word.replace(word, f"\n{' '* code_length}{word}")  # The word move to next line
            total_length = len(word)  # Recalculate the total length of words
            new_desc += next_line  # Join each word together
        else:
            new_desc += word  # Join each word together
    return new_desc


def view_full_menu():
    print("\n")
    print("[Menu]".center(54, "="))
    full_menu()
    print("1) Add food to cart\n"
          "2) Return to Customer Page\n"
          "3) Exit")
    option = input("\nSelect an option [1-3]: ")  # Accept input from user
    while option not in ["1", "2", "3"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 3.")
        option = input("Select an option [1-3]: ")  # Accept input again
    return option


def food_match(code):
    all_code = flatten_code()
    food_name = flatten_food_name()
    food_price = flatten_food_price()
    food_desc = flatten_food_desc()
    food = []
    for counter in range(len(all_code)):  # Loop through each food
        if code == all_code[counter]:  # Check if the code given by user matches existing food code
            food = [code, food_name[counter], food_price[counter],
                    food_desc[counter]]  # Add the code, name and price of the food if matches
            break
    return food


def add_cart():
    all_code = flatten_code()
    cart = []
    print()
    print("[Add to Cart]".center(54, "="))
    code = input("\nEnter a valid food code: ")  # Accept one code from users
    while code not in all_code:  # Input must not equal to 1 or 2
        print("\nInvalid food code!")
        code = input("Enter a valid food code: ")  # Accept input from user aga
    cart.append(food_match(code))  # Add the food into cart
    print("\nFood added into cart successfully\n"
          "1) Continue Ordering\n"
          "2) Return to Customer page")
    option = input("\nSelect an option [1-2]: ")  # Accept input from user
    while option not in ["1", "2"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 2.")
        option = input("Select an option [1-2]: ")  # Accept input again

    if option == "1":  # If user choose to continue ordering
        return ["1", cart]  # If user continue ordering, return the option and the cart
    else:
        return ["2", cart]  # If user stop ordering, return the option and the cart


def view_cart(cart):
    print()
    print("[Your Cart]".center(54, "="))
    for i in range(len(cart)):
        if not cart[i]:  # If cart[i] is an empty list
            cart.pop(i)  # Remove cart[i] from cart
    code = [code[0] for code in cart]  # Obtain every code from cart and flatten them
    food_name = [name[1] for name in cart]  # Obtain every food name from cart and flatten them
    food_price = [price[2] for price in cart]  # Obtain every price from cart and flatten them
    print("{:43}{:5}".format("Item", "Price (RM)"))
    for counter in range(len(cart)):  # Loop through each food in cart
        print("{:3}{:43}{:.2f}".format(code[counter], food_name[counter], float(food_price[counter])))
    print("\n"
          "1) Delete Food\n"  # Display options for guest
          "2) Clear Cart\n"
          "3) Proceed to Payment\n"
          "4) Return to Customer Page")
    option = input("\nSelect an option [1-4]: ")  # Accept input from user
    while option not in ["1", "2", "3", "4"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 4.")
        option = input("Select an option [1-4]: ")  # Accept input again
    return option


def save_cart(username, cart):
    old_cust = False  # Check either old customer or new customer
    with open(f"{username}.txt", "r+") as file:  # Open customer text file
        lines = file.readlines()  # Store menu contents into a variable
        file.seek(0)  # Place the file handler at the beginning of the file
        file.truncate()  # Set the file to certain byte. In this situation is delete all file contents
        for line in lines:
            if "cart" in line:
                old_cust = True
                break
        if old_cust is True:
            for line in lines:
                if "cart" in line:
                    new_cart = line.replace(line, cart + "\n")  # Replace old cart with final cart
                    file.write(new_cart)  # Write down the new cart
                else:  # If "cart" is not in line
                    file.write(line)  # Write back all the lines that are not related to cart
        else:  # If old_cust is False
            for line in lines:
                file.write(line)  # Write back all the lines that are not related to cart
            file.write("\n" + cart)  # Write down the final cart


def update_cart(username, cart):
    separator = ";"
    if len(cart) > 0:  # Got food in cart
        codes = [code[0] for code in cart]
        code_in_file = ""
        for code in codes:
            code_in_file += f"{code}{separator}"
        final_cart = f"cart{separator}" + code_in_file
        save_cart(username, final_cart)
    else:  # No items in cart
        final_cart = f"cart{separator}"
        save_cart(username, final_cart)


def create_cart(username):
    cart = []
    with open(f"{username}.txt", "r") as file:  # Open customer text file
        lines = file.readlines()  # Store each line into a list
        for line in lines:
            if "cart" in line:
                code = line.strip("\n").split(";")  # Split food codes into a list
                code.pop()  # Remove the last element from the list which is an empty string
                for i in range(len(code) - 1):  # Loop through the length of code
                    food = food_match(code[i + 1])  # Obtain each food code
                    cart.append(food)  # Add into cart
                break
    return cart


def log_out():
    print("\nLogging Out..."
          "\nReturning to Main Page..."
          "\nLog Out Successful\n")


def del_food(cart):
    code = [code[0] for code in cart]  # Obtain the code from cart and flatten it
    print()
    print("[Delete From Cart]".center(54, "="))
    delete = input("\nEnter a food code you wish to delete: ")  # Accept food code from user
    while delete not in code:  # If food code does not exist
        print("\nThe food does not exist in your cart.")
        delete = input("Enter a food code you wish to delete: ")  # Accept food code again
    for food in range(len(cart)):  # Loop through each food
        if delete in cart[food]:  # If the food code is in the list
            cart.pop(food)  # Remove the food
            break
    print("The food is deleted from your cart.")
    return cart


def check_cart(cart):
    if len(cart) == 0:  # If length of cart is 0
        print("\nYour cart is empty.")
        return False
    else:
        return True


def order_price(cart):
    food_price = [float(price[2]) for price in cart]  # Get all the food price into a list
    total_price = 0  # Set total price = 0
    for price in food_price:  # Loop through every price
        total_price += price  # Add up the price to total price
    return total_price


def payment(cart):
    total_price = order_price(cart)
    total_item = len(cart)  # Count the total number of items in cart
    print()
    print("[Payment]".center(54, "="))
    print("Total Items:", total_item)  # Display total items
    print("Total Price:", "RM{:.2f}".format(total_price))  # Display total price
    if check_payment(cart) is True:
        print("\nAre you sure to place this order?\n"
              "1) Yes\n"
              "2) No")
        option = input("\nSelect an option [1-2]: ")  # Accept input from user
        while option not in ["1", "2"]:  # Check if input is valid
            print("\nInvalid input."
                  "\nPlease insert a number between 1 and 2.")
            option = input("Select an option [1-2]: ")  # Accept input again
        if option == "2":
            print("\nReturning to View Cart...")
        return option
    else:
        return False


def check_payment(cart):
    if len(cart) == 0:  # Check if food exists in cart
        print("\nYour cart is empty.")
        print("Please add food before paying.")
        return False
    else:
        return True


def confirm_payment(username, cart):
    separator = ";"  # Used to separate each details
    order_id = "order" + ID()  # Create order id
    payment_id = "payment" + ID()  # Create payment id
    code = [code[0] for code in cart]  # Obtain the code from cart and flatten it
    food_name = [name[1] for name in cart]  # Obtain the food name from cart and flatten it
    total_price = "\n" + f"{payment_id}{separator}" + str(order_price(cart))
    for number in range(len(code)):  # Loop through number of food in cart
        order = "\n" + f"{order_id}{separator}" + f"{code[number]}{separator}" + f"{food_name[number]}"
        with open(f"{username}.txt", "r+") as file:  # Open customer text file
            file.readlines()  # Place the cursor to the last line
            file.write(order)  # Add food name given by user into text final_food_category
    with open(f"{username}.txt", "r+") as cust:  # Open customer text file
        cust.readlines()  # Place the cursor to the last line
        cust.write(total_price)  # Add food name given by user into text final_food_category
    with open("Order.txt", "r+") as order_file:  # Open text file that records all orders
        order_file.readline()  # Place the cursor to the last character in the first line
        order_file.write(f"{ID()}{separator}")  # Add the order id
    print("Payment made.")


def ID():
    num = 101  # Set ID start from 101
    while True:
        with open("Order.txt", "r") as orders:  # Open text file that records all orders
            line = orders.readline()  # Read the first line and put the value into a variable
            if str(num) in line:  # Check if the ID already exist
                num += 1  # If ID already exist, ID increase by 1
            else:
                return str(num)  # If ID does not exist, return the ID in string format


def add_item():
    separator = ";"  # Used to separate each details
    print()
    print("[Add Food Item]".center(54, "="))
    category = input("\nEnter food category: ").lower().strip()  # Accept one code from user
    while check_category(category) is False:
        category = input("\nEnter food category: ").lower().strip()  # Accept one code from user
    food_name = input("\nEnter food name: ").strip()  # Accept one code from user
    while check_food_name(food_name) is False:  # Check if food name already exist in the menu text file
        food_name = input("\nEnter food name: ").strip()  # Accept food name from user again
    food_price = check_food_price()  # Check if food price matches the requirements
    food_desc = input("\nEnter food description: ").strip()  # Accept input from user
    while check_food_desc(food_desc) is False:  # Check if food description matches the requirements
        food_desc = input("\nEnter food description: ").strip()  # Accept input from user again
    item = f"{category}{separator}" + f"{food_name}{separator}" + f"{food_price:.2f}{separator}" + f"{food_desc}" + "\n"  # Add all the details of food together
    with open("Menu.txt", "r+") as file:  # Open customer text file
        file.readlines()  # Place the cursor to the last line
        file.write(item)  # Add food given by user into text file
    print("\nNew food added into menu successfully\n"
          "1) Continue adding\n"
          "2) Return to admin page")
    option = input("\nSelect an option [1-2]: ")  # Accept input from user
    while option not in ["1", "2"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 2.")
        option = input("Select an option [1-2]: ")  # Accept input again
    return option


def check_category(category):
    if category == "":  # If category is an empty string
        print("Category cannot be left blank.")
        return False
    else:
        words = category.split()  # Split the name input by user
        for word in words:  # Loop through each word
            if not word.isalpha():  # If the word contains other than alphabets
                print("\nInvalid input.")
                print("Only alphabets are accepted.")
                return False
        return True


def check_food_name(name):
    if name == "":  # If name is an empty string
        print("Please enter a name.")
        return False
    else:
        with open("Menu.txt", "r") as Menu:  # Open menu text file in reading mode
            for line in Menu:  # Loop through each line in menu
                food = line.strip("\n").split(";")  # Split each line into a list
                if name == food[1]:  # If name exists in menu
                    print("\nFood exists.")
                    print("Please enter again.")
                    return False
            return True


def check_food_price():  # Loop until break
    while True:
        try:  # Try to run the code if error occur it goes to except section
            food_price = float(input("\nEnter food price: "))  # Accept input from user
            break  # If no error occur break the loop
        except ValueError:  # If user enter value other than integer
            print("\nInvalid input.")
            print("Only numbers are accepted.")
    return food_price


def check_food_desc(desc):
    if desc == "":  # If desc is an empty string
        print("Description cannot be left blank.")
        return False
    else:
        return True


def modify_item():
    print()
    print("[Modify Item]".center(54, "="))
    full_menu()
    print("1) Delete Item\n"
          "2) Update Item\n"
          "3) Return to Admin Page")
    option = input("\nSelect an option [1-3]: ")  # Accept input
    while option not in ["1", "2", "3"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 3.")
        option = input("Select an option [1-3]: ")  # Accept input again
    return option


def admin_del_food_page():
    code = flatten_code()  # Obtain the code from menu
    print()
    print("[Delete Item]".center(54, "="))
    delete = input("\nEnter the food code of the food you wish to delete: ")  # Accept food code from user
    while delete not in code:  # If food code does not exist
        print("\nThe food does not exist.")
        delete = input("Enter an existing food code: ")  # Accept food code again
    food = food_match(delete)  # Use the code given to get the details of the food
    return food


def del_confirmation():
    food = admin_del_food_page()
    print()
    print("{:43}{:5}".format("Item", "Price (RM)"))
    print("{:3}{:43}{:.2f}".format(food[0], food[1], float(food[2])))  # Display the food details that user wanted to delete
    print("  ", "{:43}".format(food[3]))
    print("\nAre you sure you want to delete this food?\n"
          "1) Yes\n"
          "2) No")
    option = input("\nSelect an option [1-2]: ")  # Accept input
    while option not in ["1", "2"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 2.")
        option = input("Select an option [1-2]: ")  # Accept input again
    if option == "1":  # If user confirm deletion
        with open("Menu.txt", "r+") as Menu:  # Open the file
            lines = Menu.readlines()  # Store menu contents into a variable
            Menu.seek(0)  # Place the file handler at the beginning of the file
            Menu.truncate()  # Set the file to certain byte. In this situation is delete all file contents
            for line in lines:  # Loop through the list
                if food[1] not in line:  # Rewrite the menu file without the specified food
                    Menu.write(line)
        print("\nFood is now deleted from menu.")
        return_page()
    else:  # If user rejects deletion
        print("\nReturning to Modify Item Page...")


def return_page():  # Function that act as a resting station to let user see the results
    option = input("\nEnter 0 to return: ")  # Accept input from user
    while option != "0":  # Check if option is equal to 0
        print("\nInvalid input")
        option = input("\nEnter 0 to return: ")  # Accept input from user again


def update_food():
    code = flatten_code()  # Obtain the code from menu
    print()
    print("[Update Item]".center(54, "="))
    update = input("\nEnter the food code of the food you wish to update: ")  # Accept food code from user
    while update not in code:  # If food code does not exist
        print("\nThe food does not exist.")
        update = input("Enter an existing food code: ")  # Accept food code again
    food = food_match(update)  # Use the code given to get the details of the food
    return food


def update_confirmation(food):
    print()
    print("{:43}{:5}".format("Item", "Price (RM)"))
    print("{:3}{:43}{:.2f}".format(food[0], food[1], float(food[2])))  # Display the details of food that user wants to update
    print("  ", "{:43}".format(food[3]))
    print("\nAre you sure you want to update this food?\n"
          "1) Yes\n"
          "2) No")
    option = input("\nSelect an option [1-2]: ")  # Accept input
    while option not in ["1", "2"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 and 2.")
        option = input("Select an option [1-2]: ")  # Accept input again
    return option


def update_process():
    print("\nChoose the one you wish to make changes.\n"
          "1) Food Name\n"
          "2) Food Price\n"
          "3) Food Description")
    choice = input("Select an option [1-3]: ")  # Accept input
    while choice not in ["1", "2", "3"]:  # Check if input is valid
        print("\nInvalid input."
              "\nPlease insert a number between 1 to 3")
        choice = input("Select an option [1-3]: ")  # Accept input again
    return choice


def update_food_name(food):
    print("\nOriginal food name:", food[1])  # Display original food name
    new_name = input("Enter food name: ")  # Accept new food name
    while check_food_name(new_name) is False:  # Check if new food name matches the requirements
        new_name = input("\nEnter food name: ")
    with open("Menu.txt", "r+") as Menu:  # Open the file in reading and writing mode
        lines = Menu.readlines()  # Store menu contents into a variable
        Menu.seek(0)  # Place the file handler at the beginning of the file
        Menu.truncate()  # Set the file to certain byte. In this situation is delete all file contents
        for line in lines:  # Loop through the list
            if food[1] in line:  # If old food name is found in the list
                new_line = line.replace(food[1], new_name)  # Replace the old food name with new food name
                Menu.write(new_line)  # Add the new food details in menu file with new food name
            else:
                Menu.write(line)  # Rewrite others food details in the menu file
    print("\nFood name updated.")
    print("{:43}{:5}".format("Item", "Price (RM)"))
    print("{:3}{:43}{:.2f}".format(food[0], new_name, float(food[2])))  # Display the new food name with other details
    print("  ", "{:43}".format(food[3]))
    return_page()


def update_food_price(food):
    print("\nOriginal food price:", f"RM{food[2]}")  # Display original food price
    new_price = check_food_price()  # Check if the new food price matches the requirements
    with open("Menu.txt", "r+") as Menu:  # Open the file in reading and writing mode
        lines = Menu.readlines()  # Store menu contents into a variable
        Menu.seek(0)  # Place the file handler at the beginning of the file
        Menu.truncate()  # Set the file to certain byte. In this situation is delete all file contents
        for line in lines:  # Loop through the list
            if food[1] in line:  # By using food name, locate the position of the food in the list
                new_line = line.replace(food[2], str(new_price))  # Replace the old food price with new food price
                Menu.write(new_line)  # Add the food details in menu file with new food price
            else:
                Menu.write(line)  # Rewrite others food details in the menu file
    print("\nFood price updated.")
    print("{:43}{:5}".format("Item", "Price (RM)"))
    print("{:3}{:43}{:.2f}".format(food[0], food[1], float(new_price)))  # Display the new food price with other details
    print("  ", "{:43}".format(food[3]))
    return_page()


def update_food_desc(food):
    print("\nOriginal food description:", food[3])  # Display original food price
    new_desc = input("Enter food description: ")  # Accept new food desc
    while check_food_desc(new_desc) is False:  # Check if the new food price matches the requirements
        new_desc = input("\nEnter food description: ")  # Accept new food desc again
    with open("Menu.txt", "r+") as Menu:  # Open the file in reading and writing mode
        lines = Menu.readlines()  # Store menu contents into a variable
        Menu.seek(0)  # Place the file handler at the beginning of the file
        Menu.truncate()  # Set the file to certain byte. In this situation is delete all file contents
        for line in lines:  # Loop through the list
            if food[1] in line:  # By using food name, locate the position of the food in the list
                new_line = line.replace(food[3], new_desc)  # Replace the old food description with new food description
                Menu.write(new_line)  # Add the food details in menu file with new food price
            else:
                Menu.write(line)  # Rewrite others food details in the menu file
    print("\nFood description updated.")
    print("{:43}{:5}".format("Item", "Price (RM)"))
    print(
        "{:3}{:43}{:.2f}".format(food[0], food[1], float(food[2])))  # Display the new food price with other description
    print("  ", "{:43}".format(new_desc))
    return_page()


def view_food_category():
    food_types = food_type()
    print()
    print("[Food Category]".center(54, "="))
    for i in range(len(food_types)):  # Loop based on the total number of food category
        print(f"{i + 1}. {food_types[i]}")  # Display each food category
    return_page()


def admin_view_menu():
    print("\n")
    print("[Menu]".center(54, "="))
    full_menu()
    return_page()


def all_orders():
    all_cust = all_customer()
    print("\n")
    print("[All Customer Orders]".center(70, "="))
    print("-" * 70)
    for name in all_cust:  # Loop through each customer name in the list
        with open(f"{name}.txt", "r") as cust:  # Open the customer's file in reading mode
            order_id = []
            for lines in cust:  # Loop through each line in the file
                if "order" in lines:  # If "order" found in that line
                    line = lines.strip("\n").split(";")  # Split each order details into a list
                    order_id.append(line[0])  # Add the order id into list
            unique_id = remove_duplicate(order_id)  # Remove duplicate order id
            for elem in unique_id:  # Loop through each order id
                cust.seek(0)  # Place the file handler back to the beginning of the file
                print(f"{elem[0].upper() + elem[1:]}\n")  # Display the order id with first letter being capitalised
                print(f"Customer: {name}")  # Display customer name
                codes = []
                food_quantity = []
                food_names = []
                food_price = []
                for lines in cust:  # Loop through each line in the file
                    if elem in lines:  # If the particular order id found in that line
                        order_details = lines.strip("\n").split(";")  # Split the order details into a list
                        codes.append(order_details[1])  # Add the food code into a list
                        food_names.append(order_details[2])  # Add the food name into a list
                unique_code = remove_duplicate(codes)  # Remove duplicate food code
                unique_food = remove_duplicate(food_names)  # Remove duplicate food name
                for code in unique_code:  # Loop through each code
                    quantity = codes.count(code)  # Count the total number of code appear in the list before remove duplicate
                    food_quantity.append(quantity)  # Add the total number of code appeared into a list
                    food_details = food_match(code)  # Use the code given to get the details of the food
                    food_price.append(food_details[2])  # Add the individual food price into list
                print("{:43}{:16}{:5}".format("Item", "Item Price(RM)", "Quantity"))
                for i in range(len(unique_code)):  # Loop based on the total number of unique code
                    print("{:3}{:40}{:^13.2f}{:^15}".format(unique_code[i], unique_food[i], float(food_price[i]), food_quantity[i]))  # Display the ordered food details
                print()
                print("-" * 70)
    return_page()


def all_customer():
    with open("Customer.txt", "r") as cust:  # Open the customer text file that records all the customer name in reading mode
        names = cust.readline().split(";")  # Separate each customer name and put them into a list
        names.pop()  # Delete the last index which is the blank string in the list
    return names


def remove_duplicate(items):
    final_list = []
    for item in items:  # Loop through each element in the list
        if item not in final_list:  # If the element does not exist in the final list
            final_list.append(item)  # Add the element into the list
    return final_list


def specific_order():
    all_cust = all_customer()
    print("\n")
    print("[Specific Customer Order]".center(70, "="))
    print("All customers:")
    for i in range(len(all_cust)):  # Loop based on the total number of customers
        print(f"{i + 1}. {all_cust[i]}")  # Display all customer names
    name = input("\nEnter a customer name: ")  # Accept customer name from user
    while name not in all_cust:  # If input does not match
        print("\nName does not exist.")
        name = input("Enter a customer name: ")  # Accept customer name from user again
    with open(f"{name}.txt", "r") as cust:  # Open the given customer's file in reading mode
        print()
        print(f"Customer: {name}")  # Display customer name
        print("-" * 70)
        order_id = []
        for lines in cust:  # Loop through each line in the file
            if "order" in lines:  # If "order" is found in that line
                line = lines.strip("\n").split(";")  # Split each order details into a list
                order_id.append(line[0])  # Add the order id into a list
        unique_id = remove_duplicate(order_id)  # Remove duplicate order id
        if len(unique_id) == 0:  # Check if the total number of order id is equal to 0
            print("No orders")
        else:
            for elem in unique_id:  # Loop through each order id
                cust.seek(0)  # Place the file handler back to the beginning of the file
                print(f"{elem[0].upper() + elem[1:]}\n")  # Display the order id with first letter being capitalised
                codes = []
                food_quantity = []
                food_names = []
                food_price = []
                for lines in cust:  # Loop through each line in the file
                    if elem in lines:  # If the particular order id is found in that line
                        order_details = lines.strip("\n").split(";")  # Split the order details into a list
                        codes.append(order_details[1])  # Add the food code into a list
                        food_names.append(order_details[2])  # Add the food name into a list
                unique_code = remove_duplicate(codes)  # Remove duplicate food code
                unique_food = remove_duplicate(food_names)  # Remove duplicate food name
                for code in unique_code:  # Loop through each code
                    quantity = codes.count(code)  # Count the total number of code appear in the list before remove duplicate
                    food_quantity.append(quantity)  # Add the total number of code appeared into a list
                    food_details = food_match(code)  # Use the code given to get the details of the food
                    food_price.append(food_details[2])  # Add the individual food price into list
                print("{:43}{:16}{:5}".format("Item", "Item Price(RM)", "Quantity"))
                for i in range(len(unique_code)):  # Loop based on the total number of unique code
                    print("{:3}{:40}{:^13.2f}{:^15}".format(unique_code[i], unique_food[i], float(food_price[i]), food_quantity[i]))  # Display the ordered food details
                print()
                print("-" * 70)
    return_page()


def all_payments():
    all_cust = all_customer()
    print("\n")
    print("[All Orders Payment]".center(54, "="))
    print("-" * 54)
    for name in all_cust:  # Loop through each customer name in the list
        with open(f"{name}.txt", "r") as cust:  # Open the customer's file in reading mode
            payment_id = []
            for lines in cust:  # Loop through each line in the file
                if "payment" in lines:  # If "payment" found in that line
                    line = lines.strip("\n").split(";")  # Split each payment details into a list
                    payment_id.append(line[0])  # Add the payment id into list
            for elem in payment_id:  # Loop through each payment id
                cust.seek(0)  # Place the file handler back to the beginning of the file
                print(f"Order{elem[-3:]}\n")  # Display the order id
                print(f"Customer: {name}")  # Display customer name
                for lines in cust:  # Loop through each line in the file
                    if elem in lines:  # If the particular payment id found in that line
                        payment_details = lines.strip("\n").split(";")  # Split the payment details into a list
                        bill = float(payment_details[1])  # Get the total payment
                print("Total Payment: RM{:.2f}".format(bill))
                print()
                print("-" * 54)
    return_page()


def specific_payment():
    all_cust = all_customer()
    print("\n")
    print("[Specific Customer Payment]".center(54, "="))
    print("All customers:")
    for i in range(len(all_cust)):  # Loop based on the total number of customer
        print(f"{i + 1}. {all_cust[i]}")  # Display all customer names
    name = input("\nEnter a customer name: ")  # Accept customer name from user
    while name not in all_cust:  # If input does not match
        print("\nName does not exist.")
        name = input("Enter a customer name: ")  # Accept customer name from user again
    with open(f"{name}.txt", "r") as cust:  # Open the given customer's file in reading mode
        print()
        print(f"Customer: {name}")
        print("-" * 54)
        payment_id = []
        for lines in cust:  # Loop through each line in the file
            if "payment" in lines:  # If "payment" is found in that line
                line = lines.strip("\n").split(";")  # Split each payment details into a list
                payment_id.append(line[0])  # Add the payment id into a list
        if len(payment_id) == 0:  # Check if the total number of payment id is equal to 0
            print("No orders.")
        else:
            for elem in payment_id:  # Loop through each payment id
                cust.seek(0)  # Place the file handler back to the beginning of the file
                print(f"Order{elem[-3:]}\n")  # Display the order id
                for lines in cust:  # Loop through each line in the file
                    if elem in lines:  # If the particular payment id is found in that line
                        payment_details = lines.strip("\n").split(";")  # Split the payment details into a list
                        bill = float(payment_details[1])  # Get the total payment
                print("Total Payment: RM{:.2f}".format(bill))
                print()
                print("-" * 54)
    return_page()  # Add the payment id into list  # Loop through each order id


def main():
    main_page_opt = main_page()  # Main page is shown and input given by user is assigned to input1

    while main_page_opt != "4":  # Log out if input is 4
        if main_page_opt == "1":
            admin_login_opt = admin_login()  # User is directed to admin login page
            if admin_login_opt is True:  # Check if the username and password exists and matches
                admin_page_opt = admin_page()  # User is directed to admin page
                while admin_page_opt != "9":  # Program terminates if input is 9
                    if admin_page_opt == "1":
                        add_item_opt = add_item()  # User is directed to add item page
                        while add_item_opt == "1":
                            add_item_opt = add_item()  # User can continue adding more item
                    elif admin_page_opt == "2":
                        modify_item_opt = modify_item()  # User is directed to modify item page
                        while modify_item_opt != "3":  # User is redirected back to admin page if input is 3
                            if modify_item_opt == "1":
                                del_confirmation()  # User is directed to delete item page
                            elif modify_item_opt == "2":
                                food = update_food()  # User is directed to update item page and the returned value is stored in food
                                update_food_opt = update_confirmation(food)  # User is asked for update confirmation
                                if update_food_opt == "1":
                                    update_process_opt = update_process()  # User proceeds to choose to make the desired changes
                                    if update_process_opt == "1":
                                        update_food_name(food)  # User changes the food name
                                    elif update_process_opt == "2":
                                        update_food_price(food)  # User changes the food price
                                    else:
                                        update_food_desc(food)  # User changes the food description
                                else:
                                    pass  # User is redirected back to modify item page
                            modify_item_opt = modify_item()
                    elif admin_page_opt == "3":
                        view_food_category()  # User is directed to view food category page
                    elif admin_page_opt == "4":
                        admin_view_menu()  # User is directed to view food menu page
                    elif admin_page_opt == "5":
                        all_orders()  # User is directed to view all orders page
                    elif admin_page_opt == "6":
                        all_payments()  # User is directed to view specific order page
                    elif admin_page_opt == "7":
                        specific_order()  # User is directed to view all payments page
                    elif admin_page_opt == "8":
                        specific_payment()  # User is directed to view specific payment page
                    elif admin_page_opt == "10":
                        exit_program()
                    admin_page_opt = admin_page()
                log_out()  # Exit program   # Change to break if want return to main page
        elif main_page_opt == "2":
            username = cust_login()  # # User is directed to customer login page and username is stored after login
            if username is not False:  # Check if the username and password exists and matches
                cart = create_cart(username)  # Create a cart for the customer
                cust_page_opt = cust_page()  # User is directed to customer page
                while cust_page_opt != "3":  # Log out if input is 3
                    if cust_page_opt == "1":
                        view_menu_opt = view_full_menu()  # User is directed to view menu page
                        if view_menu_opt != "2":  # User is redirected back to customer page if input is 2
                            if view_menu_opt == "1":
                                add_cart_opt = add_cart()  # User is directed to add cart page
                                while add_cart_opt[0] == "1":  # If user choose to continue ordering
                                    cart += add_cart_opt[1]  # Add the food into cart
                                    add_cart_opt = add_cart()  # User is directed to add cart page again
                                cart += add_cart_opt[1]  # If user choose to stop ordering, add the food into cart
                            elif view_menu_opt == "3":
                                exit_program()  # Exit program
                    elif cust_page_opt == "2":
                        view_cart_opt = view_cart(cart)  # User is directed to view cart page
                        while view_cart_opt != "4":  # User is redirected back to customer page if input is 3
                            if view_cart_opt == "1":
                                if check_cart(cart) is True:
                                    cart = del_food(cart)  # User is directed to delete page
                            elif view_cart_opt == "2":
                                cart = []
                                print("\nYour cart is cleared.")
                            elif view_cart_opt == "3":
                                payment_opt = payment(cart)  # User is directed to payment page
                                if payment_opt is not False and payment_opt != "2":  # User is redirected back to view cart page if input is 2
                                    confirm_payment(username, cart)  # User is directed to confirm payment page
                                    cart = []
                            view_cart_opt = view_cart(cart)  # User is directed back to view cart page
                    elif cust_page_opt == "4":
                        update_cart(username, cart)  # Customer's cart is saved
                        exit_program()  # Program terminates
                    cust_page_opt = cust_page()  # User is directed back to customer page
                update_cart(username, cart)  # Customer's cart is saved
                log_out()  # Program terminates
        elif main_page_opt == "3":  # User is directed to guest page
            guest_page_opt = guest_page()
            while guest_page_opt != "3":  # User is redirected back to main page if input is 3
                if guest_page_opt == "1":
                    view_menu_opt = view_menu()
                    while view_menu_opt != "1":  # User is redirected back to guest page if input is 3
                        exit_program()  # Exit program
                elif guest_page_opt == "2":
                    signup()  # User is directed to customer signup page
                    break  # User is redirected back to main page after signup is successful
                elif guest_page_opt == "4":  # The program terminates if input2 is 4
                    exit_program()  # Exit program
                guest_page_opt = guest_page()  # User is redirected back to guest page
        main_page_opt = main_page()  # User is redirected back to main page
    exit_program()

if __name__ == "__main__":
    main()
