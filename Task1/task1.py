print("BPP Pizza Price Calculator")
print("="*25)


def inp():
    
    """
    Retrieves user inputs related to pizza orders and services.

    This function prompts the user for information regarding their pizza order, including:
    - Number of pizzas ordered (ensures a non-negative integer input)
    - Preference for delivery (accepts 'yes'/'no' or 'y'/'n')
    - Confirmation if it's Tuesday (accepts 'yes'/'no' or 'y'/'n')
    - Confirmation of app usage (accepts 'yes'/'no' or 'y'/'n')

    Returns:
        - Number of pizzas ordered (integer)
        - Delivery preference (string: 'yes'/'no')
        - Confirmation if it's Tuesday (string: 'yes'/'no')
        - Confirmation of app usage (string: 'yes'/'no')
    """
    # Infinite loop to repeatedly prompt the user for the number of pizzas ordered.
    # It ensures that the input is a non-negative integer and breaks out of the loop when a valid input is provided.
    while True:
        try:
            no_of_pizza = int(input("\n How many pizzas ordered? "))
            if no_of_pizza < 0:
                raise ValueError("NegativeError: Input cannot be negative")
            break  
        except ValueError:
            print('Invalid input. Please enter a valid number')
    
    # Infinite loop to repeatedly prompt the user for the preference for delivery.
    # It validates that the input is either 'yes'/'no'/'y'/'n' (case-insensitive) and breaks out of the loop when a valid input is provided.
    while True:
        try:
            delivery = input("\nIs delivery required? ")
            if delivery.lower() not in ["yes","y","no","n"]:
                raise ValueError("Please enter 'yes', 'no', 'y', 'n',Can be both in capslock or not.")
            break
        except ValueError as ve:
            print(ve) 
    
    # Infinite loop to repeatedly prompt the user for confirmation if it is Tuesday.
    # It validates that the input is either 'yes'/'no'/'y'/'n' (case-insensitive) and breaks out of the loop when a valid input is provided.
    while True: 
        try:               
            day = input("\nIs it Tuesday? ")
            if day.lower() not in ["yes","y","no","n"]:
                raise ValueError("Please enter 'yes', 'no', 'y', 'n',Can be both in capslock or not.")
            break
        except ValueError as ve:
            print(ve)
    
    # Infinite loop to repeatedly prompt the user for confirmation if the customer used the app.
    # It validates that the input is either 'yes'/'no'/'y'/'n' (case-insensitive) and breaks out of the loop when a valid input is provided.
    while True:
        try:
            app = input("\nDid the customer use the app? ")
            if app.lower() not in ["yes","y","no","n"]:
                raise ValueError("Please enter 'yes', 'no', 'y', 'n',Can be both in capslock or not.")
            break
        except ValueError as ve:
            print(ve)            
    
    return no_of_pizza, delivery, day, app  # Return the gathered information :  (no_of_pizza, delivery, day, app)

def delivery_cost(delivery, no_of_pizza):
    
    """
    Calculates the delivery cost based on the delivery preference and the number of pizzas ordered.
    
    Args:
    - delivery (str): Preference for delivery ('yes'/'no' or 'y'/'n').
    - no_of_pizza (int): Number of pizzas ordered.
    
    Returns:
    - float: The delivery cost calculated based on the conditions:
        - If delivery is requested ('yes'/'y') and the number of pizzas is less than 5, a cost of 2.5 is returned.
        - If delivery is requested and the number of pizzas is 5 or more, the delivery cost is 0.
        - If delivery is not requested ('no'/'n'), the delivery cost is 0.    
    """
     
    if delivery.lower() == 'yes' or delivery.lower() == 'y':  # Check if delivery is requested and the number of pizzas is less than 5
        if no_of_pizza < 5:
            return 2.5 
        else:  # If the number of pizzas is 5 or more, delivery cost is 0
            return 0
    else:  # If delivery is not requested, the delivery cost is 0
        return 0

def day_discount(day, total_price):
    
    """
     Calculates the discount amount based on a specified day.

    Args:
    - day (str): Confirmation if a specific day is considered ('yes'/'no' or 'y'/'n').
    - total_price (float): Total price of the order.

    Returns:
    - float: The discount amount calculated based on the condition:
        - If the specified day is confirmed ('yes'/'y'), a 50% discount is applied to the total price.
        - If the specified day is not confirmed ('no'/'n'), the discount amount is 0.
    """
    # Check if the specified day is confirmed
    if day.lower() == 'yes' or day.lower() == 'y':  # If confirmed, apply a 50% discount to the total price
        discount_amount = (50 / 100) * total_price
    else:  # If not confirmed, the discount amount is 0
        discount_amount = 0
    return discount_amount


def app_discount(app, total_price):
    
    """    
    Calculates the discount amount based on whether the customer used an app for the order.

    Args:
    - app (str): Confirmation if the customer used an app ('yes'/'no' or 'y'/'n').
    - total_price (float): Total price of the order.

    Returns:
    - float: The discount amount calculated based on the condition:
        - If the customer used the app ('yes'/'y'), a 25% discount is applied to the total price.
        - If the customer did not use the app ('no'/'n'), the discount amount is 0.
    """
    
    if app.lower() == 'yes' or app.lower() == 'y':   # Check if the customer used the app, regardless of case ('yes'/'y')
        app_discount_amount = (25 / 100) * total_price  # Calculate the discount amount when the app is used (25% of the total price)
    else:  # If the customer did not use the app, set the discount amount to 0
        app_discount_amount = 0
    return app_discount_amount  # Return the calculated app discount amount

def calculate_total_price(no_of_pizza, delivery, day, app):
    """
    Calculates the total price of a pizza order considering various factors.

    Args:
    - no_of_pizza (int): Number of pizzas ordered.
    - delivery (str): Preference for delivery ('yes'/'no' or 'y'/'n').
    - day (str): Confirmation if a specific day is considered ('yes'/'no' or 'y'/'n').
    - app (str): Confirmation if the customer used an app ('yes'/'no' or 'y'/'n').

    Returns:
    - float: The total price calculated based on the given parameters, including:
        - Cost of the pizzas (each pizza costs $12).
        - Delivery cost (if applicable, based on the number of pizzas ordered).
        - Day-based discount (if applicable).
        - App-based discount (if applicable).
    """
    pizza_cost = no_of_pizza * 12 # Calculate the cost of pizzas based on quantity
    total_price = pizza_cost + delivery_cost(delivery, no_of_pizza)  # Calculate the total price considering pizza cost and delivery cost
    
    # Apply any applicable day-specific discounts
    discount = day_discount(day, pizza_cost)  
    total_price -= discount
    
    # Apply app-specific discount
    app_discount_amount = app_discount(app, total_price)
    total_price -= app_discount_amount
    return total_price # Returns total price

def display(total_price):
    
    """
    Displays the detailed breakdown and grand total of the pizza order.

    Args:
    - total_price (float): The total price of the pizza order.

    Output:
    - Prints a detailed breakdown including the total pizza price, Tuesday discount, App discount, Delivery cost,
      and the grand total, with currency symbol and precision.
    """
    
    app_discount_amount = app_discount(app, total_price)  # Calculate the app discount amount
    discount_amount=day_discount(day, total_price) # Calculate the day discount amount
    dilivery_cost= delivery_cost(delivery, no_of_pizza) # Calculate the delivery cost
    
    # Display the receipt header
    print("\n\n")
    
    print("BPP pizza recipt".center(37))
    print("="*40)
    
    # Display individual components with labels and amounts
    print(f"Total pizza price:".ljust(25) + f"{no_of_pizza*12:.2f}".rjust(6))
    print(f"Tuesday discount:".ljust(25)+f"-{discount_amount:.2f}".rjust(6))
    print(f"App discount:".ljust(25)+f"-{app_discount_amount:.2f}".rjust(6))
    print(f"Delivery cost".ljust(25)+f"+{dilivery_cost:.2f}".rjust(6))
    print("="*40)
    
    # Display the grand total
    print("GRAND TOTAL:".ljust(25)+ f"£{total_price:.2f}".rjust(5))



no_of_pizza, delivery, day, app = inp()  # Get user input for number of pizzas, delivery details, day, and app usage
total_price = calculate_total_price(no_of_pizza, delivery, day, app)  # Calculate the total price of the pizza order
display(total_price)  # Display the receipt with detailed information about the order
