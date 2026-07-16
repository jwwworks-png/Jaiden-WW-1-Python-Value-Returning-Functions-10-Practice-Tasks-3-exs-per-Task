#1
def calculate_assets(liabilities, equity):
    return liabilities + equity

liabilities = 40000
equity = 60000
company_name = input("Enter Company Name: ")
liabilities = float(input("Enter Liabilities: "))
equity = float(input("Enter Equity: "))
assets = calculate_assets(liabilities, equity)
print("\nCompany:", company_name)
print("Assets:", assets)
print("Liabilities:", liabilities)
print("Equity:", equity)
assets = calculate_assets(liabilities, equity)
print("Assets:", assets)
#2
company_name = input("Enter Company Name: ")
liabilities = float(input("Enter Liabilities: "))
equity = float(input("Enter Equity: "))
assets = calculate_assets(liabilities, equity)
print("\nCompany:", company_name)
print("Assets:", assets)
print("Liabilities:", liabilities)
print("Equity:", equity)
#3
company_a = input("Enter name for Company A: ")
liab_a = float(input(f"Enter Liabilities for {company_a}: "))
eq_a = float(input(f"Enter Equity for {company_a}: "))
assets_a = calculate_assets(liab_a, eq_a)
company_b = input("Enter name for Company B: ")
liab_b = float(input(f"Enter Liabilities for {company_b}: "))
eq_b = float(input(f"Enter Equity for {company_b}: "))
assets_b = calculate_assets(liab_b, eq_b)
company_c = input("Enter name for Company C: ")
liab_c = float(input(f"Enter Liabilities for {company_c}: "))
eq_c = float(input(f"Enter Equity for {company_c}: "))
assets_c = calculate_assets(liab_c, eq_c)
combined_assets = assets_a + assets_b + assets_c
print(f"\n{company_a}")
print(f"Assets: {assets_a}")
print(f"\n{company_b}")
print(f"Assets: {assets_b}")
print(f"\n{company_c}")
print(f"Assets: {assets_c}")
print(f"\nCombined Assets: {combined_assets}")