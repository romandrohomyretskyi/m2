'''
Прийнято говорити, що один людський рік еквівалентний 7 собачим рокам.
Однак це просте перетворення не визнає, що собаки досягають дорослого 
віку приблизно через два роки. В результаті деякі люди вважають, 
що кожен з перших двох людських років краще вважати 10,5 собачими роками, 
а потім вважати кожен наступний людський рік 4 собачими роками.
Напишіть програму, яка реалізує переклад з людських років в собачі роки, 
описані в попередньому пункті. Переконайтеся,
що ваша програма працює правильно для конверсій менше двох людських років 
і для конверсій двох або більше людських років. Ваша програма повинна видавати 
відповідне повідомлення про помилку, якщо користувач вводить від'ємне число.

'''

humanyears = int(input("Скільки вам років?"))

try:
    if humanyears <= 0:
        print("Помилка!")
    elif humanyears <= 2:
        dogyears = humanyears * 10.5
    elif humanyears > 2: 
        dogyears = 21 + (humanyears - 2) * 4
    print(f"Це по собачому: {int(dogyears)} :)")
except:
    print("Введіть додатнє число!")



