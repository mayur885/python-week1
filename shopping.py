cart = ["milk", "bread", "eggs"]
print("Your cart:")
for i, item in enumerate(cart, 1):
    print(f"{i}. {item}")

# Add new item
new_item = input("\nAdd to cart? ")
cart.append(new_item)

print("\nUpdated cart:")
print("  " + ", ".join(cart))
print(f"Total items: {len(cart)}")
