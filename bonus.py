price =int(input("enter the price:"))
if(price>=1000):
    discount =0.05*price
    print("the discount is",discount)
    amount_payable=price-discount
    print(amount_payable)
else:
    print("no discount")