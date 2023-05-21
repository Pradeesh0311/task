def calculate_discounted_price(quantity, price, discount_name):
    if discount_name == "bulk_5_discount" and quantity > 10:
        return price * quantity * 0.95
    elif discount_name == "bulk_10_discount" and quantity > 20:
        return price * quantity * 0.9
    elif discount_name == "tiered_50_discount" and quantity > 30:
        if quantity > 15:
            return (15 * price) + ((quantity - 15) * price * 0.5)
        else:
            return price * quantity
    else:
        return price * quantity


def calculate_shipping_fee(total_quantity):
    package_count = total_quantity // 10
    if total_quantity % 10 != 0:
        package_count += 1
    return package_count * 5


def calculate_total_gift_wrap_fee(quantity):
    return quantity


def apply_discount_rules(total_quantity, cart_total):
    discounts = {
        "flat_10_discount": cart_total - 10,
        "bulk_5_discount": cart_total,
        "bulk_10_discount": cart_total,
        "tiered_50_discount": cart_total * 0.5,
    }
    applied_discount = max(discounts, key=discounts.get)
    return applied_discount, discounts[applied_discount]


product_prices = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

cart = {}
total_quantity = 0
cart_total = 0

for product, price in product_prices.items():
    quantity = int(input("Enter the quantity of {} : ".format(product)))
    is_gift_wrapped = input("Is {} gift-wrapped? (yes/no): ".format(product)).lower() == "yes"

    cart[product] = {
        "quantity": quantity,
        "price": price,
        "gift_wrapped": is_gift_wrapped
    }

    total_quantity += quantity
    cart_total += calculate_discounted_price(quantity, price, "")

sub_total = cart_total
discount_name, discount_amount = apply_discount_rules(total_quantity, cart_total)
cart_total -= discount_amount
shipping_fee = calculate_shipping_fee(total_quantity)
gift_wrap_fee = sum([calculate_total_gift_wrap_fee(item["quantity"]) for item in cart.values() if item["gift_wrapped"]])
total = sub_total - discount_amount + shipping_fee + gift_wrap_fee

# Output
print("\nProduct Details:")
for product, item in cart.items():
    total_amount = item["quantity"] * item["price"]
    print("{0}: Quantity - {1},Total Amount - {2}".format(product, item['quantity'],total_amount ))

print("\nSubtotal:${}".format(sub_total))
print("Discount Applied: {} , Discount Amount: ${}" .format(discount_name,discount_amount))

print("Shipping Fee: ${}".format(shipping_fee))
print("Gift Wrap Fee: ${}".format(gift_wrap_fee))
print("Total: ${}".format(total))