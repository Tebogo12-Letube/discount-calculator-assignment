def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage (0-100)
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item (ZAR): "))
discount = float(input("Enter the discount percentage (0-100): "))

# Calculate and display result
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: ZAR {final_price:.2f}")
else:
    print(f"No discount applied. Original price: ZAR {original_price:.2f}")