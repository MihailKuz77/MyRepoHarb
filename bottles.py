word='бутылки'

for beer_num in range(99,0,-1):
    print(beer_num,word,'стоит в холодильнике')
    print(beer_num,word,'Холстена')
    print('возьми одну')
    print('пусти по кругу')
    if beer_num==1:
        print('Вот и кончилось пиво. Иди и купи ещё сто бутылок')
    else:
        new_num = beer_num -1
        if new_num >= 11 and new_num <= 19:
            word='бутылок'
        else:
            if new_num %10==1:
                word='бутылка'
            elif new_num %10 in (2 ,3, 4):
                word="бутылки"
            else:
                word="бутылок"
        print(new_num, word, 'стоит в холодильнике')
    print()