def withdraw_money(current_balance, amount):
    if (current_balance >= amount):
        current_balance = current_balance-amount
    else:
        print("Insufficient balance!")
    return current_balance

balance = withdraw_money(100, 20)

if (balance <= 20):
    print("Time to recharge!")
else:
    print("Keep on trucking!")