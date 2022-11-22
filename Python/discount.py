class discount:
    def discount():
        sales = int(input("Enter the sales price : "))        
        dis = int(input("Enter the discount percentage : "))
        discount = sales * (100 - dis)/ 100
        print(f"The discount price is {discount}")
    discount()