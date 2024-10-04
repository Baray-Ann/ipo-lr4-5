a=list(map(int, input("Введите числа списка: ").split()))
print("Ваш список: ", a)
k=0
for i in a:
    if i>10:
        k+=1
print("Количество чисел больше 10: ", k)