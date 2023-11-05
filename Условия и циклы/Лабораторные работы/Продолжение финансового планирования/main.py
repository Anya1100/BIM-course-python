salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
a = 0
s = 0
money = 0

for x in range(1, 11):
    if x == 1:
        money = spend - salary
        a += money
    else:
        spend = spend * increase + spend
        money = spend - salary
        s += money
i = a + s


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f"{i:.2f}")
