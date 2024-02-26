#calculate the final price after applying a discount.
#price function is the original price
def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        discount = price * discount_percent
        final_price = price - discount
        return abs((final_price))
    else:
        return abs((price))

#prompt the user to enter the original price and discount percentage
price = float(input("Enter the original price"))
discount_percent = float(input("Enter the discount percentage"))

#calculate the final_price using the calculate_discount() 
#print the output based on the application or no_application of dicount.
final_price = calculate_discount(price, discount_percent) 
if final_price != price:
    print(final_price)
else:
    print(price)
