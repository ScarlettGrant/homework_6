from random import randint
def fill_list(lst, a, b):
    return [i for i in range(len(lst)) if a <= lst[i] <= b ] or 'None' 


quantity = int(input('Введите размер списка: '))
nums = [randint(1, 1000) for _ in range(quantity)]

start, end = int(input('Введите правую границу диапазона: ')), int(input('Введите левую границу диапазона: '))

print(*nums)
print(*fill_list(nums, start, end))