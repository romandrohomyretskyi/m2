'''
На змагання з квідичу прийшло багато студентів. 
Їм необхідно об'єднатися в дві команди. 
Для цього кожному учаснику видали свій унікальний номер. 
Гамблдор оголосив, що всі учасники з непарними номерами 
гратимуть в команді «Гріфендор», а всі інші - в команді «Слизерін». 
Нумерація учасників починається з числа "а", останній учасник 
зареєстрований під номером "b". Виведіть у стовпчик номери 
всіх студентів, які будуть грати в команді «Слизерін».
'''
a = int(input("Введіть номер першого зареєстрованого учасника:"))
b = int(input("Введіть номер останнього зареєстрованого учасника:"))

i = a
print("Номери всіх студентів, які будуть грати в команді «Слизерін»:")
while i in range(a, b+1):
    if i %2 == 0:
        print(i)
    i = i + 1