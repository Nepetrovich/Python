# 6.Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input("Введите результаты пробежки первого дня в километрах: "))
b = int(input("Введите желаемый результат пробежки в километрах: "))
days = 0
while a < b:
    a = a * 1.1
    days += 1
print(f"На {days+1}-й день спортсмен достигнет результата — не менее {b} км.")

# Добавила в результат "+1", чтобы не потерять первый день. Возможно, это можно сделать по-другому,
# но я пока не придумала, как именно:)