friend='Максим'
print(friend)
#тип данных str
print(type(friend))

friend="Максим"

print(type(friend))
#тип данных str(условие:одни и теже ковычки в начале и конце)

say='say "Hello"'
print(say)

say="say 'Hello'"
print(say)
#первая буква в str
firsr_letter=friend[0]
print(firsr_letter)
#вторая с конца
firsr_letter=friend[-2]
print(firsr_letter)

print(friend[-1+2])
print()
#Срезы
print(friend[0:4])
print()
#c [0]по[2]
print(friend[:2])
print()
#c [2]по[последний]
print(friend[2:])

#Функция len (4:50)