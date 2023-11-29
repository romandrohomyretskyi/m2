'''
!LOOPS

Напишіть програму, яка відображає таблицю перетворення температури градусів 
Цельсія і градусів Фаренгейта. 
Таблиця повинна включати рядки для всіх температур від 0 до 100 градусів Цельсія, 
кратних 10 градусам Цельсія. Додайте відповідні заголовки до стовпців. 
Формулу перекладу між градусами Цельсія і градусами Фаренгейта можна знайти в 
інтернеті.


'''
    
print("Градуси Цельсія\tГрадуси Фаренгейта")

for c in range(0, 101, 10): #для с від 0 до 100, з кроком 10
    f = c * 9/5 + 32 #підставляємо значення 
    print(f"{c}\t\t\t{f}") #відображаємо текст у вигляді таблиці за допомогою трьох табуляцій
