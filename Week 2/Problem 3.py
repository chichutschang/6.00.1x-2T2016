#balance = 320000
#annualInterestRate = 0.2
month = 0
monthlyInterestRate = annualInterestRate / 12.0
lowerBound = balance / 12
upperBound = (balance * (( 1 + monthlyInterestRate)**12) / 12.0)
lowestPayment = (lowerBound + upperBound) / 2
unpaidBalance = balance
                            
while True:
    for month in range(12):
        balance -= (lowestPayment)
        interest = ((annualInterestRate / 12) * balance)
        balance += interest

    if abs(balance) < 0.1:   
        print ('Lowest Payment: %.2f' % lowestPayment)
        break
                                    
    else:
        if balance < 0:
            upperBound = lowestPayment
        elif balance > 0:
            lowerBound = lowestPayment
            
        lowestPayment = (lowerBound + upperBound) / 2
        balance = unpaidBalance