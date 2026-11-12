def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


def calculate_bill(price, quantity=1, gst=0.05):
    total = price * quantity
    tax = total * gst

    return total, tax


def scope_example():
    global count
    count = 10

    def inner():
        nonlocal_value = 20
        print("Local:", nonlocal_value)

    inner()
    print("Global:", count)


print(add_item_buggy("Tea"), add_item_buggy("Vada"))
print(add_item("Tea"), add_item("Vada"))

print(add_item_buggy.__defaults__)

print("Customer 1:", add_item("Tea"))
print("Customer 2:", add_item("Coffee"))
print("Customer 3:", add_item("Juice"))

total, gst = calculate_bill(100, quantity=2)

print("Total:", total)
print("GST:", gst)

scope_example()