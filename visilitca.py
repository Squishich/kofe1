from random import choice

Chel = (
    """
    -------
    !     !
    !
    !
    !
    !
    !
    !.......
    """
    ,
    """
    -------
    !     !
    !     0
    !
    !
    !
    !
    !.......
    """
    ,
    """
    -------
    !     !
    !     0
    !    /!\\
    !
    !
    !
    !.......
    """
    ,
    """
    -------
    !     !
    !     0
    !    /!\\
    !     !
    !
    !
    !.......
    """
    ,
    """
    -------
    !     !
    !     0
    !    /!\\
    !     !
    !    /!\\
    !
    !.......
    """
)

max_oshibka = len(Chel)
Slova = ('хоккей', 'футбол', 'бильярд', 'баскетбол', 'пейнтбол', 'дартс', 'шахматы')

slovo = choice(Slova)

zvezda = '*' * len(slovo)
oshibka = 0
spisok = []

while oshibka < max_oshibka and zvezda != slovo:
    print(Chel[oshibka])
    print('\n вы использовали буквы -\n', spisok)
    print('\n загаданное слово-\n', zvezda)

    predpologi = input('\nВведите букву \n')

    while predpologi in spisok:
        print('буква уже угаданна', predpologi)
        predpologi = input('гадайте букву - ')

    spisok.append(predpologi)

    if predpologi in slovo:
        print('\nВерно,', predpologi, 'есть в этом слове\n')
        new = ''
        for i in range(len(slovo)):
            if predpologi == slovo[i]:
                new += predpologi
            else:
                new += zvezda[i]
        zvezda = new
    else:
        print('\nбуквы \'' + predpologi + '\'нет в слове')
        oshibka += 1

if oshibka == max_oshibka:
    print(Chel[oshibka])
    print('\nТы повешан')
else:
    print('\nПовезло-повезло')
print('\nЗагаданное слово -\'' + slovo + '\'')