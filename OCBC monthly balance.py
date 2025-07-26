# Calculates balance to maintain in OCBC 360 Account
import datetime as dt
import calendar

# Collect necessary info to perform calc
monthly_balance = float(input("Enter current monthly balance: \n"))
monthly_balance_change = float(input("Enter monthly balance change vs last month: \n"))
ledger_bal = float(input("Enter ledger balance: \n"))

# Target monthly balance
target_monthly_balance = monthly_balance - monthly_balance_change + 500

# Calculation
num_days_in_month = calendar.monthrange(dt.datetime.now().year, dt.datetime.now().month)[1]
# 1 is subtracted from the calculation below to accurately account for days passed e.g. on 2nd of the month,
# 1 day passed
days_passed = dt.datetime.now().day - 1
days_left_in_month = num_days_in_month - days_passed
acct_bal_to_maintain = (target_monthly_balance * num_days_in_month - days_passed * monthly_balance) / days_left_in_month
amount_to_withdraw = ledger_bal - acct_bal_to_maintain

print(f'number of days left in the month is: {days_left_in_month}')
print(f"Target monthly balance is: ${target_monthly_balance}")
print("You need to withdraw: ${:0.2f}".format(amount_to_withdraw))