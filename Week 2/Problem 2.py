balance = 3329
annualInterestRate = 0.02
month = 0
lowestPayment = 0
unpaidBalance = balance
interest = 0

while balance >= 0:
    lowestPayment += 10

    for month in range(12):
        balance -= (lowestPayment)
        interest = ((annualInterestRate / 12) * balance)
        balance += interest
    if balance > 0:
        balance = unpaidBalance

print ('Lowest Payment: %d' % lowestPayment)
        