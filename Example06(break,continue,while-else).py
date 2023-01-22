# break
name=None
while name!= 'Гвидо':#name!= 'Гвидо' можно заменить на True,но токгда внутри цикла должен быть выход(break)
    name = input('Кто создатель Phyton:')
    if name == 'Гвидо':
        break
    print('Неверно')

print('Вертно')

# continue - переход на следующую итерацию цикла
# (команды в цикле после continue не выполняются)
number=0
n=int(input('Введите n: '))
while number<=n:
    if number % 2 == 0:
        number+=1
        continue
    print(number)
    number += 1

# while-else - в блоке else(после while) мы выполняем действия после того
# как вышли из цикла while когда условие стало неверным(false)

number=0
while number <= 100:
    print(number)
    number += 1
    # if number == 9:
    #     break
else:#Можно использовать при выходе из цикла по условию
    print('not - end')

print('end')