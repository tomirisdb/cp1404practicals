"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
Pseudocode:
LOW_THRESHOLD_DISCOUNT = 0.1
HIGH_THRESHOLD_DISCOUNT = 0.15
SALES_THRESHOLD= 1000
get sales
while sales >= 0
    if sales >= SALES_THRESHOLD
        message = sales*HIGH_THRESHOLD_DISCOUNT
    else
        message = sales*LOW_THRESHOLD_DISCOUNT
    print(message)
    get sales
display thank you message
"""
LOW_THRESHOLD_DISCOUNT = 0.1
HIGH_THRESHOLD_DISCOUNT = 0.15
SALES_THRESHOLD = 1000
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= SALES_THRESHOLD:
        message = sales*HIGH_THRESHOLD_DISCOUNT
    else:
        message = sales*LOW_THRESHOLD_DISCOUNT
    print(message)
    sales = float(input("Enter sales: $"))
print("Thank you!")


