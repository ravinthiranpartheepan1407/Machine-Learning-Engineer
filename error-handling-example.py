selected_products = str(input("Select a product to purchase: "))
products = ["pencil", "pen", "eraser"]
append_items = []
fixed_pay = int(20)

def scan_items(selected_products):
    while(True):
        try:
            if selected_products in products:
                print("Product is available for purchase")
                return selected_products
        except ValueError as err:
            print("The added product name is in form of string", err)
        else:
                print("Product is not availabe")
                print("Please enter product to add it to your cart")
                add_product = str(input("Add Product: "))
                append_items.append(add_product)
                print(f'Successfully added {add_product} product')
                break

pay = int(input("Pay the price for your selected products: "))
def purchase_products(pay):
    try:
        if selected_products in products and pay == fixed_pay:
            print("You have successfully purchased this product")
    except ValueError as err:
        print("The payment is not in form of numbers", err)
    else:
        print("Thank you for purchasing!")
    finally:
        print("process completed")

print(scan_items(selected_products))
print("Appended Products are: ", append_items)
print(purchase_products(pay))


