shipment_status = ["pending", "sent", "reached"]
shipment_id = input("Enter Item Id: ")
item_id = [10,20,30]

def assign_shipment_id(shipment_id):
    while True:
        try:
            if int(shipment_id) in item_id:
                print("Shipment verified and ID is: ", shipment_id)
                print(shipment_status[1])
                return shipment_id
        except:
            raise ValueError("Shipment ID should be in Numerical form")
        else:
            print("Shipment ID out of range")
            break

print(assign_shipment_id(shipment_id))

    
