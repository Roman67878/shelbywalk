from collections import deque


def search_success(el):
    return ("Успех!!")


def shiroky(el):
    ochered = deque()
    ochered += graph[el]
    prosm = []
    while ochered:
        el_pred = ochered.popleft()
        if not el_pred in prosm:
            print(f"{el_pred} - Найден!!")
        else:
            ochered += graph[el]
            prosm.append(el)
    return False


graph = {
    "Роман Ручкин": ["Никита Долбилин", "Илья Кривенко"],
    "Никита Долбилин": ["Василий Абаринов", "Антон Ткаченко"],
    "Василий Абаринов": ["Иван Иванов", "Петр Петрв"]
}


print(shiroky(el="Иван Иванов"))




    