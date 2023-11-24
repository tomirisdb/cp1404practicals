"""
total_price = 0
PRICE_THRESHOLD = 100
DISCOUNT = 0.1
get items
while items < 0
    display "Invalid number of items!"
    get items
for i in range(items)
    get price
    total price = total_price + price
if total_price > PRICE_THRESHOLD
     new_price = total_price - total_price*DISCOUNT
    display items, new_price
else
    display items, total_price
"""
total_price = 0
PRICE_THRESHOLD = 100
DISCOUNT = 0.1
items = int(input("Enter the number of items: "))
while items < 0:
    print("Invalid number of items!")
    items = int(input("Enter the number of items: "))
for i in range(items):
    price = float(input("Price of item: "))
    # Add the price of the current item to the total price
    total_price += price
if total_price > PRICE_THRESHOLD:
    new_price = total_price - total_price*DISCOUNT
    print(f"Total price for {items} is ${new_price:.2f}")
else:
    print(f"Total price for {items} is ${total_price:.2f}")
