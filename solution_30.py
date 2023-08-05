def arithm_prog(a_1, d, n):
    return [a_1 + (i - 1) * d for i in range(1, n + 1)]

first_term = int(input('Введите первый член арифметической прогрессии: '))
difference = int(input('Введите разность: '))
quantity = int(input('Введите кол-во членов арифм прогрессии: '))

print(*arithm_prog(first_term, difference, quantity))