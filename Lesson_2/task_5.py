# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = [7, 5, 3, 3, 2]
print(f"Рейтинг выглядит следующим образом: {rating}")
num = int(input("Введите новый элемент рейтинга (для окончания программы введите число 1000): "))
while num != 1000:
    for el in range(len(rating)):
        if rating[el] == num or rating[el] > num > rating[el + 1]:
            rating.insert(el + 1, num)
            break
        elif rating[0] < num:
            rating.insert(0, num)
        elif rating[-1] > num:
            rating.append(num)
    print(f"Новый рейтинг: {rating}")
    num = int(input("Введите новый элемент рейтинга(для окончания программы введите число 1000): "))