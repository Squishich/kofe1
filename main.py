def matem(rashet, centiki) :
    if (rashet-centiki(bibor) == 0):
        print('наливается кофе')
    elif(rashet-centiki(bibor)>0):
        print('наливается кофе','ваша сдача -',rashet-centiki(bibor))
    else:
        while(centiki(bibor)-rashet>0):
            print('вложите ещё',centiki(bibor)-rashet)
            rashet = int(input())

a = 'латте'
b = 'капучино'
c = 'американо'
d = 'kakao'
e = 'экспрессо'
f = 'мокко'

a2 = 100
b2 = 150
c2 = 200
d2 = 170
e2 = 75
f2 = 110
# программа одноразка(работает при покупке кофе только по безналу и заканчивается
# почитай что такое циклы в python, они едентичны с Си
nomerkofe = (1,2,3,4,5,6)
spisokKofe = (a,b,c,d,e,f)
centiki = (a2,b2,c2,d2,e2,f2)
# зачем соединять списки?
for i in zip(nomerkofe,spisokKofe,centiki):
    print (*i)

print('выберете HoMep кофе:')
bibor =int(input())
if (bibor>6 or bibor<0):
    print('неверный ввод')
else:
    print('ваш кофе -', spisokKofe[bibor-1])
    print('выберете способ оплаты (1)безнал/(2)наличка')
    oplata=int(input())
if (oplata == 1):
    print('кофе наливается')
elif(oplata == 2):
    print('внесите оплату')
    rashet = int(input())
    #при вводе налички программа падает на 45 строке при вызове функции
    matem(rashet, centiki)
else:
    print('неверный способ оплаты')
