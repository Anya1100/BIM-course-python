money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
allm = 0
m = money_capital + salary - spend
while m > 0
    spend = spend + spend * increase
    m = m + salary - spend
    allm += 1



print("Количество месяцев, которое можно протянуть без долгов:", allm)
