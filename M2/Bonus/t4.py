'''
Тривалість місяця варіюється від 28 до 31 дня. 
У цій вправі ви створите програму, 
яка читає назву місяця від користувача у вигляді рядка. 
Тоді ваша програма повинна відображати кількість днів у цьому місяці.
Відобразіть «28 або 29 днів» для лютого, щоб зверталися до високосних років.

'''
month = input("Вкажіть назву місяця:").lower()
if month == "січень":
    print("У цьому місяці 31 день.")
elif month == "лютий":
    print("У цьому місяці 28 або 29 днів.")
elif month == "березень":
    print("У цьому місяці 31 день.")
elif month == "квітень":
    print("У цьому місяці 30 днів.")
elif month == "травень":
    print("У цьому місяці 31 день.")
elif month == "червень":
    print("У цьому місяці 30 днів.")
elif month == "липень":
    print("У цьому місяці 31 день.")
elif month == "серпень":
    print("У цьому місяці 31 день.")
elif month == "вересень":
    print("У цьому місяці 30 днів.")
elif month == "жовтень":
    print("У цьому місяці 31 день.")
elif month == "листопад":
    print("У цьому місяці 30 днів.")
else:
    print("У цьому місяці 31 день.")