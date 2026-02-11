def greet(name):
    """Say hello nicely"""
    return f"👋 Hello {name}!"

def calc_tip(bill,tip_percent=15):
    """Calculate restaurant tip"""
    tip = bill * (tip_percent / 100)
    total = bill + tip
    return total

#Use the functions!
name = input("Your name? ")
print(greet(name))

bill = float(input("Restaurant bill? $"))
total = calc_tip(bill,20)
print(f"Total with 20% tip: ${total:.2f}")