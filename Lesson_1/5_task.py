# 5.Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек фирмы: "))

if revenue > costs:
    profit = (revenue - costs) / costs
    print(f"Фирма работает с прибылью. Рентабельность выручки = {profit:.2f}")
    employees = int(input("Введите численность сотрудников: "))
    profit_empl = (revenue - costs) / employees
    print(f"Прибыль фирмы в расчете на одного сотрудника = {profit_empl:.2f}")
elif revenue < costs:
    print("Фирма работает с убытком")
else:
    print("Прибыль равна убытку. Финансовый результат фирмы равен 0.")