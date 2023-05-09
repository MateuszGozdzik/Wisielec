words = [
    "jego",
    "że",
    "on",
    "dla",
    "na",
    "są",
    "zespół",
    "oni",
    "być",
    "jeden",
    "mieć",
    "tego",
    "gorący",
    "słowo",
    "ale",
    "co",
    "niektóre",
    "jest",
    "to",
    "ty",
    "lub",
    "miał",
    "kilka",
    "stopa",
    "do",
    "i",
    "ciągnąć",
    "puszka",
    "zewnątrz",
    "inne",
    "były",
    "który",
    "ich",
    "czas",
    "jeśli",
    "będzie",
    "powiedział",
    "próba",
    "każda",
    "zestaw",
    "trzy",
    "chcą",
    "powietrze",
    "dobrze",
    "również",
    "grać",
    "mały",
    "koniec",
    "wkładać",
    "strona",
    "czytaj",
    "ręka",
    "port",
    "zaklęcie",
    "dodać",
    "nawet",
    "tutaj",
    "musi",
    "wysoki",
    "takie",
    "śledzić",
    "akt",
    "dlaczego",
    "zapytaj",
    "mężczyźni",
    "zmiana",
    "poszedł",
    "światła",
    "rodzaj",
    "potrzeba",
    "dom",
    "obraz",
    "spróbuj",
    "nas",
    "ponownie",
    "zwierząt",
    "punkt",
    "matka",
    "świat",
    "blisko",
    "budować",
    "własny",
    "ojciec",
    "dowolny",
    "nowy",
    "praca",
    "część",
    "wziąć",
    "dostać",
    "miejsce",
    "wykonane",
    "żyć",
    "gdzie",
    "później",
    "powrotem",
    "mało",
    "okrągły",
    "mężczyzna",
    "rok",
    "spokojnie",
    "pokaż",
    "każdy",
    "dobry",
    "mnie",
    "dać",
    "nasze",
    "pod",
    "nazwa",
    "bardzo",
    "formularz",
    "zdanie",
    "wielki",
    "myśleć",
    "pomoc",
    "niski",
    "linia",
    "różnią",
    "kolej",
    "przyczyna",
    "oznaczać",
    "przed",
    "ruch",
    "prawo",
    "chłopiec",
    "stary",
    "zbyt",
    "sam",
    "ona",
    "wszystko",
    "tam",
    "kiedy",
    "góra",
    "zastosowanie",
    "twój",
    "sposób",
    "o",
    "następnie",
    "im",
    "pisać",
    "byłoby",
    "tak",
    "te",
    "ją",
    "długo",
    "rzecz",
    "zobaczyć",
    "mu",
    "dwa",
    "ma",
    "szukać",
    "więcej",
    "dzień",
    "iść",
    "przyjść",
    "liczba",
    "brzmieć",
    "najbardziej",
    "ludzie",
    "ponad",
    "wiem",
    "woda",
    "niż",
    "wezwanie",
    "pierwszy",
    "kto",
    "dół",
    "bok",
    "teraz",
    "odnaleźć",
    "w",
    "jak",
    "duży",
    "z",
    "ziemia",
    "przez",
    "tylko",
    "powiedzieć",
    "wiele",
    "zrobić",
    "nie",
    "my",
    "może",
    "było",
]

import random


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


# word = input("Podaj Słowo\n")
word = random.choice(words)
print(word)

len_word = len(word)
list_letters = [letter.lower() for letter in word]
hp = len_word
run = True


print(f"Hasło ma {len_word} liter")
while run:
    print(f"Pozostała ilość życia: {hp}")
    litera = input("Podaj literę lub całe słowo\n").lower()
    if len(litera) > 1:
        if litera == word:
            print("\n\n\nWygrałeś!")
            run = False
        elif litera != word:
            hp -= 1
    else:
        if litera in list_letters:
            idx = find(word, litera)
            print(f"{litera} występuje na pozycjach: {[i + 1 for i in idx]}")
            list_letters = [l for l in list_letters if l != litera]
        else:
            print("Próbuj dalej")
            hp -= 1

    if hp == 0:
        print("\n\n\nPrzegrałeś")
        run = False
    if list_letters == []:
        print("\n\n\nWygrałeś!")
        run = False

print(f"Słowo: {word}")
