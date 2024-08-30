
def calculate_discount(price, discount_percent):

    # Check if the discount percent provided is >= 20%
    if discount_percent >= 20.0:
        final_price = price - (price * discount_percent / 100 )
        print(f"Final Price = Le{final_price}")
        return final_price
    else:
        print(f"No discount applied because the discount percent provided is below 20%. Fianl Price = Le{price}")
        return price


# Prompte the user to provide input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percent of the item: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percent)





 
