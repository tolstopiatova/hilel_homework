credit = int(input('Введіть суму кредиту: '))
save_credit = credit
# Погашення за 1 рік
print("Погашення за 1 рік: ")
platizh = credit / 12
j=1
while j <= 12:
    prozent = credit * 0.02
    credit = credit - platizh
    monthly_payment = platizh + prozent
    print(f'Місяць {j:2}: Платіж: {monthly_payment:.2f}, Відсотки: {prozent:.2f}')
    j = j + 1

# Погашення за 5 років
print("Погашення за 5 років: ")
platizh = save_credit / 60
i = 1
while i <= 60:
    if i <= 24:
        prozent = save_credit * 0.02
    else:
        prozent = save_credit * 0.04
    monthly_payment = platizh + prozent
    save_credit = save_credit - platizh
    print(f'Місяць {i:2}: Платіж: {monthly_payment:.2f}, Відсотки: {prozent:.2f}')
    i += 1