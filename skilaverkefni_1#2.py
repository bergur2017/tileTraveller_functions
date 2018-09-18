## skilaverkefni 1, Bergur Gardar og Brynjar Orri


lan = float(input("Input the cost of the item in $: "))
counter = 0
if lan >= 2500:
    print('The cost is too much')

elif lan <= 1000:
    r = 0.015
else:
    r == 0.02
total_int_paid = 0
while lan > 0:
    if lan > 49.8:
        payment = 50
        counter += 1
        int_paid = lan*r
        rem_debt = payment-int_paid
        lan = lan - rem_debt
        total_int_paid += int_paid
        print('Month:',counter, 'Payment:',round(payment,2), 'Interest paid:',round(int_paid,2), 'Remaining debt:' ,round(lan,2))
    else:
        counter += 1
        int_paid = lan*r
        payment = lan+int_paid
        lan = lan - (payment-int_paid)
        print('Month:',counter, 'Payment:',round(payment,2), 'Interest paid:',round(int_paid,2), 'Remaining debt:' ,round(lan,2))
        total_int_paid += int_paid
        print('')
        print('Number of months:',counter)
        print('Total interest paid:',round(total_int_paid,2))