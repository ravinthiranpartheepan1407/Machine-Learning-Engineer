# Breakdown:
    # Create total no.of smaples
    # Create var for specific category count
    # Compute it with r = 1- p / p where p = specific_category_count / total_count

check_money_bill = str(input("Enter the money bill tupe you want to check: "))

def probability_odds():
    money_bills = {
        "100_bills": 20,
        "200_bills": 50,
        "500_bills": 100,
        "2000_bills": 35,
    }
    get_bill_type = money_bills.get(check_money_bill)
    # print(get_bill_type)
    total = money_bills.get("100_bills") + money_bills.get("200_bills") + money_bills.get("500_bills") + money_bills.get("2000_bills")
    # print(total)
    compute_selection = 1 - (get_bill_type/total) / (total/get_bill_type) # (n/m) / (m/n)
    print(f'The probability of the selected bill type among the entire bill type collections is: {compute_selection}')

probability_odds()
