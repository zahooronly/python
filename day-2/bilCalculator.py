bill = float(input('What is the total bill? '))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
totalBill = round(bill*(1+tip/100), 2)
print(f'Your total bill is ${totalBill}.')
