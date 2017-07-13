


def cal_annual (balance,annualInterestRate,monthlyPaymentRate):
    Monthly_interest_rate= (annualInterestRate) / 12.0
    Minimum monthly payment = (monthlyPaymentRate) x (Previous balance)
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)