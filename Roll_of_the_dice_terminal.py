import random

TYPE_KUB = { 4 : "Тетраэдр",
             6 : "Куб",
             8 : "Октаэдр",
             12 : "Додекаэдр",
             20 : "Икосаэдр",
             100 : "Зоккиэдр"
             }

GAME = True

def selection_menu():
    list_num = list()
    list_num.append("|{:^12}|{:^12}|".format("Terminology", "Facets")) 
    for name, val in TYPE_KUB.items():
        list_num.append("|{:<12}|{:>12}|".format(val, name)) 
    return list_num

def user_input():    
    type_kud_uzer = input("Select Cube: >>> ")
    number_of_throws = int(input("How many dice to throw?: >>> "))     
    return type_kud_uzer, number_of_throws

while GAME:

    for el in selection_menu():
        print(el)

    type_kud_uzer, number_of_throws = user_input()
    type_kud_uzer = int(type_kud_uzer)

    for type_k, facet in TYPE_KUB.items():
        if type_kud_uzer == type_k:
            type_kubs = facet
            break

    for i in range(0, number_of_throws):
        list_kub = []
        list_kub.append(random.randint(1, type_kud_uzer))
        print(list_kub, type_kubs)
        
    if GAME:
        exit = input("To close enter: Exit >>> ")
        if exit in "exit":
            GAME = False
