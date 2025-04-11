# Q4 Write a program that calculates the discount on a product based 
# on the following criteria:
# If the price is greater than $1000, a discount of 10% is applied.
# If the price is between $500 and $1000, a discount of 5% is applied.
# If the price is below $500, no discount is applied

user=int(input("enter the price:"))



if user>1000:
    discount=10

elif user>=500:
    discount=5
else:
    discount=0


discount_amount = user * discount / 100
final_price = user - discount_amount


print(f"Original Price: {user}")
print(f"Discount Applied: {discount}%")
print(f"Discount Amount: {discount_amount}")
print(f"Final Price after Discount: ${final_price}")

