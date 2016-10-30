#balance = 4213
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
monthlyUnpaidBalance = balance
totalPayment = 0
month = 0

for month in range(12):
    month += 1
     
    minimumMonthlyPayment = balance * monthlyPaymentRate   
    totalPayment += minimumMonthlyPayment
        
    monthlyUnpaidBalance = (balance - minimumMonthlyPayment)
    
    interest = round(monthlyUnpaidBalance * (annualInterestRate / 12.0), 2)
    
    balance = round((monthlyUnpaidBalance + interest),2)
    
print ('Remaining balance: %.2f' % round(balance, 2))
