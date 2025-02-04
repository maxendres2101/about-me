price = 50
money_due = 50
print('Amount Due:', price)


while money_due > 0:
    inserted = int(input('Insert Coin: '))
    if inserted == 25 or inserted == 5 or inserted == 10:
        if inserted >= money_due:
            print('Amount Due: 0')
            money_owed = inserted - money_due
            print('Change Owed:', money_owed)
            break
        else:
            money_due -= inserted
            print('Amount Due:', money_due)
    else:
        print('Amount Due:', money_due)

